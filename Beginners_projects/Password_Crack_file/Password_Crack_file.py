from string import *
from itertools import product

value = ascii_letters + digits + punctuation

for i in range(1,4):
    for j in product(value, repeat = i):
        word = "".join(j)
        p = open("Beginners_projects/Password_Crack_file/password.txt","a")
        p.write(word + "\n")