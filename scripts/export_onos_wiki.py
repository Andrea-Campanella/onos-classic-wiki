import json
import mimetypes
import os
import posixpath
import re
import shutil
from collections import defaultdict
from html import unescape
from urllib.parse import quote, unquote, urljoin, urlparse, parse_qs

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_URL = "https://wiki.onosproject.org"
SPACE_KEY = "ONOS"
DOCS_DIR = "docs"
ASSETS_DIR = os.path.join(DOCS_DIR, "assets")
CACHE_DIR = os.path.join(DOCS_DIR, ".cache")
API_CONTENT = f"{BASE_URL}/rest/api/content"
USER_AGENT = "ONOS-Wiki-Exporter/1.0 (+GitHub Pages static export)"


def make_session():
    session = requests.Session()
    retry = Retry(
        total=5,
        read=5,
        connect=5,
        backoff_factor=1,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update({"User-Agent": USER_AGENT})
    return session


def sanitize_segment(text):
    text = unquote(text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"[^A-Za-z0-9._\- ]+", "", text)
    text = text.replace(" ", "-")
    text = re.sub(r"-+", "-", text).strip("-._")
    return text.lower() or "page"


def read_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default


def write_json(path, payload):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def reset_output():
    os.makedirs(DOCS_DIR, exist_ok=True)
    os.makedirs(ASSETS_DIR, exist_ok=True)
    os.makedirs(CACHE_DIR, exist_ok=True)
    for entry in os.listdir(DOCS_DIR):
        if entry in {"assets", ".cache"}:
            continue
        path = os.path.join(DOCS_DIR, entry)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def fetch_all_pages(session):
    pages = []
    start = 0
    limit = 100
    print("Fetching page list from Confluence API...")
    while True:
        params = {
            "spaceKey": SPACE_KEY,
            "type": "page",
            "limit": limit,
            "start": start,
            "expand": "ancestors,title,version",
        }
        response = session.get(API_CONTENT, params=params, timeout=60)
        response.raise_for_status()
        data = response.json()
        results = data.get("results", [])
        if not results:
            break
        pages.extend(results)
        print(f"  Fetched {len(pages)} pages so far...")
        start += len(results)
    print(f"  Done — {len(pages)} pages found.\n")
    return pages


def unique_doc_path(segments, page_id, used_paths):
    base_parts = [sanitize_segment(s) for s in segments if str(s).strip()]
    if not base_parts:
        base_parts = [f"page-{page_id}"]
    filename = "index.md" if len(base_parts) == 1 else base_parts[-1] + ".md"
    rel_dir = os.path.join(*base_parts[:-1]) if len(base_parts) > 1 else ""
    rel_path = os.path.join(rel_dir, filename) if rel_dir else filename
    rel_path = rel_path.replace("\\", "/")
    if rel_path not in used_paths:
        used_paths.add(rel_path)
        return rel_path
    alt_filename = f"{base_parts[-1]}-{page_id}.md"
    rel_path = os.path.join(rel_dir, alt_filename) if rel_dir else alt_filename
    rel_path = rel_path.replace("\\", "/")
    used_paths.add(rel_path)
    return rel_path


def build_manifest(pages):
    print("Building page manifest...")
    used_paths = set()
    by_id = {}
    title_to_ids = defaultdict(list)

    for page in pages:
        page_id = page["id"]
        title = page.get("title", f"page-{page_id}")
        ancestors = [a.get("title", "") for a in page.get("ancestors", []) if a.get("title")]
        rel_path = unique_doc_path(ancestors + [title], page_id, used_paths)
        webui = f"{BASE_URL}/pages/viewpage.action?pageId={page_id}"
        by_id[page_id] = {
            "id": page_id,
            "title": title,
            "ancestors": ancestors,
            "webui": webui,
            "path": rel_path,
            "version": page.get("version", {}).get("number"),
        }
        title_to_ids[title].append(page_id)

    print(f"  Manifest built — {len(by_id)} entries.\n")
    return by_id, title_to_ids


def download_bytes(session, url, target_path):
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with session.get(url, stream=True, timeout=120) as response:
        response.raise_for_status()
        with open(target_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 64):
                if chunk:
                    f.write(chunk)


def infer_asset_name(source_url, response_headers=None):
    parsed = urlparse(source_url)
    filename = os.path.basename(parsed.path)
    filename = unquote(filename)
    if not filename:
        filename = "asset"
    if "." not in filename and response_headers:
        content_type = response_headers.get("Content-Type", "").split(";")[0].strip()
        ext = mimetypes.guess_extension(content_type) or ""
        filename += ext
    return sanitize_segment(filename.rsplit(".", 1)[0]) + ("." + filename.rsplit(".", 1)[1] if "." in filename else "")


def rewrite_page_and_assets(session, html, current_page, manifest_by_id, webui_to_path, asset_cache):
    soup = BeautifulSoup(html, "lxml")

    for el in soup.select("script, style"):
        el.decompose()

    assets_downloaded = 0
    assets_skipped = 0

    for tag in soup.find_all(["a", "img"]):
        attr = "href" if tag.name == "a" else "src"
        raw = tag.get(attr)
        if not raw:
            continue
        absolute = urljoin(BASE_URL, raw)
        parsed = urlparse(absolute)

        # Internal page links
        target_page_id = None
        qs = parse_qs(parsed.query)
        if "pageId" in qs and qs["pageId"]:
            target_page_id = qs["pageId"][0]
        elif parsed.path.startswith("/display/"):
            parts = parsed.path.split("/")
            if len(parts) >= 4:
                candidate_title = unquote(parts[3]).replace("+", " ")
                for pid, meta in manifest_by_id.items():
                    if meta["title"] == candidate_title:
                        target_page_id = pid
                        break

        if target_page_id and target_page_id in manifest_by_id:
            target_rel = manifest_by_id[target_page_id]["path"]
            rel = posixpath.relpath(target_rel, posixpath.dirname(current_page["path"]) or ".")
            tag[attr] = rel
            continue

        # Download attachment/media links and localize them
        is_asset = (
            tag.name == "img"
            or "/download/attachments/" in parsed.path
            or re.search(r"\.(png|jpg|jpeg|gif|svg|pdf|zip|tar|gz|tgz|bz2|txt|json|yaml|yml|xml|csv)$", parsed.path, re.I)
        )
        if is_asset and parsed.netloc.endswith("onosproject.org"):
            if absolute not in asset_cache:
                try:
                    print(f"    -> Downloading asset: {absolute}")
                    temp_response = requests.get(
                        absolute, stream=True, timeout=15,
                        headers={"User-Agent": USER_AGENT},
                    )
                    temp_response.raise_for_status()
                    asset_name = infer_asset_name(absolute, temp_response.headers)
                    target = os.path.join(ASSETS_DIR, asset_name)
                    if os.path.exists(target):
                        base, ext = os.path.splitext(asset_name)
                        i = 1
                        while os.path.exists(os.path.join(ASSETS_DIR, f"{base}-{i}{ext}")):
                            i += 1
                        asset_name = f"{base}-{i}{ext}"
                        target = os.path.join(ASSETS_DIR, asset_name)
                    with open(target, "wb") as f:
                        for chunk in temp_response.iter_content(chunk_size=1024 * 64):
                            if chunk:
                                f.write(chunk)
                    temp_response.close()
                    asset_cache[absolute] = f"assets/{asset_name}"
                    assets_downloaded += 1
                except requests.exceptions.RequestException as exc:
                    print(f"    [WARN] Skipping asset {absolute!r}: {exc}")
                    asset_cache[absolute] = None
                    assets_skipped += 1

            if asset_cache[absolute] is None:
                tag[attr] = absolute
                continue
            rel = posixpath.relpath(asset_cache[absolute], posixpath.dirname(current_page["path"]) or ".")
            tag[attr] = rel
            continue

        tag[attr] = absolute if raw.startswith("/") else raw

    return md(str(soup), heading_style="ATX").replace("\r\n", "\n").strip() + "\n", assets_downloaded, assets_skipped


def export_pages(session, manifest_by_id):
    asset_cache = {}
    total = len(manifest_by_id)
    exported = 0
    skipped_pages = 0
    total_assets_downloaded = 0
    total_assets_skipped = 0

    print(f"Exporting {total} pages...\n")

    for i, (page_id, meta) in enumerate(manifest_by_id.items(), start=1):
        print(f"[{i}/{total}] {meta['title']} (id={page_id})")
        page_api = f"{API_CONTENT}/{page_id}"
        params = {"expand": "body.view,title,ancestors"}
        try:
            response = session.get(page_api, params=params, timeout=120)
            response.raise_for_status()
        except requests.exceptions.RequestException as exc:
            print(f"  [WARN] Skipping page {page_id} ({meta['title']!r}): {exc}")
            skipped_pages += 1
            continue

        payload = response.json()
        html = payload.get("body", {}).get("view", {}).get("value", "")
        title = payload.get("title", meta["title"])

        document, assets_dl, assets_sk = rewrite_page_and_assets(
            session, html, meta, manifest_by_id, None, asset_cache
        )
        total_assets_downloaded += assets_dl
        total_assets_skipped += assets_sk

        target_path = os.path.join(DOCS_DIR, meta["path"])
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            if document.lstrip().startswith(f"# {title}"):
                f.write(document.split("\n", 1)[1].lstrip())
            else:
                f.write(document)

        exported += 1
        status_parts = [f"  Saved → {meta['path']}"]
        if assets_dl:
            status_parts.append(f"{assets_dl} asset(s) downloaded")
        if assets_sk:
            status_parts.append(f"{assets_sk} asset(s) skipped")
        print("  |  ".join(status_parts))

    print(f"""
Export complete
  Pages  : {exported} exported, {skipped_pages} skipped
  Assets : {total_assets_downloaded} downloaded, {total_assets_skipped} skipped
""")


def write_index(manifest_by_id):
    root_titles = sorted({meta["ancestors"][0] for meta in manifest_by_id.values() if meta["ancestors"]})
    lines = [
        "# ONOS Wiki",
        "",
        "This site is a static Markdown export of the public ONOS Confluence wiki.",
        "",
        "## Top-level sections",
        "",
    ]
    for title in root_titles:
        lines.append(f"- {title}")
    if not root_titles:
        lines.append("- Exported pages")
    lines += [
        "",
        "Use the left sidebar to browse the exported hierarchy.",
        "",
    ]
    with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    reset_output()
    session = make_session()
    pages = fetch_all_pages(session)
    manifest_by_id, title_to_ids = build_manifest(pages)
    write_json(os.path.join(CACHE_DIR, "manifest.json"), {"pages": list(manifest_by_id.values())})
    export_pages(session, manifest_by_id)
    write_index(manifest_by_id)
    print(f"Output written to {DOCS_DIR}/")


if __name__ == "__main__":
    main()