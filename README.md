# jupyter-venv
Repository for some of my notebooks / experiments with python

## See html index

<a href='https://iacchus.github.io/jupyter-venv/'>https://iacchus.github.io/jupyter-venv/</a>

## Creating the index.html

We are using this git pre-commit hook to generate the index for the exported  HTML files:

### pre-commit (git hook)

```python
#!/usr/bin/env python

import glob

index_filename = "index.html"

html_files = glob.glob('html/**/**.html',recursive=True)

index_files = str()

for file in html_files:
    index_files += "<a href='{0}'>{0}</a><br/>\n".format(file)

file_contents = """
<h1>Index of Jupyter Notebooks exported to html</h1>

From the repository <a href="https://github.com/iacchus/jupyter-venv/">https://github.com/iacchus/jupyter-venv/</a><br/><br/>

{0}
""".format(index_files)

print(file_contents)

with open(index_filename,'w') as fd:
    fd.write(file_contents)
    fd.close()
```

### post-commit (git hook)

```sh
#!/usr/bin/env bash

if grep 'Untracked' <<< $(git status); then
	git add .
	git commit -a -m 'redoing commit from gits post-commit hook.'
else
	:
fi
```
