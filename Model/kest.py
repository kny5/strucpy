import numpy as np


def est_init(dict):
    y = 0
    lim = len(dict)
    for key in range(0,lim):
        x = max(dict[key].ve)
        if x > y:
            y = x
    kest = np.matlib.zeros(shape=(y + 1, y + 1))
    pcur = np.zeros(y + 1)
    return {"kest" : kest, "pcur" : pcur}


def kest_maker(dict__, est_init__):
    lim = 12
    for key in range(len(dict__)):
        ve = dict__[key].ve
        kebg = dict__[key].kebg
        # print("lim ",lim)
        for i in range(0, lim):  # vertical
            # print("lim ",lim)
            for j in range(0, lim):  # horizontal
                est_init__[ve[i], ve[j]] += kebg.item(i, j)
                #print(dict__[key])
                #print("[",i,"]","[",j,"]","valor: ",kebg.item(i, j))  # trace counter
    return est_init__


def pcur_maker(dict__, est_init__):
    lim = 12
    for key in range(len(dict__)):
        ve = dict__[key].ve
        pcur = dict__[key].pcur
        for i in range(0,lim):
            est_init__[ve[i]] += pcur[i]
    return est_init__