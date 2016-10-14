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


