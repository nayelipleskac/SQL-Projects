#Practice Set 1

import sqlite3
conn = sqlite3.connect('practice1.db')
c = conn.cursor()

def createTable(firstName, lastName, emailId, age, phoneNumber, city):


    c.execute("SELECT * FROM sqlite_schema WHERE type='table' AND name= 'users' ")

    if c.fetchone()== None: 
        c.execute('CREATE TABLE users(userId integer PRIMARY KEY AUTOINCREMENT, firstName text, lastName text, emailId text, age integer, phoneNumber text, city text)') 

    c.execute("INSERT INTO users(firstName, lastName, emailId, age, phoneNumber, city) VALUES (?,?,?,?,?,?)",(firstName, lastName, emailId, age, phoneNumber, city)) #inserts one row
    conn.commit()

    print('CREATION OF TABLE AND INSERT SUCCESSFUL')

def updatePhoneNumber(phoneNumber, firstName):
    c.execute('UPDATE users SET phoneNumber = ? WHERE firstName = ?', (phoneNumber, firstName))
    conn.commit()
def delete(firstName, lastName):
    c.execute('DELETE FROM users WHERE firstName = ? and lastName = ?', (firstName, lastName))
    conn.commit()

def details(age, city):
    #select * from users where age > 25 and city = 'Boston'
    c.execute("SELECT * FROM users WHERE age > ? and city = ? ", (age, city))
    getRows = c.fetchall()
    for row in getRows:
        print(row)

def moreDets(city1, city2):
    c.execute("SELECT firstName, emailId FROM users WHERE city = ? or city = ? ", (city1, city2))
    getRows = c.fetchall()
    for row in getRows:
        print(row)

def minimumAge():
    c.execute("SELECT MIN(age) FROM users")

def descending():
    c.execute("SELECT age FROM users ORDER BY age DESC ")

def avg():
    c.execute("SELECT AVG(age) from users")

def alphabeticalNames():
    c.execute("SELECT userId, firstName, lastName, age FROM users ORDER BY firstName")


def showTable():
    # c.execute('SELECT * FROM users')
    getRows= c.fetchall()
    for row in getRows: 
        print(row)

# createTable('Joe', 'Smith', 'joesmith@gmail.com', 23, '4015689008', 'SF')
# createTable('Peter', 'Parker', 'peter@gmail.com', 19, '6002359599', 'NY')
# createTable('Ross', 'Cook', 'ross@gmail.com', 27, '7888453737', 'NY')
# createTable('Janel', 'Brown', 'janel@gmail.com', 35, '2323235566', 'Boston')
# createTable('Tony', 'Stark', 'tony@gmail.com', 40, '5454829382', 'Boston')
# updatePhoneNumber('40547475588', 'Ross')
# delete('Joe', 'Smith')
# details(25, 'Boston')
# moreDets('NY', 'Boston')
# minimumAge()
# descending()
# avg()
alphabeticalNames()

showTable()