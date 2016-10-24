#!/usr/bin/env python

import glob
import os
#from os.path import isfile, getmtime
#import datetime

index_filename = "index.html"

# lets's first convert all ipynb which it's more recent than it's html
## some day maybe?
#ipynb_files = glob.glob('*.ipynb',recursive=False)

#for nbook in ipynb_files:
#    if isfile

nbconvert_command = "nbconvert *.ipynb --to html --output-dir html/ --template full"
os.system(nbconvert_command)

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
