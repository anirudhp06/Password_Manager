from time import sleep
from os import path
from os import mkdir
from sys import exit
import os
import pass_gen
from pathlib import Path
from getpass import getpass
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
    master_pwd=getpass(prompt="Enter the password to proceed with script:")
    key=load_key()
    fer=Fernet(key)
    proceed(master_pwd,0)
else:
    print("New user DETECTED!")
    print("PLEASE REMEMBER THIS PASSWORD, WITHOUT THIS PASSWORD UR STORAGE IS LOST")
    master_pwd=getpass(prompt="Enter the MASTER PASSWORD:")
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
        mypath=Path("passwords.txt")
        if mypath.stat().st_size==0:
            print("You do not have any passwords stored currently...")
        else:    
            with open('passwords.txt', 'r') as f:
                for line in f.readlines():    
                    data = line.rstrip()
                    user, passw = data.split("|")
                    print("User:", user, "| Password:",
                        fer.decrypt(passw.encode()).decode())
    except cryptography.fernet.InvalidToken:
        print("Token has been changed or lost.")
    except FileNotFoundError:
        print("You do not have any passwords stored currently")

def add():
    choice=["yes","y"]
    decide=input("Do you want to generate random password?(Y/N)").lower()
    if decide in choice:
        name=input("Enter name of the account:")
        strength=int(input("Enter Length of password to be generated:"))
        pwd=pass_gen.gen(strength)
        print("Password generated for account {} is {}.".format(name,pwd))
        stopp=False
        while not stopp:
            do_you=input("Do you want to generate another password?(Y/N):").lower()
            if do_you=="y":
                strength_again=input("Do you want to modify the length of password?(Y/N):").lower()
                if strength_again == "Y":
                    strength=int(input("Enter length of password to be generated:"))
                    pwd=pass_gen.gen(strength)
                    print("New password:",pwd)
                else:
                    print("Generating password with length of previous selection({})".format(strength))
                    pwd=pass_gen.gen(strength)
                    print("New password:",pwd)
            else:
                print("Proceeding with currently generated password:{}".format(pwd))
                stopp=True
        try:
            with open('passwords.txt', 'a') as f:
                f.write("\n"+name + "|" + fer.encrypt(pwd.encode()).decode())
            print("Password Added")
        except cryptography.fernet.InvalidToken:
            print("Token has been changed or lost.")
    else:
        print("Will save the user given password.")
        name = input('Account Name: ')
        pwd = getpass(prompt="Password:")
        try:
            with open('passwords.txt', 'a') as f:
                f.write("\n"+name + "|" + fer.encrypt(pwd.encode()).decode())
            print("Password Added")
        except cryptography.fernet.InvalidToken:
            print("Token has been changed or lost.")

while True:
    mode = input(
        'Do you want to add new Password or view stored password?\n1."add"\n2."view"\n3."q" to exit ').lower()
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