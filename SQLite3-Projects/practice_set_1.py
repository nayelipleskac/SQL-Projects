#Practice Set 1

import sqlite3
conn = sqlite3.connect('myDatabase.db')
c = conn.cursor()

def createTable(firstName, lastName, emailId, age, phoneNumber, city):
    c.execute(" SELECT count(firstName) FROM sqlite_master WHERE type='table' AND name='users' ")

    #if the count is 1, then table exists
    if c.fetchone()[0]==1 : {
	print('Table exists.')
    } 
    else:
        c.execute('CREATE TABLE users(userId integer PRIMARY KEY AUTOINCREMENT, firstName text, lastName text, emailId text, age integer, phoneNumber text, city text)') 

    c.execute("INSERT INTO user(firstName, lastName, emailId, age, phoneNumber, city) VALUES (?,?,?)",(firstName, lastName, emailId, age, phoneNumber, city)) #inserts one row
    conn.commit()

    print('CREATION OF TABLE AND INSERT SUCCESSFUL')

def showTable():
    c.execute('SELECT * FROM signUpUser')
    getRows =c.fetchall()
    for row in getRows: 
        print(row)