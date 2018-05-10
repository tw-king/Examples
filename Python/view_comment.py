#!/usr/bin/python2.7
"""
view_comment.py

Displays comments records from the Postgres database and responds to sort order requests.
"""
# Import modules
import os
import cgi
import lib01

# Global variables

#===============================================================================
# FUNCTIONS
#===============================================================================
    

#===============================================================================
# MAIN
#===============================================================================
# Top of program, main code
ctrls = cgi.FieldStorage()
if 'col1' in ctrls:
    html = lib01.getCommentsPage(1)
elif 'col2' in ctrls:
    html = lib01.getCommentsPage(2)
elif 'col2a' in ctrls:
    html = lib01.getCommentsPage(3)
else:
    html = lib01.getCommentsPage()
print('Content-type: text/html\n')
print(html)
