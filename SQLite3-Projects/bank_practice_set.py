import sqlite3

class Database:
    def __init__(self, database_file):
        self.conn= sqlite3.connect(database_file)
        self.c = self.conn.cursor()
        self.time= 0
        self.bankID= None
        self.dbn = None #database name 
        self.tn = None #table name
    def createTable(self):
        if self.c.fetchone() == None: 
            self.c.execute('''CREATE TABLE {}(userId integer PRIMARY KEY AUTOINCREMENT, firstName text, lastName text, emailId text, age integer, phoneNumber text, city text)'''.format(self.tn))
        print('table has been created')

        self.conn.commit()
        
    def insertRow(self, firstName, lastName, emailID, age, phoneNumber, city):
        self.c.execute("INSERT INTO {}(firstName, lastName, emailId, age, phoneNumber, city) VALUES (?,?,?,?,?,?)".format(self.tn),(firstName, lastName, emailID, age, phoneNumber, city)) #inserts one row
        self.conn.commit()
    def deleteRow(self, firstName, lastName):
        query = 'SELECT * FROM users'
        query2 = 'DROP TABLE users'
        self.c.execute(query)
        records= self.c.fetchall()
        for row in records: 
            if firstName or lastName not in records:
                print('Either name entered is not found')
        self.c.execute('DELETE FROM users WHERE firstName = ? and lastName = ?', (firstName, lastName))
        
        if self.c.fetchone() == None:
            print('user has been deleted')
        self.conn.commit()
    def updatePhoneNumber(self, phoneNumber, firstName, lastName):
        query = 'SELECT * FROM users'
        self.c.execute(query)
        records= self.c.fetchall()
        if type(phoneNumber) == int:
            self.c.execute('UPDATE users SET phoneNumber = ? WHERE firstName = ? and lastName = ?', (phoneNumber, firstName, lastName))
            self.conn.commit()
        elif type(phoneNumber) != int: 
            print('Enter a valid phone number')

        for row in records: 
            if firstName not in records:
                print('first name entered is not found')
            
        
    def close(self):
        self.conn.close()

class Bank(Database):
    def __init__(self):
        Database.__init__(self, 'updatedbankpractice.db')
        self.cmd = None
    def interface(self):
        print('a) select from a table')
        print('b) select from databases')
        print('c) create new table')
        print('d) insert into table')
        self.cmd = input('\n>: ')
    def run(self):
        while True: 
            self.interface()
            if self.cmd == 'a':
                print('table name: ')
                self.tn = input('>: ')
                q = "SELECT * FROM " + self.tn + ";"
                self.c.execute(q)
                records= self.c.fetchall()
                for row in records: 
                    print(row,'\n')

            if self.cmd == 'b':
                print('enter database name')
                self.db = input('>: ')
                q = self.db + '.db'  
                sql_query = """SELECT name FROM sqlite_master WHERE type = 'table'"""
                # sql_query= """SELECT name from sys.Databases WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb')"""
                self.c.execute(sql_query)
                print('List of tables\n')
                print(self.c.fetchall())
                self.close()

            if self.cmd == 'c':
                self.tn = input('table name: ')
                firstNameInput = input('first name: ')
                lastNameInput = input('last name: ')
                emailInput = input('email: ')
                ageInput = input('age: ')
                phoneInput = input('phone #: ')
                cityInput = input('city: ')
                if firstNameInput=='' or lastNameInput=='' or emailInput=='' or ageInput=='' or phoneInput==''or cityInput == '':
                    print('\n--enter in valid information--\n')
                self.createTable(firstNameInput, lastNameInput, emailInput, ageInput, phoneInput, cityInput)
                q= 'SELECT * FROM ' + self.tn + ';'
                self.c.execute(q)
                records= self.c.fetchall()
                for row in records: 
                    print(row,'\n')

            if self.cmd == 'd':
                self.tn = input('table name: ')
                firstNameInput = input('first name: ')
                lastNameInput = input('last name: ')
                emailInput = input('email: ')
                ageInput = input('age: ')
                phoneInput = input('phone #: ')
                cityInput = input('city: ')
                if firstNameInput=='' or lastNameInput=='' or emailInput=='' or ageInput=='' or phoneInput==''or cityInput == '':
                    print('\n--enter in valid information--\n')
                self.insertRow(firstNameInput, lastNameInput, emailInput, ageInput, phoneInput, cityInput)

            elif self.cmd != 'a' or self.cmd != 'b' or self.cmd != 'c' or self.cmd != 'd':
                print('choose a-d to start')

    def showTable(self):
        query = 'SELECT * FROM users'
        query2 = 'PRAGMA table_info(users)'
        self.c.execute(query)
        records= self.c.fetchall()
        # getRows= c.fetchall()
        for row in records: 
            print(row,'\n')
class App:
    def __init__(self, database_file):
        self.bank = Bank()
        self.conn= sqlite3.connect(database_file)
        self.c = self.conn.cursor()
        self.bank.run()


if __name__ == '__main__':
    app = App('updatedbankpractice.db')
    #change file to database name
        