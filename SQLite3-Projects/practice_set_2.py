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

def leftJoinOrders():
    c.execute('SELECT * FROM employees left join orders using (employeeID)')
def leftJoinCustomers():
    c.execute('SELECT * FROM customers left join orders using (customerID)')

def totalAmount():
    c.execute('SELECT customerID from orders where totalAmount > 100')

def customerAndEmployee():
    c.execute('SELECT * from orders where customerID == employeeID')

def ordersInUSA():
    c.execute('SELECT employeeName from employees where city = "USA" ')

def showCustomers():
    # c.execute('SELECT * FROM customers')
    getRows = c.fetchall()
    for row in getRows:
        print(row)

def showEmployees():
    # c.execute('SELECT * FROM employees')
    getRows = c.fetchall()
    for row in getRows:
        print(row)

def showOrders():
    # c.execute('SELECT * FROM orders')
    getRows = c.fetchall()
    for row in getRows:
        print(row)

def deleteTable():
    c.execute("DROP TABLE customers")
    # c.execute("DROP TABLE employees")
    # c.execute("DROP TABLE orders")


# deleteTable()
# createCustomers('Steve Liu', 'Nagasaki', 'Japan')
# createCustomers('Ram Pandey', 'Mumbai', 'India')
# createCustomers('Mayank Sing', 'Delhi', 'India')
# createCustomers('James Tang', 'Tokyo', 'Japan')
# createCustomers('William Johnson', 'San Jose', 'USA')
# createCustomers('Nick Nelson', 'San Francisco', 'USA')

# createEmployees('John Taylor', '2016-04-19', 'New York', 'USA')
# createEmployees('Bob Williams', '2017-08-25', 'Boston', 'USA')
# createEmployees('Anisha Iyer', '2012-04-11', 'Chennai', 'India')
# createEmployees('Raj Chawla', '2016-02-09', 'Bangalore', 'India')
# createEmployees('Mark Lee', '2017-04-11', 'Tokyo', 'Japan')

# createOrders(6,1,'2019-07-11', 110)
# createOrders(5,2,'2018-11-22', 85)
# createOrders(4,5,'2019-05-11', 98)
# createOrders(3,4,'2017-11-30', 45)
# createOrders(2,3,'2018-08-09', 150)

# alias()
# totalAmount()
# customerAndEmployee()
# ordersInUSA()
# # leftJoinOrders()
# # leftJoinCustomers()
# showCustomers()
# showEmployees()
# showOrders()

#Excercise 2
def createStudents(studentName, grade):
    c.execute("SELECT * FROM sqlite_schema WHERE type='table' AND name= 'students' ")

    if c.fetchone()== None:
        c.execute("CREATE TABLE students(studentID integer PRIMARY KEY AUTOINCREMENT, studentName text, grade integer)")

    c.execute("INSERT INTO students(studentName, grade) VALUES (?,?)", (studentName, grade))
    conn.commit()

def createBooks(bookName, pageCount):
    c.execute("SELECT * FROM sqlite_schema WHERE type='table' AND name= 'books' ")

    if c.fetchone()== None:
        c.execute("CREATE TABLE books(bookID integer PRIMARY KEY AUTOINCREMENT, bookName text, pageCount integer)")

    c.execute("INSERT INTO books(bookName, pageCount) VALUES (?,?)", (bookName, pageCount))
    conn.commit() 

def createBorrow_register(studentID, bookID, takenDate, returnedDate):
    c.execute("SELECT * FROM sqlite_schema WHERE type='table' AND name= 'borrow_register' ")

    if c.fetchone()== None:
        c.execute("CREATE TABLE borrow_register(borrowID integer PRIMARY KEY AUTOINCREMENT, studentID integer, bookID integer, takenDate date, returnedDate date, FOREIGN KEY (studentID) references students(studentID), FOREIGN KEY (bookID) references books(bookID))")

    c.execute("INSERT INTO borrow_register(studentID, bookID, takenDate, returnedDate) VALUES (?,?,?,?)", (studentID, bookID,takenDate, returnedDate))
    conn.commit() 

def pageCountNumber():
    c.execute('SELECT bookName from books where pageCount > 500')

def notReturnedBook():
    c.execute("SELECT studentID from borrow_register where returnedDate = '' ")
    c.execute('SELECT studentName from students where studentID = 1')
def checkOut():
    #ascending order of studentIDs
    c.execute('SELECT studentID from borrow_register ORDER BY studentID')

def leftJoinBooks():
    c.execute('SELECT * FROM books left join borrow_register using (bookID)')
    c.execute('SELECT bookName from borrow_register where studentID = 5')

def leftJoinStudents():
    c.execute('SELECT * FROM students left join borrow_register using (studentID)')
def borrowedBook(date1, date2): 
    
    c.execute('SELECT studentID from borrow_register where takenDate > ? and takenDate < ?', (date1, date2) )
    # c.execute('SELECT bookName from borrow_register where studentID = 5')
    # c.execute('SELECT bookName from borrow_register where studentID = 2')

def showStudents():
    # c.execute('SELECT * from students')
    getRows = c.fetchall()
    for rows in getRows:
        print(rows)
def showBooks():
    # c.execute('SELECT * from books')
    getRows = c.fetchall()
    for rows in getRows:
        print(rows)
def showBorrow_register():
    # c.execute('SELECT * from borrow_register')
    getRows = c.fetchall()
    for rows in getRows:
        print(rows)
def delete():
    c.execute('DROP TABLE students')
    c.execute('DROP TABLE books')
    c.execute('DROP TABLE borrow_register')

# delete()
# createStudents("tany Anand", 8)
# createStudents("ishita Reddy", 11)
# createStudents('Nick He', 7)
# createStudents("Mary Wang", 8)
# createStudents("Steve Liu", 5)

# createBooks("Hidden Alley", 300)
# createBooks("Purple Flower", 150)
# createBooks("Sheild of queens", 200)
# createBooks("The hollow snowman", 550)
# createBooks("the edge of atlas", 753)

# createBorrow_register(2,1,"2020-01-01", "2020-01-16")
# createBorrow_register(5,4,"2020-04-01", "2020-04-20")
# createBorrow_register(3,1,"2020-06-13", "2020-01-26")
# createBorrow_register(1,4, "2020-01-26", "")
# createBorrow_register(2,4,"2020-04-05", "2020-04-15")

# pageCountNumber()
# notReturnedBook()
# checkOut()
leftJoinBooks()
# leftJoinStudents()
# borrowedBook('2020-04-00', '2020-04-30')
showStudents()
showBooks()
showBorrow_register()