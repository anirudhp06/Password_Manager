from time import sleep
from os import path
from os import mkdir
from sys import exit
import os
try:
    from cryptography.fernet import Fernet
    import cryptography
except ModuleNotFoundError:
    print("'cryptography' module not found\nProgram will try to install automatically\nMake sure u have stable internet Connection")
    os.system('cmd /c "pip install cryptography"')
    print("Module Installed, Please restart the program (will exit in 10 seconds)")
    sleep(10)
    exit()
def write_key():
    key = Fernet.generate_key()
    try:
        mkdir("C:/Users/key_file/")
        with open("C:\\Users\key_file\key.key", "wb") as key_file:
            key_file.write(key)
    except:
        print("Please run the program as administrator and try again, Exiting program after 10 seconds")
        sleep(10)
        exit()

def load_key():
    file = open("C:\\Users\key_file\key.key", "rb")
    key = file.read()
    file.close()
    return key

def proceed(master_pwd,nw_usr):
    temp_pwd=""
    with open("C:\\Users\key_file\secret.txt","r") as f:
        for line in f.readlines():
            data=line
            temp_pwd=fer.decrypt(data.encode()).decode()
    if master_pwd == temp_pwd:
        pass
    else:
        print("Incorrect password,exiting in 10 seconds.")
        sleep(10)
        exit()
    if path.isfile("C:\\Users\key_file\key.key"):
        pass
if path.isfile("C:\\Users\key_file\secret.txt"):
    master_pwd=input("Enter master password to proceed:")
    key=load_key()
    fer=Fernet(key)
    proceed(master_pwd,0)
else:
    print("New user DETECTED!")
    print("PLEASE REMEMBER THIS PASSWORD, WITHOUT THIS PASSWORD UR STORAGE IS LOST")
    master_pwd=input("Enter new masterpassword to proceed:")
    print("IT IS RECOMMENDED TO WRITE DOWN MASTER PASSWORD IN A SAFE PLACE IN THE MEAN TIME.(will proceed after 15 seconds)")
    sleep(15)
    if path.isfile("C:\\Users\key_file\key.key"):
        pass
    else:
        write_key()
    key=load_key()
    fer=Fernet(key)
    with open("C:\\Users\key_file\secret.txt","a") as f:
        f.write(fer.encrypt(master_pwd.encode()).decode())
    proceed(master_pwd,1)

def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:", user, "| Password:",
                    fer.decrypt(passw.encode()).decode())
    except cryptography.fernet.InvalidToken:
        print("Token has been changed or lost.")


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    try:
        with open('passwords.txt', 'a') as f:
            f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    except cryptography.fernet.InvalidToken:
        print("Token has been changed or lost.")


while True:
    mode = input(
        "Do you want to add new Password or view stored password? (add,view) 'q' to exit ").lower()
    if mode == "q":
        print("Exiting program in 3 seconds")
        sleep(5)
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid option.")
        continue