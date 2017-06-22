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
    filename = file.split('/')[1] # remove 'html/'
    notebook_nicename = filename.split('.')[0].replace('-',' ')

    index_files += "<a href='{0}' data-featherlight='iframe'>{1}</a><br/>\n".format(file, notebook_nicename)

file_contents = """
<!DOCTYPE html>
<html lang="en">
  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">

    <title>Iacchus Mercurius Jupyter Notebooks</title>

    <link href="index_files/featherlight.min.css" type="text/css" rel="stylesheet" />
    <link rel="stylesheet" href="index_files/style.css">

    <link href='https://fonts.googleapis.com/css?family=Old+Standard+TT|Slabo+27px|Roboto:400,700|Inconsolata:400,700' rel='stylesheet' type='text/css'>

    <!--<script src="script.js"></script>-->
    <script src="index_files/jquery-latest.js"></script>
    <script src="index_files/featherlight.min.js" type="text/javascript" charset="utf-8"></script>


  </head>
  <body>
    <a href="https://github.com/iacchus/jupyter-notebooks/"><img id="github-fork" src="index_files/github-corner-right.svg" /></a>
    <div id="page-container">
      <h1>Index of Jupyter Notebooks exported to html</h1>

      <div id="presentation">
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
