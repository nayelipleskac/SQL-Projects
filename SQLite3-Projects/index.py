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
    c.close()
    conn.close()
    

def login(userNameInput, passwordInput):
    
    
    c.execute('SELECT * FROM signUpUser WHERE userName = ? and password = ?', (userNameInput, passwordInput)) 
    rows = c.fetchall()
    for r in rows:
        print(r)
        print('welcome ', r[0])
    else:
        print('record not found')

def deleteAccount(userNameInput, passwordInput):
    c.execute('DELETE FROM signUpUser WHERE userName = ? and password = ?', (userNameInput, passwordInput))
    rows = c.fetchall()
     
    print('record found and deleted')
def resetPassword(userNameInput, passwordInput):
    
   

      

    

    # if c.fetchone()[0] == 1:
    #     pass
    # else:
    #     print('sorry, try again')
        # userNameInput = input('enter your username: ')
        # passwordInput = input('enter your password: ')



print('Login Menu')
print('1. Signup')
print('2. Login')
print('3. Delete Account')

userInput = input('Enter your choice (1/2/3): ')

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
elif userInput == '2':
    print('Enter your login info:')
    userNameInput = input('enter your username: ')
    passwordInput = input('enter your password: ')
    login(userNameInput, passwordInput)
elif userInput == '3':
    findUserName = input('enter your username to delete: ')
    findPassword = input('enter your password to delete: ')
    deleteAccount(findUserName, findPassword)
else:
    print('enter 1 or 2 to signup/login')


