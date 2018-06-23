import numpy as np
from numpy import matlib
import math
# from pandas import DataFrame as df


def calculations(object, SCC=20, POISSON=0.25):
    dx = object.l / SCC
    object.dx = dx
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
    wy = object.wy
    wz = object.wz
    aw = object.aw
    object.vzz = vzz
    object.vyy = vyy
    object.myy = myy
    object.mzz = mzz

    def k__(c):
        k = np.matlib.zeros(shape=((SCC + 1), (SCC + 1)))
        k[0, 0] = k[-1, -1] = 3
        k[1, 1] = k[-2, -2] = 7 + c
        k[1, 0] = k[1, 2] = k[-2, -1] = k[-2, -3] = -4
        k[1, 3] = k[-2, -4] = 1
        for i in range(2, SCC - 1):
            k[i, i] = 6 + c
            k[i, i - 2] = k[i, i + 2] = 1
            k[i, i - 1] = k[i, i + 1] = -4
        return k

    kzz = k__(A)
    object.kzz = kzz
    kyy = k__(B)
    object.kyy = kyy

    def imext__(v, *args):
        n1_ = v[1]
        n2_ = -v[2] + (8 * v[1])
        p1_ = v[-2]
        p2_ = (8 * v[-2]) - v[-3]

        v1 = np.append(np.insert(v, 0, (n2_, n1_)), (p1_, p2_))
        for tupl_ in args:
            if len(tupl_) == 3:
                v1[tupl_[0]] += tupl_[1] * v1[tupl_[2]]
            else:
                v1[tupl_[0]] += tupl_[1]
        return v1

    d1zz = imext__(np.dot(kzz.I, -(np.insert(np.zeros(SCC), 0, 3))).A1, (0, -6, 2))
    d2zz = imext__(np.dot(kzz.I, -(np.append(np.zeros(SCC), 3))).A1, (-1, -6, -3))
    te1zz = imext__(np.dot(kzz.I, -(np.insert(np.zeros(SCC), 1, 2 * dx))).A1, (0, 8 * dx), (1, 2 * dx))
    te2zz = imext__(np.dot(kzz.I, -(np.insert(np.zeros(SCC), -1, 2 * dx))).A1, (-1, 8 * dx), (-2, 2 * dx))
    d1yy = imext__(np.dot(kyy.I, -(np.insert(np.zeros(SCC), 0, 3))).A1, (0, -6, 2))
    d2yy = imext__(np.dot(kyy.I, -(np.append(np.zeros(SCC), 3))).A1, (-1, -6, -3))
    te1yy = imext__(np.dot(kyy.I, -(np.insert(np.zeros(SCC), 1, 2 * dx))).A1, (0, 8 * dx), (1, 2 * dx))
    te2yy = imext__(np.dot(kyy.I, -(np.insert(np.zeros(SCC), -1, 2 * dx))).A1, (-1, 8 * dx), (-2, 2 * dx))

    def tmv__(vector, m__, v=False):
        x = np.zeros(SCC + 1)
        y = 2
        if not v:
            sums = ((1, 1), (-2, 0), (1, -1))
        else:
            sums = ((1, 2), (-2, 1), (2, -1), (-1, -2))
        for i in range(SCC + 1):
            for tupl_ in sums:
                x[i] += tupl_[0] * vector[i + y + tupl_[1]]
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

    if object.apoyos:
        for i, k in enumerate(object.apoyos):
            keb[i, i] += k

    tr = np.matlib.zeros(shape=(12, 12))
    # rotational matrix
    cosnu = math.cos(math.radians(nu))
    sinu = math.sin(math.radians(nu))
    coslm = math.cos(math.radians(lm))
    sinlm = math.sin(math.radians(lm))
    # region one
    tr[0, 0] = cosnu * coslm
    tr[0, 1] = - cosnu * sinlm
    tr[0, 2] = - sinu
    tr[1, 0] = sinlm
    tr[1, 1] = coslm
    tr[2, 0] = sinu * coslm
    tr[2, 1] = - sinu * sinlm
    tr[2, 2] = cosnu
    tr[3, 3] = cosnu * coslm
    tr[3, 4] = - cosnu * sinlm
    tr[3, 5] = - sinu
    tr[4, 3] = sinlm
    tr[4, 4] = coslm
    tr[5, 3] = sinu * coslm
    tr[5, 4] = - sinu * sinlm
    tr[5, 5] = cosnu
    # region two
    tr[6, 6] = cosnu * coslm
    tr[6, 7] = - cosnu * sinlm
    tr[6, 8] = - sinu
    tr[7, 6] = sinlm
    tr[7, 7] = coslm
    tr[8, 6] = sinu * coslm
    tr[8, 7] = - sinu * sinlm
    tr[8, 8] = cosnu
    tr[9, 9] = cosnu * coslm
    tr[9, 10] = - cosnu * sinlm
    tr[9, 11] = - sinu
    tr[10, 9] = sinlm
    tr[10, 10] = coslm
    tr[11, 9] = sinu * coslm
    tr[11, 10] = - sinu * sinlm
    tr[11, 11] = cosnu

    kebg = np.dot(np.dot(tr, keb), tr.T)

    object.tr = tr

    object.keb = keb

    object.kebg = kebg

    ###########
    pp = object.area() * (object.p_mat / 10000)

    object.pp_scc = ((pp * (object.l / 100)) / SCC) * sinlm

    p_axial = ((- sinlm *
                pp * (object.l / 100)) / 2) + \
              ((- math.sin(math.radians(aw)) * wy *
                (object.l / 100)) / 2)

    p_scc_y = ((pp * (object.l / 100) * coslm) / SCC) *\
              ((dx ** 3) / (object.e * object.izz()))
    # object.p_secc_y = p_scc_y
    p_scc_z = 0
    w_scc_y = ((((wy * object.l) / 100) *
                math.cos(math.radians(aw))) / SCC) * \
              ((dx ** 3) / (object.e * object.izz()))
    # object.w_scc_y = w_scc_y
    w_scc_z = ((wz * (object.l / 100)) / SCC) * ((dx ** 3) / (object.e * object.iyy()))
    f_zz = (object.e * object.izz()) / (2 * dx ** 3)
    f_yy = (object.e * object.iyy()) / (2 * dx ** 3)

    vplocal_y = np.insert(np.append(np.full((SCC - 1,), (p_scc_y + w_scc_y)), 0), 0, 0)
    vplocal_z = np.insert(np.append(np.full((SCC - 1,), (p_scc_z + w_scc_z)), 0), 0, 0)

    # for k, i in enumerate(vplocal_y):
    #    if i == vplocal_y_c[k]:
    #        print('ey')
    #    else:
    #        print('lu')

    dlzz = np.dot(kzz.I, -vplocal_z).A1

    dlyy = np.dot(kyy.I, -vplocal_y).A1

    object.dlzz = dlzz
    object.dlyy = dlyy

    def v_maker2(dl, m__):
        vector = np.empty(SCC + 1)
        vector[0] = (dl[1] - (2 * dl[0]) + dl[1]) * m__
        vector[-1] = (dl[-2] - (2 * dl[-1]) + dl[-2]) * m__
        for i in range(1, SCC):
            vector[i] = (dl[i + 1] - (2 * dl[i]) + dl[i - 1]) * m__
        return vector

    mdlyy = v_maker2(dlyy, mzz)
    object.mdlyy = mdlyy

    mdlzz = v_maker2(dlzz, myy)
    object.mdlzz = mdlzz

    def v_maker3(dl, v__, vplocal, i__):
        vector = np.empty(SCC + 1)
        vector[0] = ((dl[2] - (2 * dl[1]) + (2 * dl[1]) - ((8 * dl[1]) - dl[2])) * v__) +\
                    ((vplocal[1] / 2) * (object.e * i__ / (dx ** 3)))

        vector[1] = (dl[3] - (2 * dl[2]) + (2 * dl[0]) - dl[1]) * v__

        vector[-2] = (dl[-2] - (2 * dl[-1]) + (2 * dl[-3]) - dl[-4]) * v__

        vector[-1] = ((((8 * dl[-2]) - dl[-3]) - (2 * dl[-2]) + (2 * dl[-2]) - dl[-3]) * v__) -\
                     ((vplocal[1] / 2) * (object.e * i__ / (dx ** 3)))

        for i in range(2, SCC - 1):
            vector[i] = (dl[i + 2] - (2 * dl[i + 1]) + (2 * dl[i - 1]) - dl[i - 2]) * v__

        return vector

    vdlyy = v_maker3(dlyy, vzz, vplocal_y, object.izz())

    vdlzz = v_maker3(dlzz, vyy, vplocal_z, object.iyy())

    pcu_local = np.empty(12)

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

    object.pculocal = pcu_local

    pcur = np.dot(tr, pcu_local)

    object.pcur = pcur.A1

    return True
