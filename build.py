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
html_files.sort()

index_files = str()

print("Writing index file listing..")
for file in html_files:
    index_files += "<a href='{0}' data-featherlight='iframe'>{0}</a><br/>\n".format(file)

file_contents = """
<!DOCTYPE html>
<html lang="en">
  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">

    <title>Iacchi Mercurii' Jupyter Notebooks</title>

    <link href="index_files/featherlight.min.css" type="text/css" rel="stylesheet" />
    <link rel="stylesheet" href="index_files/style.css">

    <!--<script src="script.js"></script>-->
    <script src="index_files/jquery-latest.js"></script>
    <script src="index_files/featherlight.min.js" type="text/javascript" charset="utf-8"></script>

  </head>
  <body>
    <div id="page-container">
      <h1>Index of Jupyter Notebooks exported to html</h1>

      <div id="presentation">
        From the repository <a href="https://github.com/iacchus/jupyter-notebooks/">https://github.com/iacchus/jupyter-notebooks/</a><br/><br/>
      </div>

      <div id="files">
        <div id="files-title">Browse files..</div>
{0}
      </div> 
    </div>
  </body>
</html>
""".format(index_files)

#print(file_contents)

print("Writing index file '{}'..".format(index_filename))

with open(index_filename,'w') as fd:
    fd.write(file_contents)
    fd.close()

git_commands = "git add .; git commit -a -m 'autocommit from build.py!'; git push"
print("Running git commands {}..".format(git_commands))
os.system(git_commands)

print("Done..")
