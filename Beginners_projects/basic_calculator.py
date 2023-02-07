def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))

def mul(a,b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer))

def div(a,b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))

print("A. Addition\nB. Subtraction\nC. Multiplication\nD. Division\nE. Exit")

while True:
    choice = input("Input your choice: ").lower()

    if choice=="a":
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add(a,b)

    elif choice=="b":
        print("Substraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub(a,b)

    elif choice=="c":
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mul(a,b)

    elif choice=="d":
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        div(a,b)

    elif choice=="e":
        print("Program end!")
        break

    else:
        print("Enter a valid choice!")