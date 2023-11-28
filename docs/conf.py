"""documentation for ``jupyak``."""
import datetime
import os
import re
from pathlib import Path

import importnb
import tomli

with importnb.Notebook():
    from jupyak.tasks._yak import Yak

os.environ.update(JPYK_ALLOW_NO_CONFIG="1")

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
YAK = Yak()

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
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "myst_nb",
    "sphinx.ext.autosectionlabel",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.mermaid",
]

# content
autosectionlabel_prefix_document = True
myst_heading_anchors = 3

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

mermaid_version = ""
mermaid_init_js = "false"

# warnings
suppress_warnings = ["autosectionlabel.*"]

# theme
templates_path = ["_templates"]
html_static_path = [
    "_static",
    *([str(YAK.dist_path)] if YAK.dist_path.exists() else []),
]
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
}

if REPO_INFO is not None:
    html_context = {**REPO_INFO.groupdict(), "doc_path": "docs"}
