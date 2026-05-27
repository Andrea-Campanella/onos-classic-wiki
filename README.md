# onos-classic-wiki
Repository containing the content of the ONOS wiki previously hosted on wiki.onosproject.org.

The content refers to https://github.com/opennetworkinglab/onos

## ONOS Wiki → GitHub Pages

This /scripts folder contains scripts to export the public ONOS Confluence wiki to a static Markdown site suitable for GitHub Pages using MkDocs Material. Output is written to `docs/` and `site/` is produced by MkDocs during build.

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

## What does export_onos_wiki.py

- Exports the full ONOS Confluence space using the Confluence REST API
- Preserves page wording by converting the rendered HTML body to Markdown
- Preserves internal links by rewriting them to local Markdown paths
- Downloads images and attachments to `docs/assets/`

## What does generate_mkdocs.py

- Rebuilds the exact sidebar hierarchy from the page ancestor tree
- Generates `mkdocs.yml` automatically from the real page tree

## Export from wiki.onosproject.org

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 scripts/export_onos_wiki.py
```

## Serve website locally and test
```bash
python3 -m venv .venv #u nless done before
source .venv/bin/activate # unless done before
python3 scripts/generate_mkdocs.py
mkdocs serve -a localhost:8005
```

Go to http://localhost:8005/onos-classic-wiki/ from your browser

## Publish with GitHub Pages

The website is also published at https://andrea-campanella.github.io/onos-classic-wiki/ via Github Pages every time there is a change in the `/docs` or `mkdocs.yaml` files. 
Every time you want to make a change please do ensure you generate the `mkdocs.yml` file as above.
The included workflow will build and publish the site automatically.

## Contribute

To contribute follow the steps below after you checked out the repo:
- Create a new branch: `git checkout -b <branch-name>`
- Make Changes
- Add all changes `git add --all`
- Commit all changes `git commit -m "<message>"`
- Push `git push origin <branch-name>`
- Open Pull request on the github UI.

