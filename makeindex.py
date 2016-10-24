#!/usr/bin/env python

import glob
import os
#from os.path import isfile, getmtime
#import datetime


# lets's first convert all ipynb which it's more recent than it's html
## some day maybe?
#ipynb_files = glob.glob('*.ipynb',recursive=False)

#for nbook in ipynb_files:
#    if isfile

nbconvert_command = "jupyter nbconvert *.ipynb --to html --output-dir html/ --template full"
print("Running nbconvert command: '{}'..".format(nbconvert_command))
os.system(nbconvert_command)

index_filename = "index.html"

print("Listing html files..")
html_files = glob.glob('html/**/**.html',recursive=True)

index_files = str()

print("Writing index file listing..")
for file in html_files:
    index_files += "<a href='{0}'>{0}</a><br/>\n".format(file)

file_contents = """
<h1>Index of Jupyter Notebooks exported to html</h1>

From the repository <a href="https://github.com/iacchus/jupyter-venv/">https://github.com/iacchus/jupyter-venv/</a><br/><br/>

{0}
""".format(index_files)

print(file_contents)

print("Writing index file '{}'..".format(index_filename))

with open(index_filename,'w') as fd:
    fd.write(file_contents)
    fd.close()

print("Done..")
