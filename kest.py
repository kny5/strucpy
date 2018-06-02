import numpy as np


def kest_init(dict):
    y = 0
    lim = len(dict)
    for key in range(0,lim):
        x = max(dict[key].ve)
        if x > y:
            y = x
    kest = np.matlib.zeros(shape=(y + 1, y + 1))
    return kest


def kest_maker(dict__, kest):
    lim = 12
    for key in range(len(dict__)):
        ve = dict__[key].ve
        kebg = dict__[key].kebg
        # print("lim ",lim)
        for i in range(0, lim):  # vertical
            # print("lim ",lim)
            for j in range(0, lim):  # horizontal
                kest[ve[i], ve[j]] += kebg.item(i, j)
                #print(dict__[key])
                #print("[",i,"]","[",j,"]","valor: ",kebg.item(i, j))  # trace counter
    return kest
