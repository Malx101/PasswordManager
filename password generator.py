import random
import os

clear = lambda: os.system('cls')
def generater():
    characters = 'abcdefghijklmnopqrstuvwuxyzABCDEFGJIJKLMNOPQRSTUVWUXYZ1234567890!$&*(^)'#Characters that make up the password
    loop = True
    fhan = open("PasswordManager.txt","a")#Opening the file for appending new apps to it

    while loop:
        password_len = int(input("Enter password length: "))
        password = ""

        for x in range(0, password_len):
            password_char = random.choice(characters)#Randomly choose a single character from the set
            password = password + password_char#Append it to the password variable

        print("Here is your password:", password)
        accepted = input("Like it? (y/n): ").lower()
        
        if accepted == 'y':
            break
        else:
            continue

    app = input("What is the password for: ").capitalize()
    app = app.replace(' ','')

    fhan.write(app + ' ' + password + '\n')
    fhan.close()
    print("Saved successfully")
    


#Search for the app to get the password
def retrieve(app):
    found = dict()
    found['name'] = ''
    found['password'] = ''

    fhan = open('PasswordManager.txt','r')

    for line in fhan:
        line = line.rstrip()#Remove the \n
        wrds = line.split()#Convert into a list
        if app in wrds[0]:
            found['name'] = wrds[0]
            found['password'] = wrds[1]
            return found
        else:
            continue
    
    return found

def manualSave(app,password):
    fhan = open('PasswordManager.txt','a')

    fhan.write(app + ' ' + password + '\n')
    fhan.close()
    print("Saved successfully")

def remove_password(app):
    pass

while 1:
    print("What do you want to do?")
    print("[1]. Generate Password")
    print("[2]. Retrieve password")
    print("[3]. Already Saved Password")
    choice = int(input("Choice==> "))
    
    if choice == 1:
        generater()
    elif choice == 2:
        app = input("Enter App: ").capitalize()
        app = app.replace(' ', '')
        print(retrieve(app))
    elif choice == 3:
        app = input("Enter App: ").capitalize()
        app = app.replace(' ', '')
        password = input("Enter password: ")
        manualSave(app,password)

    opt = input("Would you like to continue? (y/n): ").lower()

    if opt == 'y':
        clear()
        continue
    else:
        break
    
