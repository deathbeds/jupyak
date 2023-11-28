# jupyak

> Bot-assisted previews of (multiple) PRs to the Jupyter(Lite) stack.

## What does it do?

This repo accepts [issues](#how-does-it-work) to build static [preview sites](#how-do-i-get-a-preview-site)
of Pull Requests to the [Jupyter(Lite) stack](#what-can-it-build).

## Where does it do it?

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

## How do I get a preview site?

- Make an [issue][issues], filling out the form
- Wait for the bot to make a PR
- Wait for the PR to build a site on ReadTheDocs

## How does it work?

Delivering a preview site uses a few different GitHub Actions workflows and ReadTheDocs.

- A nightly Github Actions job builds `https://deathbeds.github.io/jupyak`
  - This site includes an accessible HTML form of available PRs, tags, etc. for all
    supported repos
  - Filling out this form redirects to a new [issue][issues], requiring a GitHub login
- The issue is parsed by a lightweight JS-based workflow
  - It creates a PR with a checked-in file describing the order
    - If this **fails**, the bot should respond to the original issue with help
- ReadTheDocs checks out the PR and builds a preview JupyterLite site on a custom
    domain
  - If this **fails**, the site will contain human-readable error logs
- Additional bot commands on the PR (or original issue)
  can trigger a rebuild of the site, preserving a copy of last-known-good build


## What can it build?

The bots understand how to work with one or more human-readable HTML URLs of the forms:

  - `{:repo}/pull/{:pull-id}`
  - `{:repo}/tree/{:branch-or-commit}`
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
