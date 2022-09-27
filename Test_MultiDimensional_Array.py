from ctypes import sizeof
from operator import length_hint
import numpy as nmp
import string
import random


index = 0
x = [[" "]* 1 for i in range(18)]  
print(x)


total = 1000000
def GeneraParola():
    letters = string.ascii_letters + string.punctuation + string.digits
    frase = ''.join(random.choice(letters) for i in range(random.randint(3, 20)))
    #print(frase)
    return frase;

def ControllArray(arr, frase, length):
    result = 0
    for i in range(length):
        if(arr[i] == frase):
            result = 1
            break;
    return result
        
for i in range(total):
    frase = GeneraParola()
    
    if((ControllArray(x[length_hint(frase) -3], frase, len(x[length_hint(frase) -3]))) == 0 or len(x[length_hint(frase) -3]) == 1):
        (x[length_hint(frase) -3]).append(frase)
    else:
        i -= 1
    print(i)
    
f = open("test.txt", "w")
for i in range(18):
    for c in range(len(x[i])): 
        f.write(x[i][c] + "\n")


