import numpy as np

def kest_init(dict):
    y = 0
    for key in dict:
        x = dict[key].ve.max()
        if x > y:
            y = x
    kest = np.matlib.zeros(shape=(y + 1, y + 1))
    return kest


def kest_maker(dict__, kest):
    lim = len(kebg)
    for key in dict__:
        ve = dict__[key].ve
        kebg = dict__[key].KEBG
        # print("lim ",lim)
        for i in range(0, lim):  # vertical
            # print("lim ",lim)
            for j in range(0, lim):  # horizontal
                kest[ve[0, i], ve[0, j]] += kebg.item(i, j) + 0.1
                print(dict__[key])
                print("[",i,"]","[",j,"]","valor: ",kebg.item(i, j))  # trace counter
    return kest

