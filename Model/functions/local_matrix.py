import math
import numpy as np
from numpy import matlib


def local_matrix(section):
    """Descripción: Esta función calcula y asigna los valores individuales por elemento, que después serán usados para
    crear la matrix y vector generales de la estructura."""
    long = section.vector.long
    sections = section.SCC
    elasticity = section.e
    area = section.area()
    izz = section.izz()
    iyy = section.iyy()
    delta_x = long / sections
    mzz = (elasticity * izz) / delta_x ** 25
    myy = (elasticity * iyy) / delta_x ** 2
    vzz = (elasticity * izz) / (2 * delta_x ** 3)
    vyy = (elasticity * iyy) / (2 * delta_x ** 3)
    axial = (elasticity * area) / long
    torsion = ((elasticity / (2 * (1 + section.poisson))) * section.j()) / long
    section.mzz = mzz
    section.myy = myy
    section.vzz = vzz
    section.vyy = vyy

    def imext__(v, *args):
        """Descripción: *Pendiente*"""
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

    d1zz = imext__(np.dot(section.kzz.I,
                          -(np.insert(np.zeros(sections), 0, 3))).A1, (0, -6, 2))
    d2zz = imext__(np.dot(section.kzz.I,
                          -(np.append(np.zeros(sections), 3))).A1, (-1, -6, -3))
    te1zz = imext__(np.dot(section.kzz.I,
                           -(np.insert(np.zeros(sections), 1, 2 * delta_x))).A1,
                    (0, 8 * delta_x), (1, 2 * delta_x))
    te2zz = imext__(np.dot(section.kzz.I,
                           -(np.insert(np.zeros(sections), -1, 2 * delta_x))).A1,
                    (-1, 8 * delta_x), (-2, 2 * delta_x))
    d1yy = imext__(np.dot(section.kyy.I,
                          -(np.insert(np.zeros(sections), 0, 3))).A1, (0, -6, 2))
    d2yy = imext__(np.dot(section.kyy.I,
                          -(np.append(np.zeros(sections), 3))).A1, (-1, -6, -3))
    te1yy = imext__(np.dot(section.kyy.I,
                           -(np.insert(np.zeros(sections), 1, 2 * delta_x))).A1,
                    (0, 8 * delta_x), (1, 2 * delta_x))
    te2yy = imext__(np.dot(section.kyy.I,
                           -(np.insert(np.zeros(sections), -1, 2 * delta_x))).A1,
                    (-1, 8 * delta_x), (-2, 2 * delta_x))

    def tmv__(vector, m__, v=False):
        """Descripción: *Pendiente*"""
        x = np.zeros(sections + 1)
        y = 2
        if not v:
            sums = ((1, 1), (-2, 0), (1, -1))
        else:
            sums = ((1, 2), (-2, 1), (2, -1), (-1, -2))
        for i in range(sections + 1):
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
    keb[7, 1] = v1zz[sections]
    keb[7, 5] = tv1zz[sections]
    keb[8, 2] = v1yy[sections]
    keb[8, 4] = - tv1yy[sections]
    keb[9, 3] = - torsion
    keb[10, 2] = m1yy[sections]
    keb[10, 4] = - tm1yy[sections]
    keb[11, 1] = - m1zz[sections]
    keb[11, 5] = - tm1zz[sections]
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
    keb[7, 7] = v2zz[sections]
    keb[7, 11] = - tv2zz[sections]
    keb[8, 8] = v2yy[sections]
    keb[8, 10] = tv2yy[sections]
    keb[9, 9] = torsion
    keb[10, 8] = m2yy[sections]
    keb[10, 10] = tm2yy[sections]
    keb[11, 7] = - m2zz[sections]
    keb[11, 11] = tm2zz[sections]

    # rotational matrix
    cos_nu = math.cos(math.radians(section.nu))
    sin_nu = math.sin(math.radians(section.nu))
    cos_lm = math.cos(math.radians(section.lm))
    sin_lm = math.sin(math.radians(section.lm))

    def __tr_filler(_tr):
        """Descripción: *Pendiente*"""
        for __j in [0, 3, 6, 9]:
            _tr[__j + 1, __j] = sin_lm
            _tr[__j + 1, __j + 1] = cos_lm
            _tr[__j, __j] = cos_nu * cos_lm
            _tr[__j, __j + 1] = -cos_nu * sin_lm
            _tr[__j, __j + 2] = -sin_nu
            _tr[__j + 2, __j] = sin_nu * cos_lm
            _tr[__j + 2, __j + 1] = -sin_nu * sin_lm
            _tr[__j + 2, __j + 2] = cos_nu
        return _tr

    tr = __tr_filler(np.matlib.zeros(shape=(12, 12)))
    kebg = np.dot(np.dot(tr, keb), tr.T)

    # try:
    #     for i, k in enumerate(section.springs, 0):
    #         kebg[i, i] += k
    # except TypeError:
    #     pass

    section.tr = tr
    section.keb = keb
    section.kebg = kebg

    pp = area * (section.p_mat / 10000)
    section.pp_scc = ((pp * (long / 100)) / sections) * sin_lm

    p_axial = ((- sin_lm *
                pp * (long / 100)) / 2) + \
              ((- math.sin(math.radians(section.aw)) * section.wy *
                (long / 100)) / 2)

    p_scc_y = ((pp * (long / 100) * cos_lm) / sections) * \
              ((delta_x ** 3) / (elasticity * izz))

    p_scc_z = 0
    w_scc_y = ((((section.wy * long) / 100) *
                math.cos(math.radians(section.aw))) / sections) * \
              ((delta_x ** 3) / (elasticity * izz))

    w_scc_z = ((section.wz * (long / 100)) /
               sections) * ((delta_x ** 3) / (elasticity * iyy))

    try:
        if section.armour is True:
            p_elem = pp * (long / 100)
            vplocal_y = np.zeros(sections + 1)
            vplocal_z = np.zeros(sections + 1)
            p_vertical = -(cos_lm * p_elem) / 2

    except AttributeError:
        setattr(section, 'armour', False)

    finally:
        if section.armour is False:
            vplocal_y = np.insert(np.append(np.full((sections - 1,), (p_scc_y + w_scc_y)), 0), 0, 0)
            vplocal_z = np.insert(np.append(np.full((sections - 1,), (p_scc_z + w_scc_z)), 0), 0, 0)

    dlzz = np.dot(section.kzz.I, -vplocal_z).A1
    dlyy = np.dot(section.kyy.I, -vplocal_y).A1

    section.dlzz = dlzz
    section.dlyy = dlyy

    def v_maker2(dl, m__):
        """Descripción: *Pendiente*"""
        vector = np.empty(sections + 1)
        vector[0] = (dl[1] - (2 * dl[0]) + dl[1]) * m__
        vector[-1] = (dl[-2] - (2 * dl[-1]) + dl[-2]) * m__
        for i in range(1, sections):
            vector[i] = (dl[i + 1] - (2 * dl[i]) + dl[i - 1]) * m__
        return vector

    mdlyy = v_maker2(dlyy, mzz)
    mdlzz = v_maker2(dlzz, myy)
    section.mdlyy = mdlyy
    section.mdlzz = mdlzz

    def v_maker3(dl, v__, vplocal, i__):
        """Descripción: *Pendiente*"""
        vector = np.empty(sections + 1)
        vector[0] = ((dl[2] - (2 * dl[1]) + (2 * dl[1]) - ((8 * dl[1]) - dl[2])) * v__) + \
                    ((vplocal[1] / 2) * (elasticity * i__ / (delta_x ** 3)))
        vector[1] = (dl[3] - (2 * dl[2]) + (2 * dl[0]) - dl[1]) * v__
        vector[-2] = (dl[-2] - (2 * dl[-1]) + (2 * dl[-3]) - dl[-4]) * v__
        vector[-1] = ((((8 * dl[-2]) - dl[-3]) - (2 * dl[-2]) + (2 * dl[-2]) - dl[-3]) * v__) - \
                     ((vplocal[1] / 2) * (elasticity * i__ / (delta_x ** 3)))
        for i in range(2, sections - 1):
            vector[i] = (dl[i + 2] - (2 * dl[i + 1]) + (2 * dl[i - 1]) - dl[i - 2]) * v__
        return vector

    vdlyy = v_maker3(dlyy, vzz, vplocal_y, izz)
    vdlzz = v_maker3(dlzz, vyy, vplocal_z, iyy)

    pcu_local = np.zeros(12)

    if section.armour is True:
        pcu_local[0] = p_axial
        pcu_local[1] = p_vertical
        pcu_local[6] = p_axial
        pcu_local[7] = p_vertical

    else:
        pcu_local[0] = p_axial
        pcu_local[1] = - vdlyy[0]
        pcu_local[2] = - vdlzz[0]
        pcu_local[4] = - mdlzz[0]
        pcu_local[5] = mdlyy[0]
        pcu_local[6] = p_axial
        pcu_local[7] = vdlyy[sections]
        pcu_local[8] = vdlzz[sections]
        pcu_local[10] = mdlzz[sections]
        pcu_local[11] = - mdlyy[sections]

    section.pculocal = pcu_local
    section.pc_ = np.dot(tr, pcu_local).A1
    
    return section