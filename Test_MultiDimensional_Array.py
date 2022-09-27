from ctypes import sizeof
from operator import length_hint
import numpy as nmp
import string
import random

x = [[""]* 1] * 17 
print(x[1])
total = 100
def GeneraParola():
    letters = string.ascii_letters + string.punctuation + string.digits
    frase = ''.join(random.choice(letters) for i in range(random.randint(3, 20)))
    #print(frase)
    return frase;

#*def ControllArray(arr, i):
    #for i in range(arr[i]):
        #print("Hello")
        
for i in range(total):
    frase = GeneraParola()
    frase.join(x[length_hint(frase) -3])
    print(x[length_hint(frase) -3])
    #print(length_hint(frase) , " \n" , frase)
    #print(type(x[length_hint(frase) -3].shape))
    #x[length_hint(frase) -3].shape = tuple(int(str(x[length_hint(frase) -3].shape)) +1)
    #x[length_hint(frase)].shape = (x[length_hint(frase)].shape + 1)
    #print(x[length_hint(frase) - 3].shape, length_hint(frase))


