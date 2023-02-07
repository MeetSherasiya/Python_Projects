from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("Beginners_projects/key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("Beginners_projects/key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password?\n")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('Beginners_projects/password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")
            print("User:", user, "| Password:",fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('Beginners_projects/password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() +"\n")



while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit?\n").lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")