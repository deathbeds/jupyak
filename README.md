# jupyak

> get a JupyterLite preview of pull requests across the Jupyter stack

## what does it do?

This repo accepts [pull requests](#how-does-it-work) that build static [preview sites](#how-do-i-get-a-preview-site) to the [Jupyter(Lite) stack](#what-can-it-build).

## how do I get a preview site?

- Use the _Request Preview Site_ form to propose a `jupyak_config.json` file to this repo
  - or manually fork, clone, and build one
    - the `.toml`, `.yaml`, and `.yml`) extensions are also discovered
- Make a [pull request][pulls] to this repo
- Wait for the PR to build a site on ReadTheDocs
- Make changes to the _PR_ to trigger re-building the preview site

## where does it do it?

- `https://github.com/deathbeds/jupyak`
    - a GitHub repo where the source code for this package, and all Issues, Pull Requests, and source code are stored
- `https://deathbeds.github.io/jupyak`
    - a GitHub Pages site, rebuilt nightly, which provides a form for building site requests
- `https://jupyak.rtfd.io`
    - a ReadTheDocs site for more information about how this all works
- `https://jupyak--{:pr-number}.org.readthedocs.build/en/{:pr-number}`
    - ReadTheDocs sites generated for each Pull Request
      - this will either be a
        - PR-based [preview site](#how-do-i-get-a-preview-site)
        - preview of the docs for the site itself

## how does it work?

Delivering a preview site uses a few different GitHub Actions workflows and ReadTheDocs.

- A nightly Github Actions job builds `https://deathbeds.github.io/jupyak`
  - This site includes an HTML form of available PRs, tags, etc. for supported
    [repos](#what-can-it-build).
  - Clicking the _submit_ button will open a "new file" GitHub page against this repo
  - Click _Commit Changes..._
  - Follow the Pull Request template and submit
- ReadTheDocs will check out the PR and build a preview JupyterLite site on a custom
    domain
  - If the preview site **fails** to build, the built RTD site will contain
    human-readable error logs
- Additional commits on the PR can trigger a rebuild of the site

## what can it build?

`jupyak` understand how to work with one or more human-readable HTML URLs of the forms:

  - `{:repo}/pull/{:pull-id}`
  - `{:repo}/tree/{:branch}`
  - `{:repo}/releases/tag/{:tag}`
    - > note that the `/tree/{:tag}` form will fail loudly

...from the following repos:

  - https://github.com/ipython/traitlets
  - https://github.com/ipython/comm
  - https://github.com/ipython/ipython
  - https://github.com/jupyter-widgets/ipywidgets
  - https://github.com/jupyter/jupyter_core
  - https://github.com/jupyter/jupyter_server
  - https://github.com/jupyter/notebook
  - https://github.com/jupyterlab/jupyterlab
  - https://github.com/jupyterlab/jupyterlab_server
  - https://github.com/jupyterlab/lumino
  - https://github.com/jupyterlite/jupyterlite
  - https://github.com/jupyterlite/pyodide-kernel

[issues]: https://github.com/deathbeds/jupyak/issues
[pulls]: https://github.com/deathbeds/jupyak/pulls
