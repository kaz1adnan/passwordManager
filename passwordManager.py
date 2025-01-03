from cryptography.fernet import Fernet #fernet is a module used to generate keys

"""
def keyGenerator():
    key = Fernet.generate_key() #the key is generated here

    with open("key.key", "wb") as genKey: #A file to store key is generated / wb means to write in byte, its a special format
        genKey.write(key) #Generated key is stored there"""


def keyLoader():
    file = open("key.key", "rb")
    key = file.read()
    file.close()

    return key


masterPwd = input("Enter your master Password: ")
key = keyLoader() + masterPwd.encode()
fer = Fernet(key) #Encapsulates the key and allows use of functions like encrypt and decrypt

def view():
    with open("passwords.txt", "r") as pBase:
        for line in pBase.readlines(): #readlines() function reads every single line of the file
            data = line.rstrip() #due to "\n" an extra line is read, so rstrip removes the "\n"
            username, password = data.split("|")
            print("Username: " + username + ", Password: " + fer.decrypt(password.encode()).decode())

def add():
    userName = input("Enter username: ")
    userPass = input("Enter password: ")

    with open("passwords.txt", "a") as pBase: #with ensures that the file doesn't remain open after usage, open(file name, file format[a = write to the last if existing and read the whole and add a new file if doesn't exist]), the name after "as" is the name used to access the file
        pBase.write(userName + "|" + fer.encrypt(userPass.encode()).decode() + "\n") #fer.encrypt encrypts the password and encode() converts the password into bytes
        #decode() converts the encrypted password into a string
while True:
    userJourney = input("Would you like to view your old passwords or add a new one? (view/add/q): ").lower()
    if userJourney == "q":
        break

    if userJourney == "view":
        view()

    elif userJourney == "add":
        add()

    else:
        print("Invalid Input!")
        continue