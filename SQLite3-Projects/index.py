import sqlite3
conn = sqlite3.connect('myDatabase.db')
c = conn.cursor()

def signup(nameOfUser, userNameInput, passwordInput):
    
    c.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='signUpUser' ")

    #if the count is 1, then table exists
    if c.fetchone()[0]==1 : {
	print('Table exists.')
    } 
    else:
        c.execute('CREATE TABLE signUpUser(name text, userName text, password text)') #creates table signUpUser

    c.execute("INSERT INTO signUpUser(name, userName, password) VALUES (?,?,?)",(nameOfUser, userNameInput, passwordInput)) #inserts one row
    conn.commit()

    print('SIGN UP SUCCESSFUL')
    print(nameOfUser, userNameInput, passwordInput)
    
    

def login(userNameInput, passwordInput):
    
    c.execute('SELECT * FROM signUpUser WHERE userName = ? and password = ?', (userNameInput, passwordInput)) #verifies userName / password in signUpUser
    
    rows = c.fetchall()
    print(rows)

    for r in rows:
        print(r)
        print('welcome ', r[0])
    else:
        print('record not found')
    

def deleteAccount(userNameInput, passwordInput):
    c.execute('DELETE FROM signUpUser WHERE userName = ? and password = ?', (userNameInput, passwordInput))
    conn.commit()

    rows = c.fetchall()
    print(rows)

    print('record found and deleted')


def resetPassword(userNameInput, newPasswordInput):
    c.execute('UPDATE signUpUser SET password = ? WHERE userName = ?', (newPasswordInput, userNameInput))
    conn.commit()

    rows = c.fetchall()
    for r in rows:
        print(r)
        print('passwored reset!')
 

def showTable():
    c.execute('SELECT * FROM signUpUser')
    getRows =c.fetchall()
    for row in getRows: 
        print(row)


print('Login Menu')
print('1. Signup')
print('2. Login')
print('3. Delete Account')
print('4. Reset Password')

userInput = input('Enter your choice (1/2/3/4): ')

if userInput == '1':
    print('Sign-up page: ')
    nameInput = input('enter your name: ')
    userNameInput = input('enter your username: ')
    passwordInput = input('enter your password: ')
    confirmPassword = input('confirm Password: ')
    if passwordInput != confirmPassword:
        print('passwords do not match!')
    else:
        signup(nameInput, userNameInput, passwordInput)
        showTable()
       
elif userInput == '2':
    userNameInput = input('enter your username: ')
    passwordInput = input('enter your password: ')
    login(userNameInput, passwordInput)
    showTable()
 
elif userInput == '3':
    userNameInput = input('enter your username to delete: ')
    passwordInput = input('enter your password to delete: ')
    deleteAccount(userNameInput, passwordInput)
    showTable()
elif userInput == '4':
    userNameInput = input('enter your username: ')
    newPasswordInput = input('enter your new password: ')
    resetPassword(userNameInput, newPasswordInput)
    showTable()
else:
    print('enter 1/2/3/4')

c.close()
conn.close()


