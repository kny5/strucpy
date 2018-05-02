import numpy as np
from numpy import matlib

def m_m(a, b):
    c = np.matlib.zeros(shape=(len(a), len(b)))
    #print(df(c))
    lim = len(c)
    #print("lim ",lim)
    for i in range(0,lim): #vertical
        #print("lim ",lim)
        for j in range(0,lim): #horizontal
            for k in range(0,lim):
                c[i,j] += a[i,k] * b[k,j]
                #print("[",i,"]","[",j,"]","[",k,"]") #trace counter
    #print(df(c))
    return c
