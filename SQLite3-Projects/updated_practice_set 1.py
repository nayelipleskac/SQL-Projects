import sqlite3

# c = conn.cursor()

class Database:
    def __init__(self, database_file):
        # self.firstName = 'Nayeli'
        # self.lastName = 'Pleskac'
        self.conn = sqlite3.connect(database_file)
        self.c = self.conn.cursor()
    def createTable(self, firstName, lastName, emailId, age, phoneNumber, city):
        self.c.execute("SELECT * FROM sqlite_schema WHERE type='table' AND name= 'users' ")
        if self.c.fetchone()== None: 
            self.c.execute('CREATE TABLE users(userId integer PRIMARY KEY AUTOINCREMENT, firstName text, lastName text, emailId text, age integer, phoneNumber text, city text)') 

        self.c.execute("INSERT INTO users(firstName, lastName, emailId, age, phoneNumber, city) VALUES (?,?,?,?,?,?)",(firstName, lastName, emailId, age, phoneNumber, city)) #inserts one row
        self.conn.commit()
        self.showTable()
    def close(self):
        #close db table
        self.conn.close()
        

    def deleteRow(self, firstName, lastName):
        query = 'DROP TABLE users'
        self.c.execute('DELETE FROM users WHERE firstName = ? and lastName = ?', (firstName, lastName))
        self.c.execute(query)
        self.conn.commit()
        # self.showTable()

    def updatePhoneNumber(self, phoneNumber, firstName):
        self.c.execute('UPDATE users SET phoneNumber = ? WHERE firstName = ?', (phoneNumber, firstName))
        self.conn.commit()
    

    def showTable(self):
        # print('in showtable')
        query = 'SELECT * FROM users'
        self.c.execute(query)
        records= self.c.fetchall()
        # getRows= c.fetchall()
        for row in records: 
            print(row)

if __name__ == '__main__':
    app = Database('updated practice1.db')
    print('choose an option:\n')
    print('A to delete')
    
    app.deleteRow('Nayeli', 'Pleskac')
    app.createTable('Nayeli', 'Pleskac', 'npleskac@gmail.com', 15, '545-482-9382', 'MH')
    app.updatePhoneNumber('545-482-1111', 'Nayeli')
    app.showTable()
    app.close()



