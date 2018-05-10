#!/Python27/python.exe
# -*- coding: utf-8-1 -*-
"""
lib01.py

The function library for my web-site which includes the functions;

    get_settings
    getComments
    getCommentsPage
    loanCalc
    name2Morse
    name2AlphaNum
    LetterGroups
"""
import os
import sys
import pickle
import psycopg2 as pgdb
from urllib import urlopen

def get_settings():
    '''
    Retrieve settings
    '''
    fn = 'settings.cfg'
    fileObj = open(fn,'r')
    cfg = pickle.load(fileObj)
    fileObj.close()

    odbc = cfg[0]
    db_cfg = cfg[1]
    sqlTable = db_cfg['db_schema']+'.'+db_cfg['db_table']
    return [odbc,db_cfg,sqlTable]


def getComments(sortBy):
    '''
    Query comments table and return data or None
    ''' 
    db = get_settings()
    db_conn = pgdb.connect(**db[0])
    qry = "Select entry_dt, comment, id From "+db[2]+sortBy
    pgqry = db_conn.cursor()
    pgqry.execute(qry)
    if pgqry.rowcount == 0: rows = None
    else: rows = pgqry.fetchall()
    pgqry.close()
    db_conn.close()
    return rows  

def getCommentsPage(*params):
    '''
    Load the comment list page
    '''
    page = urlopen('http://localhost/python.html').read()
    col1 = 'col1'
    col2 = 'col2'

    if len(params) == 0:
        sortBy = " Order By entry_dt desc, id desc"
    else:
        if params[0] == 1:
            sortBy = " Order By entry_dt asc, id desc"
            col1 = 'col1a'
        elif params[0] == 2:
            sortBy = " Order By comment asc"
            col2 = 'col2a'
        elif params[0] == 3:
            sortBy = " Order By comment desc"

    data   = getComments(sortBy)
    if data == None: table = '<p id="comments">No comments to show</p><br>'
    else:
        table = '<form method=POST action="/cgi-bin/view_comment.py" enctype="multipart/form-data"><table>'
        table = table + '<tr><th id="comm_col1"><input id="comm_hdr1" name="'+col1+'" value="Date" type="submit" class="w3-btn" style="text-decoration: line;"></th>'
        table = table + '<th><input id="comm_hdr2" name="'+col2+'" value="Comment" type="submit" class="w3-btn" style="text-decoration: line;"></th></tr>'
        for row in data:
            table = table + '<tr><td id="comm_col1">'+row[0].isoformat()+'</td><td>'+row[1]+'</td></tr>'
        table = table + '</table></form>'

    content = page.replace('<p id="comments"></p>',table)
    content = content.replace('<div id="text1" class="w3-panel example">','<div id="text1" class="w3-panel example" style="display:none">')
    content = content.replace('<div id="db2" class="w3-panel example" style="display:none">','<div id="db2" class="w3-panel example">')
    return content


def loanCalc(amount,term,rate):
    '''
    loanCalc

    arguments:
        amount is total loan value
        term is number of years
        rate is interest rate as fraction i.e. 3.25% = .0325

    returns:
        Monthly repayment
    '''
    l = float(amount)
    t = int(term) * -1
    r = float(rate) / 100
    #print('(('+str(r)+' / 12.0)/(1.0 - (1.0 + '+str(r)+' / 12.0) ** ('+str(t)+' * 12.0))) * '+str(l))
    return ((r / 12.0)/(1.0 - (1.0 + r / 12.0) ** (t * 12.0))) * l
   

def name2Morse(name):
    '''
    Function: name2Morse

    Return name as morse code

    Arguments:
        name

    Returns:
        string of morse code
    '''
    colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    colour = 0
	
    morse = '<p id="result" style="color: '+colours[colour]+';">'
    alpha = morse
    colour += 1
    morseDict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'..', 'E':'.',
                 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
                 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.',
                 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-',
                 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----',
                 '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
                 '6':'-....', '7':'--...', '8':'---..', '9':'----.', 'Ä':'.-.-',
                 'Á':'.--.-', 'Å':'.--.-', 'Ch':'----', 'É':'..-..', 'Ñ':'--.--',
                 'Ö':'---.', 'Ü':'..--', '.':'.-.-.-', ',':'--..--', ':':'---...',
                 '?':'..--..', "'":'.----.', '-':'-....-', '/':'-..-.', '(':'-.--.-',
                 ')':'-.--.-', '"':'.-..-.', '@':'.--.-.', '=':'-...-'}

    for ch in name.upper():
        try:
            morse = morse + morseDict[ch]+' </p><p id="result" style="color: '+colours[colour]+';">'
            alpha = alpha + ch + ' ' * (len(morseDict[ch])-1) +' </p><p id="result" style="color: '+colours[colour]+';">'
            if colour == 6: colour = 0
            else: colour += 1
        except KeyError:
            if ch == ' ':
                morse = morse + '   '
                alpha = alpha + '   '
                colour == 0
    morse = morse[:morse.rfind('</p>')+4]
    alpha = alpha[:alpha.rfind('</p>')+4]
    return morse, alpha


def name2AlphaNum(name):
    '''
    Function: name2AlphaNum

    Return name as position numbers from alphabet
    i.e. a = 1, b = 2, etc....

    Arguments:
        name

    Returns:
        string of numbers
    '''
    numName = ''
    nameSum = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha_enum = enumerate(alphabet)
    soup = {letter: str(offset+1) for offset, letter in alpha_enum}
    for ch in name.lower():
        try:
            numName = numName + soup[ch]+' '
            nameSum += int(soup[ch])
        except KeyError:
            if ch == ' ': numName = numName + '   '
    numName = numName + '= ' + str(nameSum)
    return numName


def LetterGroups(sentence,group_len):
    '''
    Function: LetterGroups
    
    Return matching groups of letters

    Arguments:
        sentence    string    words
        group_len   integer   length of mathcing groups to extract

    Returns:
        string      matching groups
    '''
    actual_words = sentence.split(' ')  # Split string into list of words
    matching_groups = []                # Define empty lists
    groups = []
    for word in actual_words:           # Step through words
        word = word.lower()
        if len(word) > group_len:       # If word is longer than requested group length
            for n in range(0,len(word)-(group_len-1)):  # Step through word extracting blocks
                groups.append(word[n:n+group_len])      # to build group list
                
        elif len(word) == group_len:                    # Add whole word if exactly the right length
            groups.append(word)

    for group in groups:      
        if groups.count(group) > 1:             # Look for groups that occur more than once
            if group not in matching_groups:    # Create list of unique
                matching_groups.append(group)   # groups
    return matching_groups


#===============================================================================
# MAIN
#===============================================================================
# Top of program, main code
def main():
    print('Self-testing')
    res = [(n, semiPrime(n)) for n in range(1,1000) if semiPrime(n)]
    print('Semi primes between 1-100 - '+str(res))
    name = 'Tony King'
    morse, alpha = name2Morse(name)
    print(alpha)
    print(morse)
    name = 'Anthony King'
    print(name+' -'+name2AlphaNum(name))

    words = '''When the contact centre’s work (calls, emails, webchats etc) varies from forecast, and staff attendance is not what was expected on the day, the smart thing to do is to adapt the schedule received from the planning team and move people around to where they are needed.
\nBut different people have different skills, preferences, contracts, schedules, breaks…and you might not be sure what work levels will be in 40 minutes time. Getting it right is tricky.'''
    print(words+'\n\n Matching groups: '+str(LetterGroups(words,4)))
    words = 'test'
    groups = LetterGroups(words,4)
    if groups == []:
        print('No matching groups')
    else:
        print(words+'\n\n Matching groups: '+str())

    print('Monthly repayments: '+str(loanCalc(199000,25,0.0214))) # Loan amount, term in years, and interest rate

#--------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
