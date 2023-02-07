print("Welcome to my computer Quiz!")

playing = input("Do you want to play? ")
Correct = 0

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("Whats does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    Correct += 1
else :
    print('Incorrect!')

answer = input("What dose GPU stand for?  ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    Correct += 1
else :
    print('Incorrect!')

answer = input("Whats does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    Correct += 1
else :
    print('Incorrect!')

answer = input("Whats does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    Correct += 1
else :
    print('Incorrect!')

print(f"Your Score is {Correct} out of 4")