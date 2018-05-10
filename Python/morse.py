#!/usr/bin/python2.7
"""
morse.py

Takes input from the Name to morse form and returns the web-page including the results.
"""
# Import modules
import os
import cgi
import lib01
from urllib import urlopen
# Global variables

#===============================================================================
# FUNCTIONS
#===============================================================================
def morse_pg(name):
    '''
    Load morse code conversion page
    '''
    page   = urlopen('http://localhost/python.html').read()
    morse, alpha = lib01.name2Morse(name)
    content = page.replace('<p id="morsecode"></p>',alpha+'<br>'+morse)
    return content


#===============================================================================
# MAIN
#===============================================================================
# Top of program, main code
ctrls = cgi.FieldStorage()
name = ctrls['your_name'].value
html = morse_pg(name)
print('Content-type: text/html\n')
print(html)
