#Practice Set 1
#Part 1

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
    showTable()

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
# alphabeticalNames()

# showTable()

#Part 2

def createTable(firstName, lastName, joinDate, ordersTaken, country):
    c.execute("SELECT * FROM sqlite_schema WHERE type='table' AND name= 'employee' ")

    if c.fetchone()== None: 
        c.execute('CREATE TABLE employee(employeeId integer PRIMARY KEY AUTOINCREMENT, firstName text, lastName text, joinDate date, ordersTaken integer, country text)') 

    c.execute("INSERT INTO employee(firstName, lastName, joinDate, ordersTaken, country) VALUES (?,?,?,?,?)",(firstName, lastName, joinDate, ordersTaken,  country)) 
    conn.commit()

    print('CREATION OF TABLE AND INSERT SUCCESSFUL')

def totalOrders():
    c.execute("SELECT SUM(ordersTaken) FROM employee ")

def groupByCountry():
    c.execute('SELECT * FROM employee GROUP BY country')

def experience():
    c.execute('SELECT * from employee order by joinDate')

def comparision(date1, date2):
    c.execute("SELECT firstName, lastName from employee where joinDate > ? and joinDate < ?", (date1, date2))

def likeNames():
    c.execute("SELECT lastName FROM employee WHERE lastName LIKE 's%'")

def count(startDate):
    c.execute("SELECT COUNT(firstName) from employee where joinDate > ?", (startDate,))

def country():
    c.execute('SELECT firstName, lastName from employee where country = "USA" or country = "Russia"')

def maxOrders():
    c.execute('SELECT MAX(ordersTaken) from employee')

def showTable():
    print('in showTable')
    c.execute("SELECT * FROM employee") #only use for createTable
    # getRows = c.fetchall()
    # for row in getRows:
    #     print(row)

def deleteTable():
    c.execute("DROP TABLE employee")

createTable('Tony', 'Stark', '2017-05-21', 870, 'USA')
createTable('Natasha', 'Romanolf', '2018-06-08', 350, 'Russia')
createTable('Thor', 'Odinson', '2019-01-04', 3000, 'Asgard')
createTable('Steve', 'Rogers', '2013-03-24', 3500, 'USA')
createTable('Perer', 'Parker', '2018-01-04',470, 'India')
totalOrders()
# groupByCountry()
# experience()
# comparision('2017-01-01', '2019-01-01')
# likeNames()
# count('2015-01-01')
# country()
# maxOrders()

showTable()





