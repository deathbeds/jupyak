---
html_theme.sidebar_secondary.remove: true
---

# task graph


The graph below shows the current state of the executed graph of tasks to go from
<code>git clone</code> to <code>jupyter lite build</code>.

<blockquote>
Some tasks, such as extracting <code>conda</code> dependencies from <code>pyproject.toml</code>
files, have been elided to highlight the relationships between repositories.
</blockquote>


<div class="jp-Mermaid" id="task-graph-legend">

<div class="mermaid">
graph TB
%%{init: {"flowchart": {"defaultRenderer": "elk"}} }%%
classDef py fill:#4b8bbe,color:#ffe873;
classDef jupyter fill:#f37626,color:#ffe873;
classDef js fill:#f0db4f,color:#000;
classDef git fill:#f1502f,color:#fff;
classDef hack fill:#000,color:#fff;
subgraph task types
py[py]:::py
jupyter([jupyter]):::jupyter
js{{js}}:::js
git[(git)]:::git
hack((hack)):::hack
end
subgraph task status
up-to-date["✅ up-to-date"]
run["💭 run"]
error["❌ error"]
end
</div>
</div>

<div class="jp-Mermaid" id="task-graph">
<label>Zoom: </label>
<input type="radio" id="task-graph-svg-zoom-1" name="task-graph-svg-zoom" checked><label for="svg-zoom-1"> 1x</label>
<input type="radio" id="task-graph-svg-zoom-2" name="task-graph-svg-zoom" ><label for="svg-zoom-2"> 2x</label>
<input type="radio" id="task-graph-svg-zoom-4" name="task-graph-svg-zoom" ><label for="svg-zoom-4"> 4x</label>
<input type="radio" id="task-graph-svg-zoom-8" name="task-graph-svg-zoom" ><label for="svg-zoom-8"> 8x</label>
<div class="mermaid">
graph LR
%%{init: {"flowchart": {"defaultRenderer": "elk"}} }%%
classDef py fill:#4b8bbe,color:#ffe873;
classDef jupyter fill:#f37626,color:#ffe873;
classDef js fill:#f0db4f,color:#000;
classDef git fill:#f1502f,color:#fff;
classDef hack fill:#000,color:#fff;
shave:js:jupyterlab:yarn:build:prod:dev_mode --> jupyterlab:sweep:assets
shave:js:jupyterlab:yarn:builder:. --> jupyterlab:sweep:labextension
shave:git:lite:gist:init --> shave:git:lite:gist:fetch:main
shave:git:lite:gist:fetch:main --> shave:git:lite:gist:checkout
shave:git:traitlets:init --> shave:git:traitlets:fetch:main
shave:git:traitlets:fetch:main --> shave:git:traitlets:checkout
shave:git:comm:init --> shave:git:comm:fetch:main
shave:git:comm:fetch:main --> shave:git:comm:checkout
shave:git:lumino:init --> shave:git:lumino:fetch:main
shave:git:lumino:init --> shave:git:lumino:fetch:pr-655
shave:git:lumino:fetch:main --> shave:git:lumino:checkout
shave:git:lumino:fetch:pr-655 --> shave:git:lumino:checkout
shave:git:jupyter_server_terminals:init --> shave:git:jupyter_server_terminals:fetch:main
shave:git:jupyter_server_terminals:fetch:main --> shave:git:jupyter_server_terminals:checkout
shave:git:jupyter_core:init --> shave:git:jupyter_core:fetch:main
shave:git:jupyter_core:fetch:main --> shave:git:jupyter_core:checkout
shave:git:jupyter_events:init --> shave:git:jupyter_events:fetch:main
shave:git:jupyter_events:fetch:main --> shave:git:jupyter_events:checkout
shave:git:ipython:init --> shave:git:ipython:fetch:main
shave:git:ipython:fetch:main --> shave:git:ipython:checkout
shave:git:jupyter_client:init --> shave:git:jupyter_client:fetch:main
shave:git:jupyter_client:fetch:main --> shave:git:jupyter_client:checkout
shave:git:nbformat:init --> shave:git:nbformat:fetch:main
shave:git:nbformat:fetch:main --> shave:git:nbformat:checkout
shave:git:nbconvert:init --> shave:git:nbconvert:fetch:main
shave:git:nbconvert:fetch:main --> shave:git:nbconvert:checkout
shave:git:ipykernel:init --> shave:git:ipykernel:fetch:main
shave:git:ipykernel:fetch:main --> shave:git:ipykernel:checkout
shave:git:nbclient:init --> shave:git:nbclient:fetch:main
shave:git:nbclient:fetch:main --> shave:git:nbclient:checkout
shave:git:jupyter_server:init --> shave:git:jupyter_server:fetch:main
shave:git:jupyter_server:fetch:main --> shave:git:jupyter_server:checkout
shave:git:notebook_shim:init --> shave:git:notebook_shim:fetch:main
shave:git:notebook_shim:fetch:main --> shave:git:notebook_shim:checkout
shave:git:jupyterlab_server:init --> shave:git:jupyterlab_server:fetch:main
shave:git:jupyterlab_server:fetch:main --> shave:git:jupyterlab_server:checkout
shave:git:jupyterlab:init --> shave:git:jupyterlab:fetch:main
shave:git:jupyterlab:init --> shave:git:jupyterlab:fetch:pr-15443
shave:git:jupyterlab:init --> shave:git:jupyterlab:fetch:pr-15347
shave:git:jupyterlab:fetch:main --> shave:git:jupyterlab:checkout
shave:git:jupyterlab:fetch:pr-15443 --> shave:git:jupyterlab:checkout
shave:git:jupyterlab:fetch:pr-15347 --> shave:git:jupyterlab:checkout
shave:git:notebook:init --> shave:git:notebook:fetch:main
shave:git:notebook:fetch:main --> shave:git:notebook:checkout
shave:git:ipywidgets:init --> shave:git:ipywidgets:fetch:main
shave:git:ipywidgets:init --> shave:git:ipywidgets:fetch:pr-3847
shave:git:ipywidgets:fetch:main --> shave:git:ipywidgets:checkout
shave:git:ipywidgets:fetch:pr-3847 --> shave:git:ipywidgets:checkout
shave:git:jupyterlite:init --> shave:git:jupyterlite:fetch:main
shave:git:jupyterlite:fetch:main --> shave:git:jupyterlite:checkout
shave:git:jupyterlite_pyodide_kernel:init --> shave:git:jupyterlite_pyodide_kernel:fetch:main
shave:git:jupyterlite_pyodide_kernel:fetch:main --> shave:git:jupyterlite_pyodide_kernel:checkout
shave:git:lumino:checkout --> shave:js:lumino:yarn:install
shave:js:yarnrc --> shave:js:lumino:yarn:install
shave:js:lumino:yarn:install --> shave:js:lumino:yarn:build:.
shave:git:lumino:checkout --> shave:js:lumino:dist
shave:git:jupyterlab:checkout --> shave:js:jupyterlab:yarn:install
shave:js:yarnrc --> shave:js:jupyterlab:yarn:install
shave:js:lumino:dist --> shave:js:jupyterlab:yarn:install
shave:js:jupyterlab:yarn:install --> shave:js:jupyterlab:yarn:buildutils:.
shave:js:jupyterlab:yarn:install --> shave:js:jupyterlab:yarn:builder:.
shave:js:jupyterlab:yarn:install --> shave:js:jupyterlab:yarn:build:metapackage
shave:js:jupyterlab:yarn:install --> shave:js:jupyterlab:yarn:build:prod:dev_mode
shave:js:jupyterlab:yarn:buildutils:. --> shave:js:jupyterlab:yarn:build:prod:dev_mode
shave:js:jupyterlab:yarn:builder:. --> shave:js:jupyterlab:yarn:build:prod:dev_mode
shave:js:jupyterlab:yarn:build:metapackage --> shave:js:jupyterlab:yarn:build:prod:dev_mode
shave:git:jupyterlab:checkout --> shave:js:jupyterlab:dist
shave:js:jupyterlab:yarn:buildutils:. --> shave:js:jupyterlab:dist
shave:js:jupyterlab:yarn:builder:. --> shave:js:jupyterlab:dist
shave:js:jupyterlab:yarn:build:metapackage --> shave:js:jupyterlab:dist
shave:js:jupyterlab:yarn:build:prod:dev_mode --> shave:js:jupyterlab:dist
shave:git:notebook:checkout --> shave:js:notebook:yarn:install
shave:js:yarnrc --> shave:js:notebook:yarn:install
shave:js:lumino:dist --> shave:js:notebook:yarn:install
shave:js:jupyterlab:dist --> shave:js:notebook:yarn:install
shave:js:notebook:yarn:install --> shave:js:notebook:yarn:meta:build:_metapackage
shave:js:notebook:yarn:install --> shave:js:notebook:yarn:app:build:prod:app
shave:js:notebook:yarn:meta:build:_metapackage --> shave:js:notebook:yarn:app:build:prod:app
shave:git:notebook:checkout --> shave:js:notebook:dist
shave:js:notebook:yarn:meta:build:_metapackage --> shave:js:notebook:dist
shave:js:notebook:yarn:app:build:prod:app --> shave:js:notebook:dist
shave:git:ipywidgets:checkout --> shave:js:ipywidgets:yarn:install
shave:js:yarnrc --> shave:js:ipywidgets:yarn:install
shave:js:lumino:dist --> shave:js:ipywidgets:yarn:install
shave:js:jupyterlab:dist --> shave:js:ipywidgets:yarn:install
shave:js:ipywidgets:yarn:install --> shave:js:ipywidgets:yarn:build:base
shave:js:ipywidgets:yarn:install --> shave:js:ipywidgets:yarn:build:controls
shave:js:ipywidgets:yarn:build:base --> shave:js:ipywidgets:yarn:build:controls
shave:js:ipywidgets:yarn:install --> shave:js:ipywidgets:yarn:build:base-manager
shave:js:ipywidgets:yarn:build:controls --> shave:js:ipywidgets:yarn:build:base-manager
shave:js:ipywidgets:yarn:install --> shave:js:ipywidgets:yarn:build:html-manager
shave:js:ipywidgets:yarn:build:base-manager --> shave:js:ipywidgets:yarn:build:html-manager
shave:js:ipywidgets:yarn:install --> shave:js:ipywidgets:yarn:build:output
shave:js:ipywidgets:yarn:build:html-manager --> shave:js:ipywidgets:yarn:build:output
shave:js:ipywidgets:yarn:install --> shave:js:ipywidgets:yarn:build:jupyterlab_widgets
shave:js:ipywidgets:yarn:build:base --> shave:js:ipywidgets:yarn:build:jupyterlab_widgets
shave:js:ipywidgets:yarn:build:controls --> shave:js:ipywidgets:yarn:build:jupyterlab_widgets
shave:js:ipywidgets:yarn:build:base-manager --> shave:js:ipywidgets:yarn:build:jupyterlab_widgets
shave:js:ipywidgets:yarn:build:html-manager --> shave:js:ipywidgets:yarn:build:jupyterlab_widgets
shave:js:ipywidgets:yarn:build:output --> shave:js:ipywidgets:yarn:build:jupyterlab_widgets
shave:git:ipywidgets:checkout --> shave:js:ipywidgets:dist
shave:js:ipywidgets:yarn:build:base --> shave:js:ipywidgets:dist
shave:js:ipywidgets:yarn:build:controls --> shave:js:ipywidgets:dist
shave:js:ipywidgets:yarn:build:base-manager --> shave:js:ipywidgets:dist
shave:js:ipywidgets:yarn:build:html-manager --> shave:js:ipywidgets:dist
shave:js:ipywidgets:yarn:build:output --> shave:js:ipywidgets:dist
shave:js:ipywidgets:yarn:build:jupyterlab_widgets --> shave:js:ipywidgets:dist
shave:git:jupyterlite:checkout --> shave:js:jupyterlite:yarn:install
shave:js:yarnrc --> shave:js:jupyterlite:yarn:install
shave:js:lumino:dist --> shave:js:jupyterlite:yarn:install
shave:js:jupyterlab:dist --> shave:js:jupyterlite:yarn:install
shave:js:notebook:dist --> shave:js:jupyterlite:yarn:install
shave:js:jupyterlite:yarn:install --> shave:js:jupyterlite:yarn:build:.
shave:git:jupyterlite:checkout --> shave:js:jupyterlite:dist
shave:js:jupyterlite:yarn:build:. --> shave:js:jupyterlite:dist
shave:git:jupyterlite_pyodide_kernel:checkout --> shave:js:jupyterlite_pyodide_kernel:yarn:install
shave:js:yarnrc --> shave:js:jupyterlite_pyodide_kernel:yarn:install
shave:js:lumino:dist --> shave:js:jupyterlite_pyodide_kernel:yarn:install
shave:js:jupyterlab:dist --> shave:js:jupyterlite_pyodide_kernel:yarn:install
shave:js:jupyterlite:dist --> shave:js:jupyterlite_pyodide_kernel:yarn:install
shave:js:jupyterlite_pyodide_kernel:yarn:install --> shave:js:jupyterlite_pyodide_kernel:yarn:build:py:wheels:pyodide-kernel
shave:py:jupyterlite:pip:jupyterlite-core --> shave:js:jupyterlite_pyodide_kernel:yarn:build:py:wheels:pyodide-kernel
shave:py:jupyterlite_pyodide_kernel:pip:jupyterlite_pyodide_kernel --> shave:js:jupyterlite_pyodide_kernel:yarn:build:py:wheels:pyodide-kernel
shave:js:jupyterlite_pyodide_kernel:yarn:install --> shave:js:jupyterlite_pyodide_kernel:yarn:build:js:pyodide-kernel
shave:js:jupyterlite_pyodide_kernel:yarn:build:py:wheels:pyodide-kernel --> shave:js:jupyterlite_pyodide_kernel:yarn:build:js:pyodide-kernel
shave:js:jupyterlite_pyodide_kernel:yarn:install --> shave:js:jupyterlite_pyodide_kernel:yarn:build:lib:pyodide-kernel-extension
shave:js:jupyterlite_pyodide_kernel:yarn:build:js:pyodide-kernel --> shave:js:jupyterlite_pyodide_kernel:yarn:build:lib:pyodide-kernel-extension
shave:git:jupyterlite_pyodide_kernel:checkout --> shave:js:jupyterlite_pyodide_kernel:dist
shave:js:jupyterlite_pyodide_kernel:yarn:build:py:wheels:pyodide-kernel --> shave:js:jupyterlite_pyodide_kernel:dist
shave:js:jupyterlite_pyodide_kernel:yarn:build:js:pyodide-kernel --> shave:js:jupyterlite_pyodide_kernel:dist
shave:js:jupyterlite_pyodide_kernel:yarn:build:lib:pyodide-kernel-extension --> shave:js:jupyterlite_pyodide_kernel:dist
shave:git:traitlets:checkout --> shave:py:traitlets:pip:traitlets
shave:git:traitlets:checkout --> shave:py:traitlets:wheel:traitlets
shave:git:comm:checkout --> shave:py:comm:pip:comm
shave:git:comm:checkout --> shave:py:comm:wheel:comm
shave:git:jupyter_server_terminals:checkout --> shave:py:jupyter_server_terminals:pip:jupyter_server_terminals
shave:git:jupyter_core:checkout --> shave:py:jupyter_core:pip:jupyter_core
shave:py:traitlets:pip:traitlets --> shave:py:jupyter_core:pip:jupyter_core
shave:git:jupyter_core:checkout --> shave:py:jupyter_core:wheel:jupyter_core
shave:py:traitlets:pip:traitlets --> shave:py:jupyter_core:wheel:jupyter_core
shave:git:jupyter_events:checkout --> shave:py:jupyter_events:pip:jupyter_events
shave:py:traitlets:pip:traitlets --> shave:py:jupyter_events:pip:jupyter_events
shave:git:ipython:checkout --> shave:py:ipython:pip:ipython
shave:py:traitlets:pip:traitlets --> shave:py:ipython:pip:ipython
shave:git:ipython:checkout --> shave:py:ipython:wheel:ipython
shave:py:traitlets:pip:traitlets --> shave:py:ipython:wheel:ipython
shave:git:jupyter_client:checkout --> shave:py:jupyter_client:pip:jupyter_client
shave:py:jupyter_core:pip:jupyter_core --> shave:py:jupyter_client:pip:jupyter_client
shave:git:nbformat:checkout --> shave:py:nbformat:pip:nbformat
shave:py:traitlets:pip:traitlets --> shave:py:nbformat:pip:nbformat
shave:py:jupyter_core:pip:jupyter_core --> shave:py:nbformat:pip:nbformat
shave:git:nbconvert:checkout --> shave:py:nbconvert:pip:nbconvert
shave:py:jupyter_core:pip:jupyter_core --> shave:py:nbconvert:pip:nbconvert
shave:py:nbformat:pip:nbformat --> shave:py:nbconvert:pip:nbconvert
shave:py:nbclient:pip:nbclient --> shave:py:nbconvert:pip:nbconvert
shave:git:ipykernel:checkout --> shave:py:ipykernel:pip:ipykernel
shave:py:traitlets:pip:traitlets --> shave:py:ipykernel:pip:ipykernel
shave:py:comm:pip:comm --> shave:py:ipykernel:pip:ipykernel
shave:py:jupyter_core:pip:jupyter_core --> shave:py:ipykernel:pip:ipykernel
shave:py:ipython:pip:ipython --> shave:py:ipykernel:pip:ipykernel
shave:py:jupyter_client:pip:jupyter_client --> shave:py:ipykernel:pip:ipykernel
shave:git:nbclient:checkout --> shave:py:nbclient:pip:nbclient
shave:py:traitlets:pip:traitlets --> shave:py:nbclient:pip:nbclient
shave:py:jupyter_core:pip:jupyter_core --> shave:py:nbclient:pip:nbclient
shave:py:jupyter_client:pip:jupyter_client --> shave:py:nbclient:pip:nbclient
shave:py:nbformat:pip:nbformat --> shave:py:nbclient:pip:nbclient
shave:git:jupyter_server:checkout --> shave:py:jupyter_server:pip:jupyter_server
shave:py:traitlets:pip:traitlets --> shave:py:jupyter_server:pip:jupyter_server
shave:py:jupyter_server_terminals:pip:jupyter_server_terminals --> shave:py:jupyter_server:pip:jupyter_server
shave:py:jupyter_core:pip:jupyter_core --> shave:py:jupyter_server:pip:jupyter_server
shave:py:jupyter_events:pip:jupyter_events --> shave:py:jupyter_server:pip:jupyter_server
shave:py:jupyter_client:pip:jupyter_client --> shave:py:jupyter_server:pip:jupyter_server
shave:py:nbconvert:pip:nbconvert --> shave:py:jupyter_server:pip:jupyter_server
shave:git:notebook_shim:checkout --> shave:py:notebook_shim:pip:notebook_shim
shave:py:jupyter_server:pip:jupyter_server --> shave:py:notebook_shim:pip:notebook_shim
shave:git:jupyterlab_server:checkout --> shave:py:jupyterlab_server:pip:jupyterlab_server
shave:py:jupyter_server:pip:jupyter_server --> shave:py:jupyterlab_server:pip:jupyterlab_server
shave:git:jupyterlab:checkout --> shave:py:jupyterlab:pip:jupyterlab
shave:js:jupyterlab:yarn:build:prod:dev_mode --> shave:py:jupyterlab:pip:jupyterlab
shave:py:ipykernel:pip:ipykernel --> shave:py:jupyterlab:pip:jupyterlab
shave:py:notebook_shim:pip:notebook_shim --> shave:py:jupyterlab:pip:jupyterlab
shave:py:jupyterlab_server:pip:jupyterlab_server --> shave:py:jupyterlab:pip:jupyterlab
shave:git:notebook:checkout --> shave:py:notebook:pip:notebook
shave:js:notebook:yarn:app:build:prod:app --> shave:py:notebook:pip:notebook
shave:py:jupyterlab:pip:jupyterlab --> shave:py:notebook:pip:notebook
shave:py:notebook:labext:lab-extension --> shave:py:notebook:pip:notebook
jupyterlab:sweep:labextension --> shave:py:notebook:labext:lab-extension
shave:js:notebook:yarn:meta:build:_metapackage --> shave:py:notebook:labext:lab-extension
shave:py:jupyterlab:pip:jupyterlab --> shave:py:notebook:labext:lab-extension
shave:git:ipywidgets:checkout --> shave:py:ipywidgets:pip:ipywidgets
shave:py:traitlets:pip:traitlets --> shave:py:ipywidgets:pip:ipywidgets
shave:py:comm:pip:comm --> shave:py:ipywidgets:pip:ipywidgets
shave:py:ipython:pip:ipython --> shave:py:ipywidgets:pip:ipywidgets
shave:py:jupyterlab:pip:jupyterlab --> shave:py:ipywidgets:pip:ipywidgets
shave:git:ipywidgets:checkout --> shave:py:ipywidgets:wheel:ipywidgets
shave:py:traitlets:pip:traitlets --> shave:py:ipywidgets:wheel:ipywidgets
shave:py:comm:pip:comm --> shave:py:ipywidgets:wheel:ipywidgets
shave:py:ipython:pip:ipython --> shave:py:ipywidgets:wheel:ipywidgets
shave:py:jupyterlab:pip:jupyterlab --> shave:py:ipywidgets:wheel:ipywidgets
shave:git:ipywidgets:checkout --> shave:py:ipywidgets:pip:jupyterlab_widgets
shave:py:traitlets:pip:traitlets --> shave:py:ipywidgets:pip:jupyterlab_widgets
shave:py:comm:pip:comm --> shave:py:ipywidgets:pip:jupyterlab_widgets
shave:py:ipython:pip:ipython --> shave:py:ipywidgets:pip:jupyterlab_widgets
shave:py:jupyterlab:pip:jupyterlab --> shave:py:ipywidgets:pip:jupyterlab_widgets
shave:git:ipywidgets:checkout --> shave:py:ipywidgets:wheel:jupyterlab_widgets
shave:py:traitlets:pip:traitlets --> shave:py:ipywidgets:wheel:jupyterlab_widgets
shave:py:comm:pip:comm --> shave:py:ipywidgets:wheel:jupyterlab_widgets
shave:py:ipython:pip:ipython --> shave:py:ipywidgets:wheel:jupyterlab_widgets
shave:py:jupyterlab:pip:jupyterlab --> shave:py:ipywidgets:wheel:jupyterlab_widgets
shave:py:ipywidgets:labext:jupyterlab_widgets --> shave:py:ipywidgets:wheel:jupyterlab_widgets
shave:git:ipywidgets:checkout --> shave:py:ipywidgets:pip:widgetsnbextension
shave:py:traitlets:pip:traitlets --> shave:py:ipywidgets:pip:widgetsnbextension
shave:py:comm:pip:comm --> shave:py:ipywidgets:pip:widgetsnbextension
shave:py:ipython:pip:ipython --> shave:py:ipywidgets:pip:widgetsnbextension
shave:py:jupyterlab:pip:jupyterlab --> shave:py:ipywidgets:pip:widgetsnbextension
jupyterlab:sweep:labextension --> shave:py:ipywidgets:labext:jupyterlab_widgets
shave:js:ipywidgets:yarn:build:jupyterlab_widgets --> shave:py:ipywidgets:labext:jupyterlab_widgets
shave:py:jupyterlab:pip:jupyterlab --> shave:py:ipywidgets:labext:jupyterlab_widgets
shave:git:jupyterlite:checkout --> shave:py:jupyterlite:pip:jupyterlite
shave:py:traitlets:pip:traitlets --> shave:py:jupyterlite:pip:jupyterlite
shave:py:jupyter_core:pip:jupyter_core --> shave:py:jupyterlite:pip:jupyterlite
shave:py:jupyter_server:pip:jupyter_server --> shave:py:jupyterlite:pip:jupyterlite
shave:py:jupyterlab:pip:jupyterlab --> shave:py:jupyterlite:pip:jupyterlite
shave:py:notebook:pip:notebook --> shave:py:jupyterlite:pip:jupyterlite
shave:git:jupyterlite:checkout --> shave:py:jupyterlite:pip:jupyterlite-core
shave:py:traitlets:pip:traitlets --> shave:py:jupyterlite:pip:jupyterlite-core
shave:py:jupyter_core:pip:jupyter_core --> shave:py:jupyterlite:pip:jupyterlite-core
shave:py:jupyter_server:pip:jupyter_server --> shave:py:jupyterlite:pip:jupyterlite-core
shave:py:jupyterlab:pip:jupyterlab --> shave:py:jupyterlite:pip:jupyterlite-core
shave:py:notebook:pip:notebook --> shave:py:jupyterlite:pip:jupyterlite-core
shave:git:jupyterlite:checkout --> shave:py:jupyterlite:pip:jupyterlite-javascript-kernel
shave:py:traitlets:pip:traitlets --> shave:py:jupyterlite:pip:jupyterlite-javascript-kernel
shave:py:jupyter_core:pip:jupyter_core --> shave:py:jupyterlite:pip:jupyterlite-javascript-kernel
shave:py:jupyter_server:pip:jupyter_server --> shave:py:jupyterlite:pip:jupyterlite-javascript-kernel
shave:py:jupyterlab:pip:jupyterlab --> shave:py:jupyterlite:pip:jupyterlite-javascript-kernel
shave:py:notebook:pip:notebook --> shave:py:jupyterlite:pip:jupyterlite-javascript-kernel
jupyterlab:sweep:labextension --> shave:py:jupyterlite:labext:jupyterlite-javascript-kernel
shave:js:jupyterlite:yarn:build:. --> shave:py:jupyterlite:labext:jupyterlite-javascript-kernel
shave:py:jupyterlab:pip:jupyterlab --> shave:py:jupyterlite:labext:jupyterlite-javascript-kernel
shave:git:jupyterlite_pyodide_kernel:checkout --> shave:py:jupyterlite_pyodide_kernel:pip:jupyterlite_pyodide_kernel
shave:py:jupyterlab:pip:jupyterlab --> shave:py:jupyterlite_pyodide_kernel:pip:jupyterlite_pyodide_kernel
shave:py:jupyterlite:pip:jupyterlite --> shave:py:jupyterlite_pyodide_kernel:pip:jupyterlite_pyodide_kernel
jupyterlab:sweep:labextension --> shave:py:jupyterlite_pyodide_kernel:labext:pyodide-kernel-extension
shave:js:jupyterlite_pyodide_kernel:yarn:build:py:wheels:pyodide-kernel --> shave:py:jupyterlite_pyodide_kernel:labext:pyodide-kernel-extension
shave:js:jupyterlite_pyodide_kernel:yarn:build:lib:pyodide-kernel-extension --> shave:py:jupyterlite_pyodide_kernel:labext:pyodide-kernel-extension
shave:py:jupyterlab:pip:jupyterlab --> shave:py:jupyterlite_pyodide_kernel:labext:pyodide-kernel-extension
shave:git:lite:gist:checkout --> shave:lite:config
shave:py:traitlets:wheel:traitlets --> shave:lite:config
shave:py:comm:wheel:comm --> shave:lite:config
shave:py:jupyter_core:wheel:jupyter_core --> shave:lite:config
shave:py:ipython:wheel:ipython --> shave:lite:config
shave:py:ipywidgets:wheel:ipywidgets --> shave:lite:config
shave:py:ipywidgets:wheel:jupyterlab_widgets --> shave:lite:config
shave:py:ipywidgets:labext:jupyterlab_widgets --> shave:lite:config
shave:py:jupyterlite:labext:jupyterlite-javascript-kernel --> shave:lite:config
shave:py:jupyterlite_pyodide_kernel:labext:pyodide-kernel-extension --> shave:lite:config
jupyterlab:sweep:assets --> shave:lite:build
shave:git:lite:gist:checkout --> shave:lite:build
shave:py:traitlets:wheel:traitlets --> shave:lite:build
shave:py:comm:wheel:comm --> shave:lite:build
shave:py:jupyter_core:wheel:jupyter_core --> shave:lite:build
shave:py:ipython:wheel:ipython --> shave:lite:build
shave:py:ipywidgets:wheel:ipywidgets --> shave:lite:build
shave:py:ipywidgets:wheel:jupyterlab_widgets --> shave:lite:build
shave:py:ipywidgets:labext:jupyterlab_widgets --> shave:lite:build
shave:py:jupyterlite:pip:jupyterlite-core --> shave:lite:build
shave:py:jupyterlite:labext:jupyterlite-javascript-kernel --> shave:lite:build
shave:py:jupyterlite_pyodide_kernel:pip:jupyterlite_pyodide_kernel --> shave:lite:build
shave:py:jupyterlite_pyodide_kernel:labext:pyodide-kernel-extension --> shave:lite:build
shave:lite:config --> shave:lite:build
subgraph jupyterlab
  jupyterlab:sweep:assets(("`💭 **assets**`")):::hack
  jupyterlab:sweep:labextension(("`💭 **labextension**`")):::hack
  shave:git:jupyterlab:init[("`💭 **init**`")]:::git
  shave:git:jupyterlab:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:jupyterlab:fetch:pr-15443[("`💭 **fetch pr-15443**`")]:::git
  shave:git:jupyterlab:fetch:pr-15347[("`💭 **fetch pr-15347**`")]:::git
  shave:git:jupyterlab:checkout[("`💭 **checkout**`")]:::git
  shave:js:jupyterlab:yarn:install{{"`💭 **yarn install**`"}}:::js
  shave:js:jupyterlab:yarn:buildutils:.{{"`💭 **yarn buildutils .**`"}}:::js
  shave:js:jupyterlab:yarn:builder:.{{"`💭 **yarn builder .**`"}}:::js
  shave:js:jupyterlab:yarn:build:metapackage{{"`💭 **yarn build metapackage**`"}}:::js
  shave:js:jupyterlab:yarn:build:prod:dev_mode{{"`💭 **yarn build prod dev_mode**`"}}:::js
  shave:js:jupyterlab:dist{{"`💭 **dist**`"}}:::js
  shave:py:jupyterlab:pip:jupyterlab["`💭 **pip jupyterlab**`"]:::py
end
subgraph lite
  shave:git:lite:gist:init[("`💭 **gist init**`")]:::git
  shave:git:lite:gist:fetch:main[("`💭 **gist fetch main**`")]:::git
  shave:git:lite:gist:checkout[("`💭 **gist checkout**`")]:::git
  shave:lite:config(["`💭 **config**`"]):::jupyter
  shave:lite:build(["`💭 **build**`"]):::jupyter
end
subgraph traitlets
  shave:git:traitlets:init[("`💭 **init**`")]:::git
  shave:git:traitlets:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:traitlets:checkout[("`💭 **checkout**`")]:::git
  shave:py:traitlets:pip:traitlets["`💭 **pip traitlets**`"]:::py
  shave:py:traitlets:wheel:traitlets["`💭 **wheel traitlets**`"]:::py
end
subgraph comm
  shave:git:comm:init[("`💭 **init**`")]:::git
  shave:git:comm:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:comm:checkout[("`💭 **checkout**`")]:::git
  shave:py:comm:pip:comm["`💭 **pip comm**`"]:::py
  shave:py:comm:wheel:comm["`💭 **wheel comm**`"]:::py
end
subgraph lumino
  shave:git:lumino:init[("`💭 **init**`")]:::git
  shave:git:lumino:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:lumino:fetch:pr-655[("`💭 **fetch pr-655**`")]:::git
  shave:git:lumino:checkout[("`💭 **checkout**`")]:::git
  shave:js:lumino:yarn:install{{"`💭 **yarn install**`"}}:::js
  shave:js:lumino:yarn:build:.{{"`❌ **yarn build .**`"}}:::js
  shave:js:lumino:dist{{"`💭 **dist**`"}}:::js
end
subgraph jupyter_server_terminals
  shave:git:jupyter_server_terminals:init[("`💭 **init**`")]:::git
  shave:git:jupyter_server_terminals:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:jupyter_server_terminals:checkout[("`💭 **checkout**`")]:::git
  shave:py:jupyter_server_terminals:pip:jupyter_server_terminals["`💭 **pip jupyter_server_terminals**`"]:::py
end
subgraph jupyter_core
  shave:git:jupyter_core:init[("`💭 **init**`")]:::git
  shave:git:jupyter_core:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:jupyter_core:checkout[("`💭 **checkout**`")]:::git
  shave:py:jupyter_core:pip:jupyter_core["`💭 **pip jupyter_core**`"]:::py
  shave:py:jupyter_core:wheel:jupyter_core["`💭 **wheel jupyter_core**`"]:::py
end
subgraph jupyter_events
  shave:git:jupyter_events:init[("`💭 **init**`")]:::git
  shave:git:jupyter_events:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:jupyter_events:checkout[("`💭 **checkout**`")]:::git
  shave:py:jupyter_events:pip:jupyter_events["`💭 **pip jupyter_events**`"]:::py
end
subgraph ipython
  shave:git:ipython:init[("`💭 **init**`")]:::git
  shave:git:ipython:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:ipython:checkout[("`💭 **checkout**`")]:::git
  shave:py:ipython:pip:ipython["`💭 **pip ipython**`"]:::py
  shave:py:ipython:wheel:ipython["`💭 **wheel ipython**`"]:::py
end
subgraph jupyter_client
  shave:git:jupyter_client:init[("`💭 **init**`")]:::git
  shave:git:jupyter_client:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:jupyter_client:checkout[("`💭 **checkout**`")]:::git
  shave:py:jupyter_client:pip:jupyter_client["`💭 **pip jupyter_client**`"]:::py
end
subgraph nbformat
  shave:git:nbformat:init[("`💭 **init**`")]:::git
  shave:git:nbformat:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:nbformat:checkout[("`💭 **checkout**`")]:::git
  shave:py:nbformat:pip:nbformat["`💭 **pip nbformat**`"]:::py
end
subgraph nbconvert
  shave:git:nbconvert:init[("`💭 **init**`")]:::git
  shave:git:nbconvert:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:nbconvert:checkout[("`💭 **checkout**`")]:::git
  shave:py:nbconvert:pip:nbconvert["`💭 **pip nbconvert**`"]:::py
end
subgraph ipykernel
  shave:git:ipykernel:init[("`💭 **init**`")]:::git
  shave:git:ipykernel:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:ipykernel:checkout[("`💭 **checkout**`")]:::git
  shave:py:ipykernel:pip:ipykernel["`💭 **pip ipykernel**`"]:::py
end
subgraph nbclient
  shave:git:nbclient:init[("`💭 **init**`")]:::git
  shave:git:nbclient:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:nbclient:checkout[("`💭 **checkout**`")]:::git
  shave:py:nbclient:pip:nbclient["`💭 **pip nbclient**`"]:::py
end
subgraph jupyter_server
  shave:git:jupyter_server:init[("`💭 **init**`")]:::git
  shave:git:jupyter_server:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:jupyter_server:checkout[("`💭 **checkout**`")]:::git
  shave:py:jupyter_server:pip:jupyter_server["`💭 **pip jupyter_server**`"]:::py
end
subgraph notebook_shim
  shave:git:notebook_shim:init[("`💭 **init**`")]:::git
  shave:git:notebook_shim:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:notebook_shim:checkout[("`💭 **checkout**`")]:::git
  shave:py:notebook_shim:pip:notebook_shim["`💭 **pip notebook_shim**`"]:::py
end
subgraph jupyterlab_server
  shave:git:jupyterlab_server:init[("`💭 **init**`")]:::git
  shave:git:jupyterlab_server:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:jupyterlab_server:checkout[("`💭 **checkout**`")]:::git
  shave:py:jupyterlab_server:pip:jupyterlab_server["`💭 **pip jupyterlab_server**`"]:::py
end
subgraph notebook
  shave:git:notebook:init[("`💭 **init**`")]:::git
  shave:git:notebook:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:notebook:checkout[("`💭 **checkout**`")]:::git
  shave:js:notebook:yarn:install{{"`💭 **yarn install**`"}}:::js
  shave:js:notebook:yarn:meta:build:_metapackage{{"`💭 **yarn meta build _metapackage**`"}}:::js
  shave:js:notebook:yarn:app:build:prod:app{{"`💭 **yarn app build prod app**`"}}:::js
  shave:js:notebook:dist{{"`💭 **dist**`"}}:::js
  shave:py:notebook:pip:notebook["`💭 **pip notebook**`"]:::py
  shave:py:notebook:labext:lab-extension(["`💭 **labext lab-extension**`"]):::jupyter
end
subgraph ipywidgets
  shave:git:ipywidgets:init[("`💭 **init**`")]:::git
  shave:git:ipywidgets:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:ipywidgets:fetch:pr-3847[("`💭 **fetch pr-3847**`")]:::git
  shave:git:ipywidgets:checkout[("`💭 **checkout**`")]:::git
  shave:js:ipywidgets:yarn:install{{"`💭 **yarn install**`"}}:::js
  shave:js:ipywidgets:yarn:build:base{{"`💭 **yarn build base**`"}}:::js
  shave:js:ipywidgets:yarn:build:controls{{"`💭 **yarn build controls**`"}}:::js
  shave:js:ipywidgets:yarn:build:base-manager{{"`💭 **yarn build base-manager**`"}}:::js
  shave:js:ipywidgets:yarn:build:html-manager{{"`💭 **yarn build html-manager**`"}}:::js
  shave:js:ipywidgets:yarn:build:output{{"`💭 **yarn build output**`"}}:::js
  shave:js:ipywidgets:yarn:build:jupyterlab_widgets{{"`💭 **yarn build jupyterlab_widgets**`"}}:::js
  shave:js:ipywidgets:dist{{"`💭 **dist**`"}}:::js
  shave:py:ipywidgets:pip:ipywidgets["`💭 **pip ipywidgets**`"]:::py
  shave:py:ipywidgets:wheel:ipywidgets["`💭 **wheel ipywidgets**`"]:::py
  shave:py:ipywidgets:pip:jupyterlab_widgets["`💭 **pip jupyterlab_widgets**`"]:::py
  shave:py:ipywidgets:wheel:jupyterlab_widgets["`💭 **wheel jupyterlab_widgets**`"]:::py
  shave:py:ipywidgets:pip:widgetsnbextension["`💭 **pip widgetsnbextension**`"]:::py
  shave:py:ipywidgets:labext:jupyterlab_widgets(["`💭 **labext jupyterlab_widgets**`"]):::jupyter
end
subgraph jupyterlite
  shave:git:jupyterlite:init[("`💭 **init**`")]:::git
  shave:git:jupyterlite:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:jupyterlite:checkout[("`💭 **checkout**`")]:::git
  shave:js:jupyterlite:yarn:install{{"`💭 **yarn install**`"}}:::js
  shave:js:jupyterlite:yarn:build:.{{"`💭 **yarn build .**`"}}:::js
  shave:js:jupyterlite:dist{{"`💭 **dist**`"}}:::js
  shave:py:jupyterlite:pip:jupyterlite["`💭 **pip jupyterlite**`"]:::py
  shave:py:jupyterlite:pip:jupyterlite-core["`💭 **pip jupyterlite-core**`"]:::py
  shave:py:jupyterlite:pip:jupyterlite-javascript-kernel["`💭 **pip jupyterlite-javascript-kernel**`"]:::py
  shave:py:jupyterlite:labext:jupyterlite-javascript-kernel(["`💭 **labext jupyterlite-javascript-kernel**`"]):::jupyter
end
subgraph jupyterlite_pyodide_kernel
  shave:git:jupyterlite_pyodide_kernel:init[("`💭 **init**`")]:::git
  shave:git:jupyterlite_pyodide_kernel:fetch:main[("`💭 **fetch main**`")]:::git
  shave:git:jupyterlite_pyodide_kernel:checkout[("`💭 **checkout**`")]:::git
  shave:js:jupyterlite_pyodide_kernel:yarn:install{{"`💭 **yarn install**`"}}:::js
  shave:js:jupyterlite_pyodide_kernel:yarn:build:py:wheels:pyodide-kernel{{"`💭 **yarn build py wheels pyodide-kernel**`"}}:::js
  shave:js:jupyterlite_pyodide_kernel:yarn:build:js:pyodide-kernel{{"`💭 **yarn build js pyodide-kernel**`"}}:::js
  shave:js:jupyterlite_pyodide_kernel:yarn:build:lib:pyodide-kernel-extension{{"`💭 **yarn build lib pyodide-kernel-extension**`"}}:::js
  shave:js:jupyterlite_pyodide_kernel:dist{{"`💭 **dist**`"}}:::js
  shave:py:jupyterlite_pyodide_kernel:pip:jupyterlite_pyodide_kernel["`💭 **pip jupyterlite_pyodide_kernel**`"]:::py
  shave:py:jupyterlite_pyodide_kernel:labext:pyodide-kernel-extension(["`💭 **labext pyodide-kernel-extension**`"]):::jupyter
end
subgraph yarnrc
  shave:js:yarnrc{{"`💭 **yarnrc**`"}}:::js
end
</div>
</div>