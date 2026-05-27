# ONOS Wiki → GitHub Pages (Production-Ready)

This repository exports the public ONOS Confluence wiki to a static Markdown site suitable for GitHub Pages using MkDocs Material.

## What this repository does

- Exports the full ONOS Confluence space using the Confluence REST API
- Preserves page wording by converting the rendered HTML body to Markdown
- Preserves internal links by rewriting them to local Markdown paths
- Downloads images and attachments to `docs/assets/`
- Rebuilds the exact sidebar hierarchy from the page ancestor tree
- Generates `mkdocs.yml` automatically from the real page tree

## Repository layout

```text
onos-classic-wiki/
├── docs/
│   ├── index.md
│   └── assets/
├── scripts/
│   ├── export_onos_wiki.py
│   └── generate_mkdocs.py
├── .github/workflows/deploy.yml
├── mkdocs.template.yml
├── requirements.txt
└── README.md
```

## Export from wiki.onosproject.org

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 scripts/export_onos_wiki.py
```
## Access locally from wiki.onosproject.org
```bash
python3 -m venv .venv #u nless done before
source .venv/bin/activate # unless done before
python3 scripts/generate_mkdocs.py
mkdocs serve -a localhost:8005
```

Go to http://localhost:8005/onos-classic-wiki/ from your browser

## Publish with GitHub Pages

The website is also published at: via Github Pages every time there is a change in the /docs or mkdocs.yaml files. 
Every time you want to make a change please do ensure you generate the `mkdocs.yml` file as above.
The included workflow will build and publish the site automatically.

## Notes

- This repository contains the export pipeline. The Markdown content is generated when you run the scripts.
- Output is written to `docs/` and `site/` is produced by MkDocs during build.
