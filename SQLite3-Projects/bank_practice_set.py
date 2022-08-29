import sqlite3

#self.tblname
#creating more than one table (users, .., ..)
#asking the user to select which table to view
#showTable --> accepts which tblname parameter 

class Database:
    def __init__(self, database_file):
        self.conn= sqlite3.connect(database_file)
        self.c = self.conn.cursor()
        self.time= 0
        self.bankID= None
        self.dbn = None #database name 
        self.tn = None #table name
    def createTable(self):
        self.c.execute("SELECT * FROM sqlite_schema WHERE type='table' AND name= 'users' ")
        if self.c.fetchone() == None: 
            self.c.execute('CREATE TABLE users(userId integer PRIMARY KEY AUTOINCREMENT, firstName text, lastName text, emailId text, age integer, phoneNumber text, city text)') 
        print('table has been created')
        # self.c.execute("INSERT INTO users(firstName, lastName, emailId, age, phoneNumber, city) VALUES (?,?,?,?,?,?)",(firstName, lastName, emailID, age, phoneNumber, city)) #inserts one row
        self.conn.commit()
    def insertRow(self, firstName, lastName, emailID, age, phoneNumber, city):
        self.c.execute("INSERT INTO users(firstName, lastName, emailId, age, phoneNumber, city) VALUES (?,?,?,?,?,?)",(firstName, lastName, emailID, age, phoneNumber, city)) #inserts one row
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
        # print('a) create first row in table')
        # print('b) edit new table')
        # print('c) insert into table')
        # # self.showTable()
        print('a) select from a table')
        print('b) select from databases')
        print('c) create new table')
        print('d) edit new table')
        self.cmd = input('\n>: ')
    def run(self):
        while True: 
            self.interface()
            if self.cmd == 'a':
                print('table name: ')
                self.tn = input('>: ')
                q = "SELECT * FROM " + self.tn
                print(q)
                records= self.c.fetchall()
                for row in records: 
                    print(row,'\n')
                self.c.execute("SELECT * FROM " + self.tn)
                        
                # firstNameInput = input('first name: ')
                # lastNameInput = input('last name: ')
                # emailInput = input('email: ')
                # ageInput = input('age: ')
                # phoneInput = input('phone #: ')
                # cityInput = input('city: ')
                # if firstNameInput or lastNameInput or emailInput or phoneInput or cityInput == '':
                #     print('\n--enter in valid information--\n')
                # else:
                # self.createTable(firstNameInput, lastNameInput, emailInput, ageInput, phoneInput, cityInput)
                # self.showTable()
            if self.cmd == 'b':
                print('enter database name: ')
                self.db = input('>: ')
                q = self.db + '.db'
                self.c.execute('.tables')
                #print out table names in database


                # print('c) delete row')
                # print('d) update phone number')
                # print('e) close database')
                # self.cmd = input(':> ')
                # if self.cmd == 'c':
                #     firstNameInput = input('first name: ')
                #     lastNameInput = input('last name: ')
                #     # if firstNameInput or lastNameInput == '':
                #     #     print('\n--enter in valid infomation--\n')
                #     # else:
                #     self.deleteRow(firstNameInput, lastNameInput)
                #     self.showTable()
                # if self.cmd == 'd':
                #     updatedPhoneInput = input('phone number: ')
                #     firstNameInput = input('first name: ')
                #     lastNameInput = input('last name: ')
                #     # if firstNameInput or lastNameInput == '':
                #     #     print('\n--enter in valid information--\n')
                #     # else:    
                #     self.updatePhoneNumber(updatedPhoneInput, firstNameInput, lastNameInput)
                #     self.showTable()
                # if self.cmd == 'e':
                #     self.close()
                #     print('closing database')
                #     break
            if self.cmd == 'c':
                firstNameInput = input('first name: ')
                lastNameInput = input('last name: ')
                emailInput = input('email: ')
                ageInput = input('age: ')
                phoneInput = input('phone #: ')
                cityInput = input('city: ')
                self.insertRow(firstNameInput, lastNameInput, emailInput, ageInput, phoneInput, cityInput)
                self.showTable()
            elif self.cmd != 'a':
                print('choose a or b to start')

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
    # database = Database('updated bank practice.db')
    app = App('updatedbankpractice.db')
    #change file to database name
        