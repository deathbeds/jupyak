"""documentation for ``jupyak``."""
import datetime
import json
import os
import re
from pathlib import Path

import tomli

CONF_PY = Path(__file__)
HERE = CONF_PY.parent
ROOT = HERE.parent
PYPROJ = ROOT / "pyproject.toml"
PROJ_DATA = tomli.loads(PYPROJ.read_text(encoding="utf-8"))
RE_GH = (
    r"https://github.com"
    r"/(?P<github_user>.*?)"
    r"/(?P<github_repo>.*?)"
    r"/tree/(?P<github_version>.*)"
)
REPO_INFO = re.search(RE_GH, PROJ_DATA["project"]["urls"]["Source"])
NOW = datetime.datetime.now(tz=datetime.timezone.utc).date()
WORK_DIST = HERE / "_static/work"
JUPYAK_CONF_CANDIDATES = [
    ROOT / f"jupyak_config.{ext}"
    for ext in ["toml", "yaml", "yml", "json"]
    if (ROOT / f"jupyak_config.{ext}").exists()
]
ALLOW_NO_CONFIG = json.loads(os.environ.get("JUPYAK_ALLOW_NO_CONFIG", "0").lower())

# metadata
author = PROJ_DATA["project"]["authors"][0]["name"]
project = PROJ_DATA["project"]["name"]
copyright = f"{NOW.year}, {author}"


# The full version, including alpha/beta/rc tags
release = PROJ_DATA["project"]["version"]

# The short X.Y version
version = ".".join(release.rsplit(".", 1))

# sphinx config
extensions = [
    "sphinx.ext.viewcode",
    "myst_nb",
    "sphinx.ext.autosectionlabel",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
    "sphinxext.rediraffe",
]

# content
autosectionlabel_prefix_document = True
myst_heading_anchors = 3

mermaid_version = ""
mermaid_init_js = "false"


# warnings
suppress_warnings = ["autosectionlabel.*"]

# theme
templates_path = ["_templates"]
html_static_path = ["_static"]
html_theme = "pydata_sphinx_theme"
html_logo = "_static/img/logo.svg"
html_favicon = "_static/img/logo.svg"
html_css_files = ["css/theme.css"]

html_theme_options = {
    "github_url": PROJ_DATA["project"]["urls"]["Source"],
    "use_edit_page_button": REPO_INFO is not None,
    "logo": {"text": PROJ_DATA["project"]["name"]},
    "navigation_with_keys": False,
    "icon_links": [
        {
            "name": "PyPI",
            "url": PROJ_DATA["project"]["urls"]["PyPI"],
            "icon": "fa-brands fa-python",
        },
        {
            "name": "conda-forge",
            "url": "https://github.com/conda-forge/jupyak",
            "icon": "_static/img/anvil.svg",
            "type": "local",
        },
    ],
    "footer_end": ["mermaid10"],
    "secondary_sidebar_items": [],
}


html_context = {}
rediraffe_redirects = {}
html_sidebars = {
    "*": ["page-toc", "edit-this-page", "sourcelink"],
    "graph": [],
}

if REPO_INFO is not None:
    html_context = {**REPO_INFO.groupdict(), "doc_path": "docs"}

if ALLOW_NO_CONFIG or JUPYAK_CONF_CANDIDATES:
    html_sidebars["*"] = [
        "demo",
        *html_sidebars["*"],
    ]
    if WORK_DIST.exists():
        html_context["lite_links"] = {
            "lab": {"label": "Lab", "icon": "fas fa-flask"},
            "repl": {"label": "Console", "icon": "fas fa-terminal"},
            "tree": {"label": "File Tree", "icon": "fas fa-folder-tree"},
        }

        rediraffe_redirects = {
            f"preview/{frag}/index": f"_static/work/lite/{frag}/index"
            for frag in html_context["lite_links"]
        }
