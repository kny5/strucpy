import numpy as np
from numpy import matlib
import math


def local_matrix(self):
    self.mzz = (self.e * self.izz()) / (self.long / self.SCC) ** 2
    self.myy = (self.e * self.iyy()) / (self.long / self.SCC) ** 2
    self.vzz = (self.e * self.izz()) / (2 * (self.long / self.SCC) ** 3)
    self.vyy = (self.e * self.iyy()) / (2 * (self.long / self.SCC) ** 3)
    axial = (self.e * self.area()) / self.long
    torsion = ((self.e / (2 * (1 + self.poisson))) * self.j()) / self.long

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

    d1zz = imext__(np.dot(self.kzz.I, -(np.insert(np.zeros(self.SCC), 0, 3))).A1, (0, -6, 2))
    d2zz = imext__(np.dot(self.kzz.I, -(np.append(np.zeros(self.SCC), 3))).A1, (-1, -6, -3))
    te1zz = imext__(np.dot(self.kzz.I, -(np.insert(np.zeros(self.SCC), 1, 2 * (self.long / self.SCC)))).A1,
                    (0, 8 * (self.long / self.SCC)), (1, 2 * (self.long / self.SCC)))
    te2zz = imext__(np.dot(self.kzz.I, -(np.insert(np.zeros(self.SCC), -1, 2 * (self.long / self.SCC)))).A1,
                    (-1, 8 * (self.long / self.SCC)), (-2, 2 * (self.long / self.SCC)))
    d1yy = imext__(np.dot(self.kyy.I, -(np.insert(np.zeros(self.SCC), 0, 3))).A1, (0, -6, 2))
    d2yy = imext__(np.dot(self.kyy.I, -(np.append(np.zeros(self.SCC), 3))).A1, (-1, -6, -3))
    te1yy = imext__(np.dot(self.kyy.I, -(np.insert(np.zeros(self.SCC), 1, 2 * (self.long / self.SCC)))).A1,
                    (0, 8 * (self.long / self.SCC)), (1, 2 * (self.long / self.SCC)))
    te2yy = imext__(np.dot(self.kyy.I, -(np.insert(np.zeros(self.SCC), -1, 2 * (self.long / self.SCC)))).A1,
                    (-1, 8 * (self.long / self.SCC)), (-2, 2 * (self.long / self.SCC)))

    def tmv__(vector, m__, v=False):
        x = np.zeros(self.SCC + 1)
        y = 2
        if not v:
            sums = ((1, 1), (-2, 0), (1, -1))
        else:
            sums = ((1, 2), (-2, 1), (2, -1), (-1, -2))
        for i in range(self.SCC + 1):
            for tupl_ in sums:
                x[i] += tupl_[0] * vector[i + y + tupl_[1]]
        z = np.dot(x, m__)
        return z

    m1zz = tmv__(d1zz, self.mzz)
    m2zz = tmv__(d2zz, self.mzz)
    tm1zz = tmv__(te1zz, self.mzz)
    tm2zz = tmv__(te2zz, self.mzz)

    m1yy = tmv__(d1yy, self.myy)
    m2yy = tmv__(d2yy, self.myy)
    tm1yy = tmv__(te1yy, self.myy)
    tm2yy = tmv__(te2yy, self.myy)

    v1zz = tmv__(d1zz, self.vzz, v=True)
    v2zz = tmv__(d2zz, self.vzz, v=True)
    tv1zz = tmv__(te1zz, self.vzz, v=True)
    tv2zz = tmv__(te2zz, self.vzz, v=True)

    v1yy = tmv__(d1yy, self.vyy, v=True)
    v2yy = tmv__(d2yy, self.vyy, v=True)
    tv1yy = tmv__(te1yy, self.vyy, v=True)
    tv2yy = tmv__(te2yy, self.vyy, v=True)

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
    keb[7, 1] = v1zz[self.SCC]
    keb[7, 5] = tv1zz[self.SCC]
    keb[8, 2] = v1yy[self.SCC]
    keb[8, 4] = - tv1yy[self.SCC]
    keb[9, 3] = - torsion
    keb[10, 2] = m1yy[self.SCC]
    keb[10, 4] = - tm1yy[self.SCC]
    keb[11, 1] = - m1zz[self.SCC]
    keb[11, 5] = - tm1zz[self.SCC]
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
    keb[7, 7] = v2zz[self.SCC]
    keb[7, 11] = - tv2zz[self.SCC]
    keb[8, 8] = v2yy[self.SCC]
    keb[8, 10] = tv2yy[self.SCC]
    keb[9, 9] = torsion
    keb[10, 8] = m2yy[self.SCC]
    keb[10, 10] = tm2yy[self.SCC]
    keb[11, 7] = - m2zz[self.SCC]
    keb[11, 11] = tm2zz[self.SCC]

    tr = np.matlib.zeros(shape=(12, 12))
    # rotational matrix
    cosnu = math.cos(math.radians(self.nu))
    sinu = math.sin(math.radians(self.nu))
    coslm = math.cos(math.radians(self.lm))
    sinlm = math.sin(math.radians(self.lm))
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

    try:
        for i, k in enumerate(self.springs, 0):
            kebg[i, i] += k
    except TypeError:
        pass

    self.tr = tr
    self.keb = keb
    self.kebg = kebg

    pp = self.area() * (self.p_mat / 10000)
    self.pp_scc = ((pp * (self.long / 100)) / self.SCC) * sinlm

    p_axial = ((- sinlm *
                pp * (self.long / 100)) / 2) + \
              ((- math.sin(math.radians(self.aw)) * self.wy *
                (self.long / 100)) / 2)

    p_scc_y = ((pp * (self.long / 100) * coslm) / self.SCC) * \
              (((self.long / self.SCC) ** 3) / (self.e * self.izz()))

    p_scc_z = 0
    w_scc_y = ((((self.wy * self.long) / 100) *
                math.cos(math.radians(self.aw))) / self.SCC) * \
              (((self.long / self.SCC) ** 3) / (self.e * self.izz()))

    w_scc_z = ((self.wz * (self.long / 100)) / self.SCC) * (((self.long / self.SCC) ** 3) / (self.e * self.iyy()))

    try:
        if self.armadura:
            p_elem = pp * (self.long / 100)
            vplocal_y = np.zeros(self.SCC + 1)
            vplocal_z = np.zeros(self.SCC + 1)
            p_vertical = -(coslm * p_elem) / 2

        elif not self.armadura:
            vplocal_y = np.insert(np.append(np.full((self.SCC - 1,), (p_scc_y + w_scc_y)), 0), 0, 0)
            vplocal_z = np.insert(np.append(np.full((self.SCC - 1,), (p_scc_z + w_scc_z)), 0), 0, 0)

    except AttributeError:
        vplocal_y = np.insert(np.append(np.full((self.SCC - 1,), (p_scc_y + w_scc_y)), 0), 0, 0)
        vplocal_z = np.insert(np.append(np.full((self.SCC - 1,), (p_scc_z + w_scc_z)), 0), 0, 0)

    dlzz = np.dot(self.kzz.I, -vplocal_z).A1
    dlyy = np.dot(self.kyy.I, -vplocal_y).A1

    self.dlzz = dlzz
    self.dlyy = dlyy

    def v_maker2(dl, m__):
        vector = np.empty(self.SCC + 1)
        vector[0] = (dl[1] - (2 * dl[0]) + dl[1]) * m__
        vector[-1] = (dl[-2] - (2 * dl[-1]) + dl[-2]) * m__
        for i in range(1, self.SCC):
            vector[i] = (dl[i + 1] - (2 * dl[i]) + dl[i - 1]) * m__
        return vector

    mdlyy = v_maker2(dlyy, self.mzz)
    self.mdlyy = mdlyy
    mdlzz = v_maker2(dlzz, self.myy)
    self.mdlzz = mdlzz

    def v_maker3(dl, v__, vplocal, i__):
        vector = np.empty(self.SCC + 1)
        vector[0] = ((dl[2] - (2 * dl[1]) + (2 * dl[1]) - ((8 * dl[1]) - dl[2])) * v__) + \
                    ((vplocal[1] / 2) * (self.e * i__ / ((self.long / self.SCC) ** 3)))

        vector[1] = (dl[3] - (2 * dl[2]) + (2 * dl[0]) - dl[1]) * v__

        vector[-2] = (dl[-2] - (2 * dl[-1]) + (2 * dl[-3]) - dl[-4]) * v__

        vector[-1] = ((((8 * dl[-2]) - dl[-3]) - (2 * dl[-2]) + (2 * dl[-2]) - dl[-3]) * v__) - \
                     ((vplocal[1] / 2) * (self.e * i__ / ((self.long / self.SCC) ** 3)))

        for i in range(2, self.SCC - 1):
            vector[i] = (dl[i + 2] - (2 * dl[i + 1]) + (2 * dl[i - 1]) - dl[i - 2]) * v__

        return vector

    vdlyy = v_maker3(dlyy, self.vzz, vplocal_y, self.izz())
    vdlzz = v_maker3(dlzz, self.vyy, vplocal_z, self.iyy())

    pcu_local = np.zeros(12)
    try:
        if self.armadura:
            pcu_local[0] = p_axial
            pcu_local[1] = p_vertical
            pcu_local[2] = 0
            pcu_local[3] = 0
            pcu_local[4] = 0
            pcu_local[5] = 0
            pcu_local[6] = p_axial
            pcu_local[7] = p_vertical
            pcu_local[8] = 0
            pcu_local[9] = 0
            pcu_local[10] = 0
            pcu_local[11] = 0

        elif not self.armadura:
            pcu_local[0] = p_axial
            pcu_local[1] = - vdlyy[0]
            pcu_local[2] = - vdlzz[0]
            pcu_local[3] = 0
            pcu_local[4] = - mdlzz[0]
            pcu_local[5] = mdlyy[0]
            pcu_local[6] = p_axial
            pcu_local[7] = vdlyy[self.SCC]
            pcu_local[8] = vdlzz[self.SCC]
            pcu_local[9] = 0
            pcu_local[10] = mdlzz[self.SCC]
            pcu_local[11] = - mdlyy[self.SCC]

    except AttributeError:
        pcu_local[0] = p_axial
        pcu_local[1] = - vdlyy[0]
        pcu_local[2] = - vdlzz[0]
        pcu_local[3] = 0
        pcu_local[4] = - mdlzz[0]
        pcu_local[5] = mdlyy[0]
        pcu_local[6] = p_axial
        pcu_local[7] = vdlyy[self.SCC]
        pcu_local[8] = vdlzz[self.SCC]
        pcu_local[9] = 0
        pcu_local[10] = mdlzz[self.SCC]
        pcu_local[11] = - mdlyy[self.SCC]

    self.pculocal = pcu_local
    self.pc_ = np.dot(tr, pcu_local).A1

    return True
