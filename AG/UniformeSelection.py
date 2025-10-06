# uniforme selection
import numpy as np
import random as rnd

L=[]
def UniformeSelection(N):
    p=1/N
    for i in range(N):
        x = rnd.randint(0,1)
        index=(x//p)+1
        L.append(index)
    return L


I=UniformeSelection(6)
print(I)