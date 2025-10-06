import numpy as np
import random as rnd
L=[5,17,8,20,38,12]


def countPi(L):
    C=0
    for i in L:
        C+=i
    Lp = []
    for j in range(len(L)):
        Lp.append((L[j]/C)*len(L))
    return Lp

def RankSelection(L):
    Lp = countPi(L)
    res=[]
    #pick major
    for i in range(len(Lp)):
        x = int(Lp[i])
        for j in range(x):
            res.append(i+1)
        y=Lp[i]
        Lp[i]=y-x

    for i in range(len(Lp)):
        ran = rnd.randint(0,1)
        if ran<Lp[i]:
            res.append(i)
    return res

Res = RankSelection(L)
print(Res)