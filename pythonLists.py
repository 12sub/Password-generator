#Create a lists of password guesses and store it in a file

import random
import string
import inspect
from itertools import product
from timeit import repeat

def passwordGenerator(size):
    #process = product()
    for passcodes in range(100):
        passcodes = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
        print(passcodes)
        
        



# codes = print(str(passwords))

# passwords = list_password.append(passwords)

def storeFiles(filed):
    with open("will.txt", "w") as file:
        file.write(filed)
    def __str__(self):
        return self.file
    return storeFiles

def readFiles():
    with open("will.txt", "r") as file:
        file.readlines()
    def __str__():
        return file   
    return readFiles
    
    
# passwords = passwordGenerator(10)
# generatedPasswords = str(passwords)

print(readFiles().__str__())

# files = storeFiles(generatedPasswords)
# print(files.__str__())