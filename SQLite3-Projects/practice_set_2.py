#Practice Set 2
#Part 1

import sqlite3
conn = sqlite3.connect('practice2.db')
c = conn.cursor()

def createCustomers(customerName, city, country):
    c.execute("SELECT * FROM sqlite_schema WHERE type='table' AND name= 'customers' ")

    if c.fetchone()== None:
        c.execute("CREATE TABLE customers(customerID integer PRIMARY KEY AUTOINCREMENT, customerName text, city text, country text)")

    c.execute("INSERT INTO customers(customerName, city, country) VALUES (?,?,?)", (customerName, city, country))
    conn.commit() 


def createEmployees(employeeName, joinDate, city, country):
    c.execute("SELECT * FROM sqlite_schema WHERE type='table' AND name= 'employees' ")

    if c.fetchone()== None:
        c.execute("CREATE TABLE employees(employeeID integer PRIMARY KEY AUTOINCREMENT, employeeName text, joinDate date, city text, country text)")

    c.execute("INSERT INTO employees(employeeName, joinDate, city, country) VALUES (?,?,?,?)", (employeeName, joinDate, city, country))
    conn.commit()

def createOrders(customerID, employeeID, orderDate, totalAmount):
    c.execute("SELECT * FROM sqlite_schema WHERE type='table' AND name= 'orders' ")

    if c.fetchone()== None:
        c.execute('PRAGMA foreign_keys = on')
        c.execute("CREATE TABLE orders(orderID integer PRIMARY KEY AUTOINCREMENT, customerID integer, employeeID integer, orderDate date, totalAmount integer, FOREIGN KEY (customerID) references customers(customerID), FOREIGN KEY (employeeID) references employees(employeeID))")

    c.execute("INSERT INTO orders(customerID, employeeID, orderDate, totalAmount) VALUES (?,?,?,?)", (customerID, employeeID, orderDate, totalAmount))
    conn.commit()

def alias():
    c.execute('SELECT c.customerID FROM customers AS c')
    c.execute('SELECT o.orderID FROM orders AS o')
    c.execute('SELECT * FROM o ')


def showCustomers():
    c.execute('SELECT * FROM customers')
    getRows = c.fetchall()
    for row in getRows:
        print(row)

def showEmployees():
    c.execute('SELECT * FROM employees')
    getRows = c.fetchall()
    for row in getRows:
        print(row)

def showOrders():
    c.execute('SELECT * FROM orders')
    getRows = c.fetchall()
    for row in getRows:
        print(row)

def deleteTable():
    c.execute("DROP TABLE customers")
    c.execute("DROP TABLE employees")
    # c.execute("DROP TABLE orders")


# deleteTable()
# createCustomers('Steve Liu', 'Nagasaki', 'Japan')
# createCustomers('Ram Pandey', 'Mumbai', 'India')
# createCustomers('Mayank Sing', 'Delhi', 'India')
# createCustomers('James Tang', 'Tokyo', 'Japan')
# createCustomers('William Johnson', 'San Jose', 'USA')
# createCustomers('Nick Nelson', 'San Francisco', 'USA')
# print('-----------')
# createEmployees('John Taylor', '2016-04-19', 'New York', 'USA')
# createEmployees('Bob Williams', '2017-08-25', 'Boston', 'USA')
# createEmployees('Anisha Iyer', '2012-04-11', 'Chennai', 'India')
# createEmployees('Raj Chawla', '2016-02-09', 'Bangalore', 'India')
# createEmployees('Mark Lee', '2017-04-11', 'Tokyo', 'Japan')
# print('----------')
# createOrders(6,1,'2019-07-11', 110)
# createOrders(5,2,'2018-11-22', 85)
# createOrders(4,5,'2019-05-11', 98)
# createOrders(3,4,'2017-11-30', 45)
# createOrders(2,3,'2018-08-09', 150)
# print('----------')

alias()
showCustomers()
showEmployees()
showOrders()


