#!/usr/bin/python2.7
"""
add_comment.py

Takes inpit from the Add comment form and inserts it into a Postgres database table.
"""
# Import modules
import os
import cgi
import lib01
from urllib import urlopen
import psycopg2 as pgdb
# Global variables

#===============================================================================
# FUNCTIONS
#===============================================================================
def insComment(email, comment):
    '''
    Insert comment to database
    '''
    email = email.replace("'","")   # Clean data of quote marks
    email = email.replace('"','')
    comment = comment.replace("'","")
    comment = comment.replace("'","")
    db = lib01.get_settings()
    db_conn = pgdb.connect(**db[0])
    qry = "INSERT INTO "+db[2]+"(email, comment) VALUES ('"+email+"','"+comment+"')"
    pgins = db_conn.cursor()
    pgins.execute(qry)
    pgins.close()
    db_conn.commit()
    db_conn.close()    
    return


#===============================================================================
# MAIN
#===============================================================================
# Top of program, main code
ctrls = cgi.FieldStorage()
if 'your_email' in ctrls:
    email = ctrls['your_email'].value
    data = ctrls['your_text'].value
    insComment(email, data)
    html = lib01.getCommentsPage()
elif 'col1' in ctrls:
    html = lib01.getCommentsPage(1)
elif 'col2' in ctrls:
    html = lib01.getCommentsPage(2)
elif 'col2a' in ctrls:
    html = lib01.getCommentsPage(3)
else:
    html = lib01.getCommentsPage()

print('Content-type: text/html\n')
print(html)
