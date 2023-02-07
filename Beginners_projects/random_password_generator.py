import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("Do you want to generate password? (Yes/No) ").lower()

if option == "yes":
    generate_password()
    
elif option == "no":
    print("Program Ended")
    quit()

else:
    print("Invalid input, please Enter Yes or No")
    quit()