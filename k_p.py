import numpy as np
from numpy import matlib
# from datetime import datetime
import math
A = object.A()
B = object.B()
D_X = object.dx()
NU = object.nu
LM = object.lm
mzz = object.mzz()
myy = object.myy()
vzz = object.vzz()
vyy = object.vyy()
AXIAL = object.axial()
T = object.torsion()
area = object.area()
p_mat = object.p_mat
l = object.l
e = object.e
izz = object.izz()
wy = object.wy
wz = object.wz
aw = object.aw
iyy = object.iyy()
SCC = object.SCC
POISSON = object.POISSON


class calculations(object):
    def __init__(self, SCC):
        pass

    def k__(c):
        k = np.matlib.zeros(shape=((SCC + 1), (SCC + 1)))
        k[0, 0] = k[SCC, SCC] = 3
        k[1, 1] = k[SCC - 1, SCC - 1] = 7 + c
        k[1, 0] = k[1, 2] = k[SCC - 1, SCC] = k[SCC - 1, SCC - 2] = -4
        k[1, 3] = k[SCC - 1, SCC - 3] = 1
        for i in range(2, SCC - 1):
            k[i, i] = 6 + c
            k[i, i - 2] = k[i, i + 2] = 1
            k[i, i - 1] = k[i, i + 1] = -4
        return k

    kzz = k__(B)
    kyy = k__(A)

    def ft__(a, b, c, d):
        f = np.matlib.zeros(shape=(SCC + 1, 1))
        f[d, 0], f[SCC - d, 0] = c * a, c * b
        return f

    f1zz = ft__(3, 0, 1, 0)
    f2zz = ft__(0, 3, 1, 0)
    f1yy = ft__(3, 0, 1, 0)
    f2yy = ft__(0, 3, 1, 0)
    t_f1zz = ft__(D_X, 0, 2, 1)
    t_f2zz = ft__(0, D_X, 2, 1)
    t_f1yy = ft__(D_X, 0, 2, 1)
    t_f2yy = ft__(0, D_X, 2, 1)

    d1zz = kzz.I * f1zz
    d2zz = kzz.I * f2zz
    te1zz = kzz.I * t_f1zz
    te2zz = kzz.I * t_f2zz
    d1yy = kyy.I * f1yy
    d2yy = kyy.I * f2yy
    te1yy = kyy.I * t_f1yy
    te2yy = kyy.I * t_f2yy

    def im__(vector, *args):
        x = 0
        for array in args:
            x += (array[0] * vector[array[1]])
        return float(x)

    d1zz_n2 = im__(d1zz, [-1, 2], [8, 1], [-6, 0])
    d1zz_n1 = im__(d1zz, [1, 1])
    d1zz_p1 = im__(d1zz, [1, SCC - 1])
    d1zz_p2 = im__(d1zz, [8, SCC - 1], [- 1, SCC - 2])

    d2zz_n2 = im__(d2zz, [8, 1], [- 1, 2])
    d2zz_n1 = im__(d2zz, [1, 1])
    d2zz_p1 = im__(d2zz, [1, SCC - 1])
    d2zz_p2 = im__(d2zz, [-1, SCC - 2], [8, SCC - 1], [-6, SCC])

    te1zz_n2 = im__(te1zz, [-1, 2], [8, 1]) + (8 * D_X)
    te1zz_n1 = im__(te1zz, [1, 1]) + (2 * D_X)
    te1zz_p1 = im__(te1zz, [1, SCC - 1])
    te1zz_p2 = im__(te1zz, [8, SCC - 1], [-1, SCC - 2])

    te2zz_n2 = im__(te2zz, [8, 1], [-1, 2])
    te2zz_n1 = im__(te2zz, [1, 1])
    te2zz_p1 = im__(te2zz, [1, SCC - 1]) + (2 * D_X)
    te2zz_p2 = im__(te2zz, [-1, SCC - 2], [8, SCC - 1]) + (8 * D_X)

    d1yy_n2 = im__(d1yy, [-1, 2], [8, 1], [-6, 0])
    d1yy_n1 = im__(d1yy, [1, 1])
    d1yy_p1 = im__(d1yy, [1, SCC - 1])
    d1yy_p2 = im__(d1yy, [8, SCC - 1], [- 1, SCC - 2])

    d2yy_n2 = im__(d2yy, [8, 1], [- 1, 2])
    d2yy_n1 = im__(d2yy, [1, 1])
    d2yy_p1 = im__(d2yy, [1, SCC - 1])
    d2yy_p2 = im__(d2yy, [-1, SCC - 2], [8, SCC - 1], [-6, SCC])

    te1yy_n2 = im__(te1yy, [-1, 2], [8, 1]) + (8 * D_X)
    te1yy_n1 = im__(te1yy, [1, 1]) + (2 * D_X)
    te1yy_p1 = im__(te1yy, [1, SCC - 1])
    te1yy_p2 = im__(te1yy, [8, SCC - 1], [-1, SCC - 2])

    te2yy_n2 = im__(te2yy, [8, 1], [-1, 2])
    te2yy_n1 = im__(te2yy, [1, 1])
    te2yy_p1 = im__(te2yy, [1, SCC - 1]) + (2 * D_X)
    te2yy_p2 = im__(te2yy, [-1, SCC - 2], [8, SCC - 1]) + (8 * D_X)

    def extend__(vector, neg, pos):
        x = np.insert(vector, 0, neg)
        x = np.append(x, pos)
        return x

    extend__(d1zz, [d1zz_n2, d1zz_n1], [d1zz_p1, d1zz_p2])
    extend__(d2zz, [d2zz_n2, d2zz_n1], [d2zz_p1, d2zz_p2])
    extend__(te1zz, [te1zz_n2, te1zz_n1], [te1zz_p1, te1zz_p2])
    extend__(te2zz, [te2zz_n2, te2zz_n1], [te2zz_p1, te2zz_p2])

    extend__(d1yy, [d1yy_n2, d1yy_n1], [d1yy_p1, d1yy_p2])
    extend__(d2yy, [d2yy_n2, d2yy_n1], [d2yy_p1, d2yy_p2])
    extend__(te1yy, [te1yy_n2, te1yy_n1], [te1yy_p1, te1yy_p2])
    extend__(te2yy, [te2yy_n2, te2yy_n1], [te2yy_p1, te2yy_p2])

    def tmv__(vector, m__, v=False):
        x = np.matlib.zeros(shape=(SCC + 1, 1))
        y = 2
        if not v:
            sums = [[1, 1], [-2, 0], [1, -1]]
        else:
            sums = [[1, 2], [-2, 1], [2, -1], [-1, -2]]
        for i in x:
            for arr in sums:
                x[i] += arr[0] * vector[i + y + arr[1]]
        x = x * m__
        return x

    m1zz = tmv__(d1zz, mzz)
    m2zz = tmv__(d2zz, mzz)
    tm1zz = tmv__(te1zz, mzz)
    tm2zz = tmv__(te2zz, mzz)

    m1yy = tmv__(d1yy, myy)
    m2yy = tmv__(d2yy, myy)
    tm1yy = tmv__(te1yy, myy)
    tm2yy = tmv__(te2yy, myy)

    v1zz = tmv__(d1zz, vzz, v=True)
    v2zz = tmv__(d2zz, vzz, v=True)
    tv1zz = tmv__(te1zz, vzz, v=True)
    tv2zz = tmv__(te2zz, vzz, v=True)

    v1yy = tmv__(d1yy, vyy, v=True)
    v2yy = tmv__(d2yy, vyy, v=True)
    tv1yy = tmv__(te1yy, vyy, v=True)
    tv2yy = tmv__(te2yy, vyy, v=True)

    keb = np.matlib.zeros(shape=(12, 12))
    # region one
    keb[0, 0] = AXIAL
    keb[1, 1] = - v1zz[0]
    keb[1, 5] = - tv1zz[0]
    keb[2, 2] = - v1yy[0]
    keb[2, 4] = tv1yy[0]
    keb[3, 3] = T
    keb[4, 2] = - m1yy[0]
    keb[4, 4] = tm1yy[0]
    keb[5, 1] = m1zz[0]
    keb[5, 5] = tm1zz[0]
    # region two
    keb[6, 0] = - AXIAL
    keb[7, 1] = v1zz[SCC]
    keb[7, 5] = tv1zz[SCC]
    keb[8, 2] = v1yy[SCC]
    keb[8, 4] = - tv1yy[SCC]
    keb[9, 3] = - T
    keb[10, 2] = m1yy[SCC]
    keb[10, 4] = - tm1yy[SCC]
    keb[11, 1] = - m1zz[SCC]
    keb[11, 5] = - tm1zz[SCC]
    # region three
    keb[0, 6] = - AXIAL
    keb[1, 7] = - v2zz[0]
    keb[1, 11] = tv2zz[0]
    keb[2, 8] = - v2yy[0]
    keb[2, 10] = - tv2yy[0]
    keb[3, 9] = - T
    keb[4, 8] = - m2yy[0]
    keb[4, 10] = - tm2yy[0]
    keb[5, 7] = m2zz[0]
    keb[5, 11] = - tm2zz[0]
    # region four
    keb[6, 6] = AXIAL
    keb[7, 7] = v2zz[SCC]
    keb[7, 11] = - tv2zz[SCC]
    keb[8, 8] = v2yy[SCC]
    keb[8, 10] = tv2yy[SCC]
    keb[9, 9] = T
    keb[10, 8] = m2yy[SCC]
    keb[10, 10] = tm2yy[SCC]
    keb[11, 7] = - m2zz[SCC]
    keb[11, 11] = tm2zz[SCC]

    tr = np.matlib.zeros(shape=(12, 12))
    # rotational matrix
    a = math.cos(math.radians(NU))
    b = math.sin(math.radians(NU))
    c = math.cos(math.radians(LM))
    d = math.sin(math.radians(LM))
    # region one
    tr[0, 0] = a * c
    tr[0, 1] = - a * d
    tr[0, 2] = - b
    tr[1, 0] = d
    tr[1, 1] = c
    tr[2, 0] = b * c
    tr[2, 1] = - b * d
    tr[2, 2] = a
    tr[3, 3] = a * c
    tr[3, 4] = - a * d
    tr[3, 5] = - b
    tr[4, 3] = d
    tr[4, 4] = c
    tr[5, 3] = b * c
    tr[5, 4] = - b * d
    tr[5, 5] = a
    # region two
    tr[6, 6] = a * c
    tr[6, 7] = - a * d
    tr[6, 8] = - b
    tr[7, 6] = d
    tr[7, 7] = c
    tr[8, 6] = b * c
    tr[8, 7] = - b * d
    tr[8, 8] = a
    tr[9, 9] = a * c
    tr[9, 10] = - a * d
    tr[9, 11] = - b
    tr[10, 9] = d
    tr[10, 10] = c
    tr[11, 9] = b * c
    tr[11, 10] = - b * d
    tr[11, 11] = a

    kebg = np.dot(np.dot(tr, keb), tr.T)
