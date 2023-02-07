import random


with open('Beginners_projects/Hangman/words.txt','r') as f:
        words = f.readlines()

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

word = random.choice(words)
word = word[:len(word)-1]
i = 0
print(HANGMAN_PICS[i])
total_chances = 6
guessed_word = "_"*(len(word))

while total_chances !=0:
    print(guessed_word+"\n")
    letter = input("Guess a letter: ").lower()
    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
                # print(guessed_word)
        if guessed_word == word:
            print("Congratulations you won!!!")
            break
    else:
        i += 1
        total_chances -= 1
        print(HANGMAN_PICS[i])
        print("Incorrect guess")
        print("The remaining chances are:",total_chances)
else:
    print("Game Over")
    print("You Lose")
    print("All the chances are exhausted")
print("The correct word is: " + word)