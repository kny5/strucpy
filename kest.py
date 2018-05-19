import numpy as np
from numpy import matlib

def kest_init(dict):
    y = 0
    for key in dict:
        x = dict[key].ve.max()
        if x > y:
            y = x
    kest = np.matlib.zeros(shape=(y + 1, y + 1))
    return kest

def kest_maker(dict, kest):
    lim = len(kebg)
    for key in dict:
        ve = dict[key].ve
        kebg = dict[key].KEBG
        #print("lim ",lim)
        for i in range(0,lim): #vertical
            #print("lim ",lim)
            for j in range(0,lim): #horizontal
                kest[ve[0, i], ve[0, j]] += kebg.item(i, j) + 0.1
                print(dict[key])
                print("[",i,"]","[",j,"]","valor: ",kebg.item(i, j)) #trace counter
    return kest




