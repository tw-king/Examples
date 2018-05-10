#!/usr/bin/python2.7
"""
repayments.py

Takes input from the Loan repayments form and returns the web-page with the results.
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
def process(repayment):
    '''
    Load loan repayments
    '''
    page   = urlopen('http://localhost/python.html').read()
    content = page.replace('<p id="repayments"></p>',
                           '<p id="repayments">Your repayments will be &pound;{0:.2f}</p>'.format(repayment))
    content = content.replace('<div id="text1" class="w3-panel example">','<div id="text1" class="w3-panel example" style="display:none">')
    content = content.replace('<div id="calc1" class="w3-panel example" style="display:none">','<div id="calc1" class="w3-panel example">')
    return content
    

#===============================================================================
# MAIN
#===============================================================================
# Top of program, main code
ctrls = cgi.FieldStorage()
amount = ctrls['borrowed'].value
term = ctrls['term'].value
rate = ctrls['rate'].value
repayment = lib01.loanCalc(amount,term,rate)
html = process(repayment)
print('Content-type: text/html\n')
print(html)
