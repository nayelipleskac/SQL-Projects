import sqlite3

class Database:
    def __init__(self):
        self.time= 0
        self.bankID= None
    def createTable(self):
        pass
    def deleteRow(self):
        pass
    def updatePhoneNumber(self):
        pass
    def close(self):
        pass

class Bank(Database):
    def __init__(self):
        Database.__init__(self)
        self.cmd = None
    def interface(self):
        pass
    def run(self):
        print('run function')
    
 

class App:
    def __init__(self, database_file):
        self.bank = Bank()
        self.conn= sqlite3.connect(database_file)
        self.c = self.conn.cursor()
        self.bank.run()


if __name__ == '__main__':
    app = App('bank practice.db')
        