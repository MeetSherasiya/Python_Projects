name = input("Type yur name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?\n").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim across:\n").lower()

    if answer == "swim":
        print("You swim across and were eaten by an alligator.")
        
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")

    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbley, do you want to cross it or head back (cross/back)?\n").lower()

    if answer == "back":
        print("You go back and lose.")
        
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)?\n").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You Win!")

        elif answer == "no":
            print("You ignore the stranger and they are affended and you lose.")

        else:
            print('Not a valid option. You lose.')

    else:
        print('Not a valid option. You lose.')

else :
    print('Not a valid option. You lose.')

print(f"Thank you for Tyring, {name}")