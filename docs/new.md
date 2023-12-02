# new
<style>

.show-repo-label { padding-right: 1rem; }
.repo input[type="text"],
.repo textarea {
min-width: 32rem;
}


#show-repo-traitlets:not(:checked) ~ table tbody #repo-traitlets {
display: none;
}

#show-repo-comm:not(:checked) ~ table tbody #repo-comm {
display: none;
}

#show-repo-lumino:not(:checked) ~ table tbody #repo-lumino {
display: none;
}

#show-repo-jupyter_server_terminals:not(:checked) ~ table tbody #repo-jupyter_server_terminals {
display: none;
}

#show-repo-jupyter_core:not(:checked) ~ table tbody #repo-jupyter_core {
display: none;
}

#show-repo-jupyter_events:not(:checked) ~ table tbody #repo-jupyter_events {
display: none;
}

#show-repo-ipython:not(:checked) ~ table tbody #repo-ipython {
display: none;
}

#show-repo-jupyter_client:not(:checked) ~ table tbody #repo-jupyter_client {
display: none;
}

#show-repo-nbformat:not(:checked) ~ table tbody #repo-nbformat {
display: none;
}

#show-repo-nbconvert:not(:checked) ~ table tbody #repo-nbconvert {
display: none;
}

#show-repo-ipykernel:not(:checked) ~ table tbody #repo-ipykernel {
display: none;
}

#show-repo-nbclient:not(:checked) ~ table tbody #repo-nbclient {
display: none;
}

#show-repo-jupyter_server:not(:checked) ~ table tbody #repo-jupyter_server {
display: none;
}

#show-repo-notebook_shim:not(:checked) ~ table tbody #repo-notebook_shim {
display: none;
}

#show-repo-jupyterlab_server:not(:checked) ~ table tbody #repo-jupyterlab_server {
display: none;
}

#show-repo-jupyterlab:not(:checked) ~ table tbody #repo-jupyterlab {
display: none;
}

#show-repo-notebook:not(:checked) ~ table tbody #repo-notebook {
display: none;
}

#show-repo-ipywidgets:not(:checked) ~ table tbody #repo-ipywidgets {
display: none;
}

#show-repo-jupyterlite:not(:checked) ~ table tbody #repo-jupyterlite {
display: none;
}

#show-repo-jupyterlite_pyodide_kernel:not(:checked) ~ table tbody #repo-jupyterlite_pyodide_kernel {
display: none;
}

</style>
<form id="new">
<table>
<thead><tr>
<th>section</th>
<th>options</th>
</tr></thead>
<tbody>

<tr>
<th>repos</th>
<td>
defaults:<br/>

<input type="checkbox" name="show-repo-traitlets" id="show-repo-traitlets"/>
<label class="show-repo-label" for="show-repo-traitlets">traitlets</label>

<input type="checkbox" name="show-repo-comm" id="show-repo-comm"/>
<label class="show-repo-label" for="show-repo-comm">comm</label>

<input type="checkbox" name="show-repo-lumino" id="show-repo-lumino"/>
<label class="show-repo-label" for="show-repo-lumino">lumino</label>

<input type="checkbox" name="show-repo-jupyter_server_terminals" id="show-repo-jupyter_server_terminals"/>
<label class="show-repo-label" for="show-repo-jupyter_server_terminals">jupyter_server_terminals</label>

<input type="checkbox" name="show-repo-jupyter_core" id="show-repo-jupyter_core"/>
<label class="show-repo-label" for="show-repo-jupyter_core">jupyter_core</label>

<input type="checkbox" name="show-repo-jupyter_events" id="show-repo-jupyter_events"/>
<label class="show-repo-label" for="show-repo-jupyter_events">jupyter_events</label>

<input type="checkbox" name="show-repo-ipython" id="show-repo-ipython"/>
<label class="show-repo-label" for="show-repo-ipython">ipython</label>

<input type="checkbox" name="show-repo-jupyter_client" id="show-repo-jupyter_client"/>
<label class="show-repo-label" for="show-repo-jupyter_client">jupyter_client</label>

<input type="checkbox" name="show-repo-nbformat" id="show-repo-nbformat"/>
<label class="show-repo-label" for="show-repo-nbformat">nbformat</label>

<input type="checkbox" name="show-repo-nbconvert" id="show-repo-nbconvert"/>
<label class="show-repo-label" for="show-repo-nbconvert">nbconvert</label>

<input type="checkbox" name="show-repo-ipykernel" id="show-repo-ipykernel"/>
<label class="show-repo-label" for="show-repo-ipykernel">ipykernel</label>

<input type="checkbox" name="show-repo-nbclient" id="show-repo-nbclient"/>
<label class="show-repo-label" for="show-repo-nbclient">nbclient</label>

<input type="checkbox" name="show-repo-jupyter_server" id="show-repo-jupyter_server"/>
<label class="show-repo-label" for="show-repo-jupyter_server">jupyter_server</label>

<input type="checkbox" name="show-repo-notebook_shim" id="show-repo-notebook_shim"/>
<label class="show-repo-label" for="show-repo-notebook_shim">notebook_shim</label>

<input type="checkbox" name="show-repo-jupyterlab_server" id="show-repo-jupyterlab_server"/>
<label class="show-repo-label" for="show-repo-jupyterlab_server">jupyterlab_server</label>

<input type="checkbox" name="show-repo-jupyterlab" id="show-repo-jupyterlab"/>
<label class="show-repo-label" for="show-repo-jupyterlab">jupyterlab</label>

<input type="checkbox" name="show-repo-notebook" id="show-repo-notebook"/>
<label class="show-repo-label" for="show-repo-notebook">notebook</label>

<input type="checkbox" name="show-repo-ipywidgets" id="show-repo-ipywidgets"/>
<label class="show-repo-label" for="show-repo-ipywidgets">ipywidgets</label>

<input type="checkbox" name="show-repo-jupyterlite" id="show-repo-jupyterlite"/>
<label class="show-repo-label" for="show-repo-jupyterlite">jupyterlite</label>

<input type="checkbox" name="show-repo-jupyterlite_pyodide_kernel" id="show-repo-jupyterlite_pyodide_kernel"/>
<label class="show-repo-label" for="show-repo-jupyterlite_pyodide_kernel">jupyterlite_pyodide_kernel</label>

<table style="position: relative;">
<thead style="position: sticky; top: 0;">
<tr>
<th>repo</th>
<th>baseline</th>
<th>merge with</th>
</tr>
</thead>
<tbody>



<tr class="repo" id="repo-traitlets">
<th>traitlets</th>
<td>
<input name="repos|traitlets|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/ipython/traitlets/tree/main" />
</td>
<td>
<textarea 
name="repos|traitlets|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-comm">
<th>comm</th>
<td>
<input name="repos|comm|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/ipython/comm/tree/main" />
</td>
<td>
<textarea 
name="repos|comm|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-lumino">
<th>lumino</th>
<td>
<input name="repos|lumino|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyterlab/lumino/tree/main" />
</td>
<td>
<textarea 
name="repos|lumino|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-jupyter_server_terminals">
<th>jupyter_server_terminals</th>
<td>
<input name="repos|jupyter_server_terminals|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyter-server/jupyter_server_terminals/tree/main" />
</td>
<td>
<textarea 
name="repos|jupyter_server_terminals|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-jupyter_core">
<th>jupyter_core</th>
<td>
<input name="repos|jupyter_core|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyter/jupyter_core/tree/main" />
</td>
<td>
<textarea 
name="repos|jupyter_core|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-jupyter_events">
<th>jupyter_events</th>
<td>
<input name="repos|jupyter_events|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyter/jupyter_events/tree/main" />
</td>
<td>
<textarea 
name="repos|jupyter_events|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-ipython">
<th>ipython</th>
<td>
<input name="repos|ipython|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/ipython/ipython/tree/main" />
</td>
<td>
<textarea 
name="repos|ipython|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-jupyter_client">
<th>jupyter_client</th>
<td>
<input name="repos|jupyter_client|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyter/jupyter_client/tree/main" />
</td>
<td>
<textarea 
name="repos|jupyter_client|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-nbformat">
<th>nbformat</th>
<td>
<input name="repos|nbformat|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyter/nbformat/tree/main" />
</td>
<td>
<textarea 
name="repos|nbformat|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-nbconvert">
<th>nbconvert</th>
<td>
<input name="repos|nbconvert|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyter/nbconvert/tree/main" />
</td>
<td>
<textarea 
name="repos|nbconvert|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-ipykernel">
<th>ipykernel</th>
<td>
<input name="repos|ipykernel|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/ipython/ipykernel/tree/main" />
</td>
<td>
<textarea 
name="repos|ipykernel|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-nbclient">
<th>nbclient</th>
<td>
<input name="repos|nbclient|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyter/nbclient/tree/main" />
</td>
<td>
<textarea 
name="repos|nbclient|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-jupyter_server">
<th>jupyter_server</th>
<td>
<input name="repos|jupyter_server|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyter-server/jupyter_server/tree/main" />
</td>
<td>
<textarea 
name="repos|jupyter_server|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-notebook_shim">
<th>notebook_shim</th>
<td>
<input name="repos|notebook_shim|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyter/notebook_shim/tree/main" />
</td>
<td>
<textarea 
name="repos|notebook_shim|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-jupyterlab_server">
<th>jupyterlab_server</th>
<td>
<input name="repos|jupyterlab_server|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyterlab/jupyterlab_server/tree/main" />
</td>
<td>
<textarea 
name="repos|jupyterlab_server|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-jupyterlab">
<th>jupyterlab</th>
<td>
<input name="repos|jupyterlab|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyterlab/jupyterlab/tree/main" />
</td>
<td>
<textarea 
name="repos|jupyterlab|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-notebook">
<th>notebook</th>
<td>
<input name="repos|notebook|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyter/notebook/tree/main" />
</td>
<td>
<textarea 
name="repos|notebook|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-ipywidgets">
<th>ipywidgets</th>
<td>
<input name="repos|ipywidgets|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyter-widgets/ipywidgets/tree/main" />
</td>
<td>
<textarea 
name="repos|ipywidgets|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-jupyterlite">
<th>jupyterlite</th>
<td>
<input name="repos|jupyterlite|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyterlite/jupyterlite/tree/main" />
</td>
<td>
<textarea 
name="repos|jupyterlite|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>



<tr class="repo" id="repo-jupyterlite_pyodide_kernel">
<th>jupyterlite_pyodide_kernel</th>
<td>
<input name="repos|jupyterlite_pyodide_kernel|github|baseline" 
type="text" 
spellcheck="false" 
placeholder="https://github.com/jupyterlite/pyodide-kernel/tree/main" />
</td>
<td>
<textarea 
name="repos|jupyterlite_pyodide_kernel|github|merge_with" 
spellcheck="false" 
placeholder="one PR per line"></textarea>
</td>
</tr>

</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</form>