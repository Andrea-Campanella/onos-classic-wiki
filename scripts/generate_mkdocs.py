import json
import os
import yaml

DOCS_DIR = "docs"
MANIFEST_PATH = os.path.join(DOCS_DIR, ".cache", "manifest.json")
TEMPLATE_PATH = "mkdocs.template.yml"
OUTPUT_PATH = "mkdocs.yml"

# Desired order for top-level nav sections.
# Sections not listed here will be appended alphabetically at the end.
TOP_LEVEL_ORDER = [
    "Downloads",
    "Guides",
    "Tutorials",
    "Community Information",
    "Release Model",
    "System Test Plans and Results",
    "Apps and Use Cases",
    "New Projects",
    "FAQ",
    "Useful Links",
    "How-to articles",
]


def load_manifest():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        payload = json.load(f)
    return payload.get("pages", [])


def insert_path(tree, ancestors, title, path):
    node = tree
    for ancestor in ancestors:
        if not isinstance(node, dict):
            return
        existing = node.get(ancestor)
        if isinstance(existing, str):
            node[ancestor] = {"index": existing}
        elif not isinstance(existing, dict):
            node[ancestor] = {}
        node = node[ancestor]

    if not isinstance(node, dict):
        return

    if isinstance(node.get(title), dict):
        node[title]["index"] = path
    else:
        node[title] = path


def to_mkdocs_nav(node, top_level=False):
    """
    Recursively convert the tree dict to MkDocs nav format.
    At the top level, keys are sorted according to TOP_LEVEL_ORDER;
    unknown keys are appended alphabetically at the end.
    Nested levels are always sorted alphabetically.
    """
    if top_level:
        order_index = {name: i for i, name in enumerate(TOP_LEVEL_ORDER)}
        sorted_keys = sorted(
            node.keys(),
            key=lambda s: (order_index.get(s, len(TOP_LEVEL_ORDER)), s.lower()),
        )
    else:
        sorted_keys = sorted(node.keys(), key=lambda s: s.lower())

    items = []
    for key in sorted_keys:
        value = node[key]
        if isinstance(value, dict):
            items.append({key: to_mkdocs_nav(value, top_level=False)})
        else:
            items.append({key: value.replace("\\", "/")})
    return items


def load_template():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def ensure_navigation_collapsed(config):
    """
    Make sure the Material theme is configured to show sections collapsed
    by default (no navigation.expand). Adds navigation.sections so that
    top-level items render as expandable groups in the sidebar.
    """
    theme = config.get("theme", {})
    if not isinstance(theme, dict):
        return config

    features = theme.get("features", [])
    # Enable section grouping in the sidebar
    if "navigation.sections" not in features:
        features.append("navigation.sections")
    # Remove expand-all if present — sections should be collapsed by default
    features = [f for f in features if f != "navigation.expand"]

    theme["features"] = features
    config["theme"] = theme
    return config


def main():
    pages = load_manifest()
    tree = {}
    for page in pages:
        insert_path(tree, page.get("ancestors", []), page["title"], page["path"])

    config = load_template()
    config["nav"] = [{"Home": "index.md"}] + to_mkdocs_nav(tree, top_level=True)
    config = ensure_navigation_collapsed(config)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        yaml.safe_dump(config, f, sort_keys=False, allow_unicode=True)

    print(f"Generated {OUTPUT_PATH}")


if __name__ == "__main__":
    main()