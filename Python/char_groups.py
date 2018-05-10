#!/usr/bin/python2.7
"""
char_groups.py

Takes input from the Common letter groups form and returns the web-page with the results.
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
def process(data, group_size):
    '''
    Process text input and colour the resulting output, then then return the
    web-page content with the results inserted.
    '''
    page   = urlopen('http://localhost/python.html').read()
    groups = lib01.LetterGroups(data, group_size)
    colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    colour = 0
    matching_groups = ''
    if groups == []:
        matching_groups = '<p id="result2" style="color: '+colours[colour]+';">No matching letter groups</p>'
    else:
        for group in groups:
            matching_groups = matching_groups + '<p id="result2" style="color: '+colours[colour]+';">'+group + ' </p>'
            if colour == 6: colour = 0
            else: colour += 1
    content = page.replace('<p id="groups"></p>',
                           'Your text:'+'<br><p style="color: grey;">'+data+'</p><br>Matching letter groups found:<br><div style="width: 800px;">'+matching_groups+'</div><br>')
    content = content.replace('<div id="text1" class="w3-panel example">','<div id="text1" class="w3-panel example" style="display:none">')
    content = content.replace('<div id="text2" class="w3-panel example" style="display:none">','<div id="text2" class="w3-panel example">')
    return content
    

#===============================================================================
# MAIN
#===============================================================================
# Top of program, main code
ctrls = cgi.FieldStorage()
group_size = int(ctrls['group_size'].value)
data = ctrls['your_text'].value
html = process(data, group_size)
print('Content-type: text/html\n')
print(html)
