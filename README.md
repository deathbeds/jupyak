# jupyak

> get a statically-hosted JupyterLite preview of pull requests from across the Jupyter
> stack

## what does it do?

This repo accepts [pull requests](#how-does-it-work) that build static
[preview sites](#how-do-i-get-a-preview-site) to the
[Jupyter(Lite) stack](#what-can-it-build).

## how do I get a preview site?

- Make a `jupyak_config.toml`
  - ... with the _Request Preview Site_ [form]
  - ... or by manually [forking][fork] and creating a new branch from your fork
- Start a [Pull Request][pulls] (PR) including the `jupyak_config.toml`
- Wait for the PR to build a site on ReadTheDocs (RTD)
- Make changes to the PR to trigger re-building the preview site

## where does it do it?

- `https://github.com/deathbeds/jupyak`
  - a GitHub repo where the source code for this package, and all Issues, Pull Requests,
    and source code are stored
- `https://deathbeds.github.io/jupyak`
  - a GitHub Pages site, rebuilt nightly, which provides a form for building preview
    site requests
- `https://jupyak--{:pr-number}.org.readthedocs.build/en/{:pr-number}`
  - ReadTheDocs sites generated for each Pull Request
    - this will either be a
      - PR-based [preview site](#how-do-i-get-a-preview-site)
      - preview of the docs for the site itself
- `https://jupyak.rtfd.io`
  - a ReadTheDocs site for more information about how this all works

> The above works on at least _one_ Ubuntu 22.03 LTS machine, but little care has been
> taken to make _anything_ run on any other system, and likely won't be tested anywhere
> else.

## how does it work?

Delivering a preview site uses a few different GitHub Actions workflows and ReadTheDocs
configurations. Once a PR is created:

- A GitHub Actions (GHA) job will create a link to the custom domain site
  - This will initially return `404`, as the site isn't built yet
  - Clicking instead on the ReadTheDocs check at the bottom of the Pull Request will
    show build logs, but these are _intentionally_ sparse, capturing most output as logs
    to present in the built site.
- RTD will check out the PR and build a preview JupyterLite site on a custom domain
  - If the preview site **fails** to build (or even check out due to conflicts), the
    built RTD site will contain human-readable error logs
- Additional commits on the PR can trigger a rebuild of the site

## what can it build?

`jupyak` understand how to work with one or more fragments of human-readable GitHub URLs
of the forms:

- `/pull/{:pull-id}`
- `/tree/{:branch}`
- `/releases/tag/{:tag}`
  - > note that the `/tree/{:tag}` form will fail loudly

...from the following repos to see novel behavior.

| repo                                          | browser UI | kernel |
| --------------------------------------------- | :--------: | :----: |
| https://github.com/ipython/comm               |            |   ✅   |
| https://github.com/ipython/ipython            |            |   ✅   |
| https://github.com/ipython/traitlets          |            |   ✅   |
| https://github.com/jupyter-widgets/ipywidgets |     ✅     |   ✅   |
| https://github.com/jupyter/jupyter_core       |            |   ✅   |
| https://github.com/jupyter/nbformat           |            |   ✅   |
| https://github.com/jupyter/notebook           |     ✅     |        |
| https://github.com/jupyterlab/jupyterlab      |     ✅     |        |
| https://github.com/jupyterlab/lumino          |     ✅     |        |
| https://github.com/jupyterlite/jupyterlite    |     ✅     |        |
| https://github.com/jupyterlite/pyodide-kernel |     ✅     |   ✅   |

Additionally, a single GitHub [Gist][gist] can be used as the contents of the preview
site. If the gist contains `jupyter_lite_config.json` and/or `jupyter-lite.json`, these
will be merged into the [configuration][lite-config] used to build and host the site.

## what does it _not_ build?

The following repos are cloned and installed to satisfy build-time requirements, but
have little measurable experience the UI.

| repo                                                       | why not?                       |
| ---------------------------------------------------------- | ------------------------------ |
| https://github.com/ipython/ipykernel                       | heavy deps, patched in pyodide |
| https://github.com/jupyter-lsp/jupyterlab-lsp              | needs mock JS server           |
| https://github.com/jupyter-server/jupyter_server           | heavy deps                     |
| https://github.com/jupyter-server/jupyter_server_terminals | what's a process?              |
| https://github.com/jupyterlab/jupyterlab_server            | heavy deps                     |
| https://github.com/jupyter/nbconvert                       | heavy deps, no `data_files`    |

For each repo, a few more things _could_ be built, and might be interesting to evaluate
a PR stack. However, each of these would come at the expense of a lower chance of a
usable JupyterLite site at the end of each PR build. These include:

- test reports
- examples
- documentation
- lint reports
- anything that doesn't work in the browser
- anything that requires a `c`/`rust`/`emscripten` compiler or other heavy dependencies
  such as `pandas`

[issues]: https://github.com/deathbeds/jupyak/issues
[pulls]: https://github.com/deathbeds/jupyak/pulls
[form]: https://deathbeds.github.io/jupyak/new.html
[fork]: https://github.com/deathbeds/jupyak/fork
[gist]: https://gist.github.com/
[pages-badge]:
  https://github.com/deathbeds/jupyak/actions/workflows/pages.yml/badge.svg?branch=main
[pages-status]: https://github.com/deathbeds/jupyak/actions/workflows/pages.yml
[lite-config]:
  https://jupyterlite.readthedocs.io/en/latest/howto/configure/config_files.html
