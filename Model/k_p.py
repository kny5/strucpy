import numpy as np
from numpy import matlib
import math

def calculations(object, SCC, POISSON):
    dx = object.l / SCC
    nu = object.nu
    lm = object.lm
    A = (object.kv * object.a1() * dx ** 4) / (1000 * object.e * object.izz())
    B = (object.kh * object.a2() * dx ** 4) / (1000 * object.e * object.iyy())
    mzz = (object.e * object.izz()) / dx ** 2
    myy = (object.e * object.iyy()) / dx ** 2
    vzz = (object.e * object.izz()) / (2 * dx ** 3)
    vyy = (object.e * object.iyy()) / (2 * dx ** 3)
    axial = (object.e * object.area()) / object.l
    torsion = ((object.e / (2 * (1 + POISSON))) * object.j()) / object.l
    p_mat = object.p_mat
    wy = object.wy
    wz = object.wz
    aw = object.aw

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
        f = np.zeros(SCC + 1)
        f[d], f[SCC - d] = c * a, c * b
        return f

    f1zz = ft__(3, 0, 1, 0)
    f2zz = ft__(0, 3, 1, 0)
    f1yy = ft__(3, 0, 1, 0)
    f2yy = ft__(0, 3, 1, 0)
    t_f1zz = ft__(dx, 0, 2, 1)
    t_f2zz = ft__(0, dx, 2, 1)
    t_f1yy = ft__(dx, 0, 2, 1)
    t_f2yy = ft__(0, dx, 2, 1)

    d1zz = np.asarray(np.dot(kzz.I, f1zz)).reshape(-1) * -1
    d2zz = np.asarray(np.dot(kzz.I, f2zz)).reshape(-1) * -1
    te1zz = np.asarray(np.dot(kzz.I, t_f1zz)).reshape(-1) * -1
    te2zz = np.asarray(np.dot(kzz.I, t_f2zz)).reshape(-1) * -1
    d1yy = np.asarray(np.dot(kyy.I, f1yy)).reshape(-1) * -1
    d2yy = np.asarray(np.dot(kyy.I, f2yy)).reshape(-1) * -1
    te1yy = np.asarray(np.dot(kyy.I, t_f1yy)).reshape(-1) * -1
    te2yy = np.asarray(np.dot(kyy.I, t_f2yy)).reshape(-1) * -1

    def im__(vector, *args):
        x = 0
        for array in args:
            x += (array[0] * vector[array[1]])
        return x

    d1zz_n1 = im__(d1zz, (1, 1))
    d1zz_n2 = im__(d1zz, (-1, 2), (8, 1), (-6, 0))
    d1zz_p1 = im__(d1zz, (1, SCC - 1))
    d1zz_p2 = im__(d1zz, (8, SCC - 1), (- 1, SCC - 2))

    d2zz_n2 = im__(d2zz, (8, 1), (- 1, 2))
    d2zz_n1 = im__(d2zz, (1, 1))
    d2zz_p1 = im__(d2zz, (1, SCC - 1))
    d2zz_p2 = im__(d2zz, (-1, SCC - 2), (8, SCC - 1), (-6, SCC))

    te1zz_n2 = im__(te1zz, (-1, 2), (8, 1)) + (8 * dx)
    te1zz_n1 = (2 * dx) + im__(te1zz, (1, 1))
    te1zz_p1 = im__(te1zz, (1, SCC - 1))
    te1zz_p2 = im__(te1zz, (8, SCC - 1), (-1, SCC - 2))

    te2zz_n2 = im__(te2zz, (8, 1), (-1, 2))
    te2zz_n1 = im__(te2zz, (1, 1))
    te2zz_p1 = (2 * dx) + im__(te2zz, (1, SCC - 1))
    te2zz_p2 = im__(te2zz, (-1, SCC - 2), (8, SCC - 1)) + (8 * dx)

    d1yy_n2 = im__(d1yy, (-1, 2), (8, 1), (-6, 0))
    d1yy_n1 = im__(d1yy, (1, 1))
    d1yy_p1 = im__(d1yy, (1, SCC - 1))
    d1yy_p2 = im__(d1yy, (8, SCC - 1), (- 1, SCC - 2))

    d2yy_n2 = im__(d2yy, (8, 1), (- 1, 2))
    d2yy_n1 = im__(d2yy, (1, 1))
    d2yy_p1 = im__(d2yy, (1, SCC - 1))
    d2yy_p2 = im__(d2yy, (-1, SCC - 2), (8, SCC - 1), (-6, SCC))

    te1yy_n2 = im__(te1yy, (-1, 2), (8, 1)) + (8 * dx)
    te1yy_n1 = im__(te1yy, (1, 1)) + (2 * dx)
    te1yy_p1 = im__(te1yy, (1, SCC - 1))
    te1yy_p2 = im__(te1yy, (8, SCC - 1), (-1, SCC - 2))

    te2yy_n2 = im__(te2yy, (8, 1), (-1, 2))
    te2yy_n1 = im__(te2yy, (1, 1))
    te2yy_p1 = im__(te2yy, (1, SCC - 1)) + (2 * dx)
    te2yy_p2 = im__(te2yy, (-1, SCC - 2), (8, SCC - 1)) + (8 * dx)

    def extend__(vector, neg, pos):
        w = np.insert(vector, 0, neg[1])
        x = np.insert(w, 0, neg[0])
        y = np.append(x, pos[0])
        z = np.append(y, pos[1])
        return z

    d1zz = extend__(d1zz, [d1zz_n2, d1zz_n1], [d1zz_p1, d1zz_p2])
    d2zz = extend__(d2zz, [d2zz_n2, d2zz_n1], [d2zz_p1, d2zz_p2])
    te1zz = extend__(te1zz, [te1zz_n2, te1zz_n1], [te1zz_p1, te1zz_p2])
    te2zz = extend__(te2zz, [te2zz_n2, te2zz_n1], [te2zz_p1, te2zz_p2])
    d1yy = extend__(d1yy, [d1yy_n2, d1yy_n1], [d1yy_p1, d1yy_p2])
    d2yy = extend__(d2yy, [d2yy_n2, d2yy_n1], [d2yy_p1, d2yy_p2])
    te1yy = extend__(te1yy, [te1yy_n2, te1yy_n1], [te1yy_p1, te1yy_p2])
    te2yy = extend__(te2yy, [te2yy_n2, te2yy_n1], [te2yy_p1, te2yy_p2])

    def tmv__(vector, m__, v=False):
        x = np.zeros(SCC + 1)
        y = 2
        if not v:
            sums = [(1, 1), (-2, 0), (1, -1)]
        else:
            sums = [(1, 2), (-2, 1), (2, -1), (-1, -2)]
        for i in range(0, SCC + 1):
            for tuple in sums:
                x[i] += tuple[0] * vector[i + y + tuple[1]]
        z = np.dot(x, m__)
        return z

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
    keb[0, 0] = axial
    keb[1, 1] = - v1zz[0]
    keb[1, 5] = - tv1zz[0]
    keb[2, 2] = - v1yy[0]
    keb[2, 4] = tv1yy[0]
    keb[3, 3] = torsion
    keb[4, 2] = - m1yy[0]
    keb[4, 4] = tm1yy[0]
    keb[5, 1] = m1zz[0]
    keb[5, 5] = tm1zz[0]
    # region two
    keb[6, 0] = - axial
    keb[7, 1] = v1zz[SCC]
    keb[7, 5] = tv1zz[SCC]
    keb[8, 2] = v1yy[SCC]
    keb[8, 4] = - tv1yy[SCC]
    keb[9, 3] = - torsion
    keb[10, 2] = m1yy[SCC]
    keb[10, 4] = - tm1yy[SCC]
    keb[11, 1] = - m1zz[SCC]
    keb[11, 5] = - tm1zz[SCC]
    # region three
    keb[0, 6] = - axial
    keb[1, 7] = - v2zz[0]
    keb[1, 11] = tv2zz[0]
    keb[2, 8] = - v2yy[0]
    keb[2, 10] = - tv2yy[0]
    keb[3, 9] = - torsion
    keb[4, 8] = - m2yy[0]
    keb[4, 10] = - tm2yy[0]
    keb[5, 7] = m2zz[0]
    keb[5, 11] = - tm2zz[0]
    # region four
    keb[6, 6] = axial
    keb[7, 7] = v2zz[SCC]
    keb[7, 11] = - tv2zz[SCC]
    keb[8, 8] = v2yy[SCC]
    keb[8, 10] = tv2yy[SCC]
    keb[9, 9] = torsion
    keb[10, 8] = m2yy[SCC]
    keb[10, 10] = tm2yy[SCC]
    keb[11, 7] = - m2zz[SCC]
    keb[11, 11] = tm2zz[SCC]

    def apoyo_add(keb, apoyos):
        lim = len(apoyos)
        for value in range(lim):
            keb[value,value] = keb[value, value] + apoyos[value]

    apoyo_add(keb, object.apoyos)

    tr = np.matlib.zeros(shape=(12, 12))
    # rotational matrix
    a = math.cos(math.radians(nu))
    b = math.sin(math.radians(nu))
    c = math.cos(math.radians(lm))
    d = math.sin(math.radians(lm))
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

    object.kebg = kebg

    ###########
    pp = object.area() * (object.p_mat / 10000)
    p_axial = ((- math.sin(math.radians(object.lm)) * pp * (object.l / 100)) / 2) +\
              ((- math.sin(math.radians(aw)) * wy * (object.l / 100)) / 2)
    p_scc_y = ((pp * (object.l / 100) * c) / SCC) * ((dx ** 3) / (object.e * object.izz()))
    p_scc_z = 0
    w_scc_y = ((((wy * object.l) / 100) * math.cos(math.radians(aw))) / SCC) * ((dx ** 3) / (object.e * object.izz()))
    w_scc_z = ((wz * (object.l / 100)) / SCC) * ((dx ** 3) / (object.e * object.iyy()))
    f_zz = (object.e * object.izz()) / (dx ** 3)
    f_yy = (object.e * object.iyy()) / (dx ** 3)

    def v_maker1(p_scc__, w_scc__):
        vector = np.zeros(SCC + 1)
        for i in range(1, SCC - 1):
            vector[i] = p_scc__ + w_scc__
        return vector

    vplocal_y = v_maker1(p_scc_y, w_scc_y)
    vplocal_z = v_maker1(p_scc_z, w_scc_z)

    dlzz = np.asarray(np.dot(kzz.I, vplocal_z) * - 1).reshape(-1)
    dlyy = np.asarray(np.dot(kzz.I, vplocal_y) * - 1).reshape(-1)

    dlyy_n2 = (8 * dlyy[1]) - dlyy[2]
    dlyy_n1 = dlyy[1]
    dlyy_p1 = dlyy[SCC - 1]
    dlyy_p2 = (8 * dlyy[SCC - 1]) - dlyy[SCC - 2]
    dlzz_n2 = (8 * dlzz[1]) - dlzz[2]
    dlzz_n1 = dlzz[1]
    dlzz_p1 = dlzz[SCC - 1]
    dlzz_p2 = (8 * dlzz[SCC - 1]) - dlzz[SCC - 2]

    def v_maker2(dl, m__, neg1, pos1):
        vector = np.zeros(SCC + 1)
        vector[0] = (dl[1] - (2 * dl[0]) + neg1) * m__
        vector[SCC] = (dl[SCC - 1] - (2 * dl[SCC]) + pos1) * m__
        for i in range(1, SCC - 1):
            vector[i] = (dl[i + 1] - (2 * dl[i]) + dl[i - 1]) * m__
        return vector

    mdlyy = v_maker2(dlyy, mzz, dlyy_n1, dlyy_p1)
    mdlzz = v_maker2(dlzz, myy, dlzz_n1, dlzz_p1)

    def v_maker3(dl, neg_1, neg_2, pos_1, pos_2, v__, vplocal, f___):
        vector = np.zeros(SCC + 1)
        vector[0] = ((dl[2] - (2 * dl[1]) + (2 * neg_1) - neg_2) * v__) + ((vplocal[1] / 2) * f___)
        vector[1] = (dl[3] - (2 * dl[2]) + (2 * dl[0]) - neg_1) * v__
        vector[SCC - 1] = (pos_1 - (2 * dl[SCC]) + (2 * dl[SCC - 2]) - dl[SCC - 3]) * v__
        vector[SCC] = ((pos_2 - (2 * pos_1) + (2 * dl[SCC - 1]) - dl[SCC - 2]) * v__) - ((vplocal[1] / 2) * f___)
        for i in range(2, SCC - 2):
            vector[i] = (dl[i + 2] - (2 * dl[i + 1]) + (2 * dl[i - 1]) - dl[i - 2]) * v__
        return vector

    vdlyy = v_maker3(dlyy, dlyy_n1, dlyy_n2, dlyy_p1, dlyy_p2, vzz, vplocal_y, f_zz)
    vdlzz = v_maker3(dlzz, dlzz_n1, dlzz_n2, dlzz_p1, dlzz_p2, vyy, vplocal_z, f_yy)

    pcu_local = np.zeros(12)

    pcu_local[0] = p_axial
    pcu_local[1] = - vdlyy[0]
    pcu_local[2] = - dlzz[0]
    pcu_local[3] = 0
    pcu_local[4] = - mdlzz[0]
    pcu_local[5] = mdlyy[0]
    pcu_local[6] = p_axial
    pcu_local[7] = vdlyy[SCC]
    pcu_local[8] = vdlzz[SCC]
    pcu_local[9] = 0
    pcu_local[10] = mdlzz[SCC]
    pcu_local[11] = - mdlyy[SCC]

    pcur = np.dot(tr, pcu_local)

    object.pcur = np.asarray(pcur).reshape(-1)

    return True
