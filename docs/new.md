# request a preview site

> Make selections below for the most common configuration options, then use the 
> _start pull request_ form to be redirected to GitHub.
> A large number of other configuration options are _possible_, but are not yet fully described.

<style>


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

#show-repo-jupyterlab_pygments:not(:checked) ~ table tbody #repo-jupyterlab_pygments {
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

#show-repo-jupyterlab_lsp:not(:checked) ~ table tbody #repo-jupyterlab_lsp {
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

<fieldset>
<legend><h2>customize GitHub checkout</h2></legend>

<blockquote>
All of the repositories below will be checked out at the current <code>main</code> branch as a <em>baseline</em>.
Check one or more repos to provide use a differnt branch, PR, or tag, or provide one or more PRs to
<i>merge with</i> it, and/or customize the <a href="https://git-scm.com/docs/merge-strategies" target="blank">merge strategy and options</a> to work around merge conflicts.
</blockquote>


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

<input type="checkbox" name="show-repo-jupyterlab_pygments" id="show-repo-jupyterlab_pygments"/>
<label class="show-repo-label" for="show-repo-jupyterlab_pygments">jupyterlab_pygments</label>

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

<input type="checkbox" name="show-repo-jupyterlab_lsp" id="show-repo-jupyterlab_lsp"/>
<label class="show-repo-label" for="show-repo-jupyterlab_lsp">jupyterlab_lsp</label>

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
<th>merge strategy</th>
<th>merge options</th>
</tr>
<tr>
<td><blockquote>
GitHub repository to check out and build
</blockquote></td>
<td><blockquote>
starting point GitHub reference
</blockquote></td>
<td><blockquote>
optional space-delimted list of references to merge into the baseline
</blockquote></td>
<td><blockquote>
merge strategy
</blockquote></td>
<td><blockquote>
additional space-delimeted <code>-X</code> options to pass to <code>git merge</code>
</blockquote></td>
</tr>
</thead>
<tbody>





<tr class="repo" id="repo-traitlets">
<th><code>https://github.com/ipython/traitlets/</code></th>
<td>
<input id="repos-traitlets-github-baseline"
name="repos|traitlets|github|baseline"
type="text"
title="the baseline GitHub URL for traitlets"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-traitlets-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-traitlets-github-merge_with"
name="repos|traitlets|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the traitlets baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-traitlets-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|traitlets|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|traitlets|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-comm">
<th><code>https://github.com/ipython/comm/</code></th>
<td>
<input id="repos-comm-github-baseline"
name="repos|comm|github|baseline"
type="text"
title="the baseline GitHub URL for comm"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-comm-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-comm-github-merge_with"
name="repos|comm|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the comm baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-comm-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|comm|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|comm|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-lumino">
<th><code>https://github.com/jupyterlab/lumino/</code></th>
<td>
<input id="repos-lumino-github-baseline"
name="repos|lumino|github|baseline"
type="text"
title="the baseline GitHub URL for lumino"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-lumino-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-lumino-github-merge_with"
name="repos|lumino|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the lumino baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-lumino-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|lumino|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|lumino|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-jupyter_server_terminals">
<th><code>https://github.com/jupyter-server/jupyter_server_terminals/</code></th>
<td>
<input id="repos-jupyter_server_terminals-github-baseline"
name="repos|jupyter_server_terminals|github|baseline"
type="text"
title="the baseline GitHub URL for jupyter_server_terminals"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-jupyter_server_terminals-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-jupyter_server_terminals-github-merge_with"
name="repos|jupyter_server_terminals|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the jupyter_server_terminals baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-jupyter_server_terminals-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|jupyter_server_terminals|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|jupyter_server_terminals|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-jupyter_core">
<th><code>https://github.com/jupyter/jupyter_core/</code></th>
<td>
<input id="repos-jupyter_core-github-baseline"
name="repos|jupyter_core|github|baseline"
type="text"
title="the baseline GitHub URL for jupyter_core"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-jupyter_core-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-jupyter_core-github-merge_with"
name="repos|jupyter_core|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the jupyter_core baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-jupyter_core-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|jupyter_core|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|jupyter_core|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-jupyter_events">
<th><code>https://github.com/jupyter/jupyter_events/</code></th>
<td>
<input id="repos-jupyter_events-github-baseline"
name="repos|jupyter_events|github|baseline"
type="text"
title="the baseline GitHub URL for jupyter_events"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-jupyter_events-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-jupyter_events-github-merge_with"
name="repos|jupyter_events|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the jupyter_events baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-jupyter_events-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|jupyter_events|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|jupyter_events|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-ipython">
<th><code>https://github.com/ipython/ipython/</code></th>
<td>
<input id="repos-ipython-github-baseline"
name="repos|ipython|github|baseline"
type="text"
title="the baseline GitHub URL for ipython"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-ipython-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-ipython-github-merge_with"
name="repos|ipython|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the ipython baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-ipython-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|ipython|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|ipython|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-jupyterlab_pygments">
<th><code>https://github.com/jupyterlab/jupyterlab_pygments/</code></th>
<td>
<input id="repos-jupyterlab_pygments-github-baseline"
name="repos|jupyterlab_pygments|github|baseline"
type="text"
title="the baseline GitHub URL for jupyterlab_pygments"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-jupyterlab_pygments-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-jupyterlab_pygments-github-merge_with"
name="repos|jupyterlab_pygments|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the jupyterlab_pygments baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-jupyterlab_pygments-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|jupyterlab_pygments|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|jupyterlab_pygments|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-jupyter_client">
<th><code>https://github.com/jupyter/jupyter_client/</code></th>
<td>
<input id="repos-jupyter_client-github-baseline"
name="repos|jupyter_client|github|baseline"
type="text"
title="the baseline GitHub URL for jupyter_client"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-jupyter_client-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-jupyter_client-github-merge_with"
name="repos|jupyter_client|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the jupyter_client baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-jupyter_client-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|jupyter_client|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|jupyter_client|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-nbformat">
<th><code>https://github.com/jupyter/nbformat/</code></th>
<td>
<input id="repos-nbformat-github-baseline"
name="repos|nbformat|github|baseline"
type="text"
title="the baseline GitHub URL for nbformat"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-nbformat-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-nbformat-github-merge_with"
name="repos|nbformat|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the nbformat baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-nbformat-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|nbformat|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|nbformat|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-nbconvert">
<th><code>https://github.com/jupyter/nbconvert/</code></th>
<td>
<input id="repos-nbconvert-github-baseline"
name="repos|nbconvert|github|baseline"
type="text"
title="the baseline GitHub URL for nbconvert"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-nbconvert-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-nbconvert-github-merge_with"
name="repos|nbconvert|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the nbconvert baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-nbconvert-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|nbconvert|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|nbconvert|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-ipykernel">
<th><code>https://github.com/ipython/ipykernel/</code></th>
<td>
<input id="repos-ipykernel-github-baseline"
name="repos|ipykernel|github|baseline"
type="text"
title="the baseline GitHub URL for ipykernel"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-ipykernel-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-ipykernel-github-merge_with"
name="repos|ipykernel|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the ipykernel baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-ipykernel-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|ipykernel|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|ipykernel|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-nbclient">
<th><code>https://github.com/jupyter/nbclient/</code></th>
<td>
<input id="repos-nbclient-github-baseline"
name="repos|nbclient|github|baseline"
type="text"
title="the baseline GitHub URL for nbclient"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-nbclient-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-nbclient-github-merge_with"
name="repos|nbclient|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the nbclient baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-nbclient-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|nbclient|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|nbclient|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-jupyter_server">
<th><code>https://github.com/jupyter-server/jupyter_server/</code></th>
<td>
<input id="repos-jupyter_server-github-baseline"
name="repos|jupyter_server|github|baseline"
type="text"
title="the baseline GitHub URL for jupyter_server"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-jupyter_server-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-jupyter_server-github-merge_with"
name="repos|jupyter_server|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the jupyter_server baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-jupyter_server-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|jupyter_server|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|jupyter_server|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-notebook_shim">
<th><code>https://github.com/jupyter/notebook_shim/</code></th>
<td>
<input id="repos-notebook_shim-github-baseline"
name="repos|notebook_shim|github|baseline"
type="text"
title="the baseline GitHub URL for notebook_shim"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-notebook_shim-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-notebook_shim-github-merge_with"
name="repos|notebook_shim|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the notebook_shim baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-notebook_shim-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|notebook_shim|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|notebook_shim|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-jupyterlab_server">
<th><code>https://github.com/jupyterlab/jupyterlab_server/</code></th>
<td>
<input id="repos-jupyterlab_server-github-baseline"
name="repos|jupyterlab_server|github|baseline"
type="text"
title="the baseline GitHub URL for jupyterlab_server"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-jupyterlab_server-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-jupyterlab_server-github-merge_with"
name="repos|jupyterlab_server|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the jupyterlab_server baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-jupyterlab_server-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|jupyterlab_server|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|jupyterlab_server|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-jupyterlab_lsp">
<th><code>https://github.com/jupyter-lsp/jupyterlab-lsp/</code></th>
<td>
<input id="repos-jupyterlab_lsp-github-baseline"
name="repos|jupyterlab_lsp|github|baseline"
type="text"
title="the baseline GitHub URL for jupyterlab_lsp"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-jupyterlab_lsp-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-jupyterlab_lsp-github-merge_with"
name="repos|jupyterlab_lsp|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the jupyterlab_lsp baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-jupyterlab_lsp-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|jupyterlab_lsp|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|jupyterlab_lsp|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-jupyterlab">
<th><code>https://github.com/jupyterlab/jupyterlab/</code></th>
<td>
<input id="repos-jupyterlab-github-baseline"
name="repos|jupyterlab|github|baseline"
type="text"
title="the baseline GitHub URL for jupyterlab"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-jupyterlab-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-jupyterlab-github-merge_with"
name="repos|jupyterlab|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the jupyterlab baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-jupyterlab-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|jupyterlab|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|jupyterlab|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-notebook">
<th><code>https://github.com/jupyter/notebook/</code></th>
<td>
<input id="repos-notebook-github-baseline"
name="repos|notebook|github|baseline"
type="text"
title="the baseline GitHub URL for notebook"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-notebook-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-notebook-github-merge_with"
name="repos|notebook|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the notebook baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-notebook-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|notebook|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|notebook|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-ipywidgets">
<th><code>https://github.com/jupyter-widgets/ipywidgets/</code></th>
<td>
<input id="repos-ipywidgets-github-baseline"
name="repos|ipywidgets|github|baseline"
type="text"
title="the baseline GitHub URL for ipywidgets"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-ipywidgets-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-ipywidgets-github-merge_with"
name="repos|ipywidgets|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the ipywidgets baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-ipywidgets-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|ipywidgets|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|ipywidgets|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-jupyterlite">
<th><code>https://github.com/jupyterlite/jupyterlite/</code></th>
<td>
<input id="repos-jupyterlite-github-baseline"
name="repos|jupyterlite|github|baseline"
type="text"
title="the baseline GitHub URL for jupyterlite"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-jupyterlite-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-jupyterlite-github-merge_with"
name="repos|jupyterlite|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the jupyterlite baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-jupyterlite-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|jupyterlite|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|jupyterlite|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>





<tr class="repo" id="repo-jupyterlite_pyodide_kernel">
<th><code>https://github.com/jupyterlite/pyodide-kernel/</code></th>
<td>
<input id="repos-jupyterlite_pyodide_kernel-github-baseline"
name="repos|jupyterlite_pyodide_kernel|github|baseline"
type="text"
title="the baseline GitHub URL for jupyterlite_pyodide_kernel"
spellcheck="false"
placeholder="tree/main"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)"
/>
<label for="repos-jupyterlite_pyodide_kernel-github-baseline">
must be empty, or one of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<input id="repos-jupyterlite_pyodide_kernel-github-merge_with"
name="repos|jupyterlite_pyodide_kernel|github|merge_with"
title="one or more space-delimited GitHub URLs to merge into the jupyterlite_pyodide_kernel baseline"
type="text"
spellcheck="false"
placeholder="pull/{:number} tree/{:branch} releases/tag/{:tag}"
pattern="^$|^(tree/[^s]+|pull/\d+|releases/tag/[^s]+)(\s+(tree/[^s]+|pull/\d+|releases/tag/[^s]+))*"
/>
<label for="repos-jupyterlite_pyodide_kernel-github-merge_with">
must be empty, or one or more (separated by space) of:<br/>
<code>pull/{:number}</code><br/>
<code>tree/{:branch}</code><br/>
<code>releases/tag/{:tag}</code>
</label>
</td>
<td>
<select
name="repos|jupyterlite_pyodide_kernel|github|merge_strategy"
title="choose a different git merge strategy"
>
<option value="">ort (default)</option>
<option>resolve</option>
<option>octopus</option>
<option>ours</option>
<option>subtree</option>
</select>
</td>
<td>
<input
name="repos|jupyterlite_pyodide_kernel|github|merge_options"
type="text"
title="add space-delimted -X options for the merge strategy"
/>
</td>
</tr>

</tbody>
</table>

<fieldset>
<legend>customize JupyterLite</legend>

<blockquote>
If given, an optional <a target="_blank" href="https://gist.github.com/">gist</a> will be cloned
to provide the content of the JupyterLite site.
If the gist contains <code>jupyter_lite_config.json</code> and/or <code>jupyter-lite.json</code>,
this will be merged into the generated
<a target="_blank" href="https://jupyterlite.readthedocs.io/en/latest/howto/configure/config_files.html">configuration</a>
of <code>jupyter lite build</code> and the runtime application.
</blockquote>

<input id="lite-gist"
type="text"
name="lite|gist"
pattern="^$|^[a-z\d]{20,}$"
placeholder="gist ID"
/>
<label for="lite-gist">the gist ID must be empty, or contain 20+ letters and numbers</label>
</fieldset>
</form>
<style>
.bd-main .bd-content .bd-article-container .bd-article {
padding: 0;
}
.bd-sidebar-primary {
padding-bottom: 0;
}
</style>

<div class="work-sidebar">
<div class="work-sidebar-header">
<i class="fas fa-code-pull-request"></i>
start pull request
</div>
<div class="work-sidebar-content">
<form id="propose" method="get" action="https://github.com/deathbeds/jupyak/new/main" target="_blank">
<label for="toml-preview"><code>jupyak_config.toml</code> contents</label>
<textarea
required="true"
id="toml-preview"
name="value"
spellcheck="false"
placeholder="# make choices in the form"
></textarea>
<input type="hidden" name="filename" value="jupyak_config.toml"/>
<br/>
<button class="btn btn-success" form="propose">
<i class="fas fa-github-alt"></i> new pull request...
</button>
</form>
</div>
</div>
<script type="importmap">
{
"imports": {
"json2toml": "https://cdn.skypack.dev/pin/json2toml@v6.0.0-d8Y8va9lNUE85BZ5GSQ2/mode=imports,min/optimized/json2toml.js"
}
}
</script>
<script type="module">
document.addEventListener('DOMContentLoaded', async function(){
const form = document.querySelector('form#new');
const preview = document.querySelector('#toml-preview');
const selector = 'form#new input[type="text"], form#new select';
const inputs = [...document.querySelectorAll(selector)];
const split_fields = ['merge_with', 'merge_options'];
async function update() {
const json2toml = (await import('json2toml')).default;
const config = find_config();
preview.value = json2toml(config);
}
function find_config() {
const config = {};
const data = new FormData(form);
for (const [name, value] of data.entries()) {
if(document.querySelector(`input[name="${name}"]:invalid`)) {
continue
}
let bits = name.split("|");
if(value.trim() === "" || bits.length == 1){
continue;
}
let current = config;
for(const bit of bits.slice(0, -1)) {
if(!current[bit]) {
current[bit] = {};
}
current = current[bit];
}
let last_bit = bits[bits.length - 1];
current[last_bit] = (
split_fields.includes(last_bit) ?
value.split(/[\s\n]+/):
value
);
}
return config;
}
inputs.map((input) => input.addEventListener('input', update))
})

</script>
