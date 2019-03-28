import numpy as np
import math


def get_data(self, section):

    vdgen_p = np.zeros(12)
    for k, i_ in enumerate(section.ve):
        if i_ != 0:
            vdgen_p[k] = self.dn_est[0, i_ - 1]
        else:
            pass

    # p_global
    p_global = np.dot(section.kebg, vdgen_p).A1
    # fuerza_local
    f = np.dot(section.tr.T, p_global).A1
    # f_real_local
    pcu_loc = section.pculocal
    pcu_loc[6] = - pcu_loc[6]
    section.springs = np.asarray(section.springs)
    f_g_springs = np.multiply(vdgen_p, section.springs)
    f_l_springs = np.dot(section.tr.T, f_g_springs).A1
    fr_local = pcu_loc - f + f_l_springs
    # desp_local
    dlen = np.dot(section.tr.T, vdgen_p).A1
    # desp_
    y = np.zeros(section.SCC + 1)
    y[0] = -3 * dlen[1]
    y[1] = -2 * (section.long / section.SCC) * dlen[5]
    y[-2] = 2 * (section.long / section.SCC) * dlen[11]
    y[-1] = -3 * dlen[7]

    section.desp_imp_antes_y = y

    z = np.zeros(section.SCC + 1)
    z[0] = 3 * dlen[2]
    z[1] = -2 * (section.long / section.SCC) * dlen[4]
    z[-2] = 2 * (section.long / section.SCC) * dlen[10]
    z[-1] = 3 * dlen[8]

    desp_imp_y = np.dot(-section.kzz.I, y).A1
    desp_imp_z = np.dot(-section.kyy.I, z).A1

    # d_real
    section.dry = desp_imp_y + section.dlyy
    section.drz = desp_imp_z - section.dlzz

    # cortante
    def cor__(v__, dr_, a, b, c):
        v_ = np.zeros(section.SCC + 1)
        for __j in range(2, section.SCC - 1):
            v_[__j] = (dr_[__j + 2] - 2 * dr_[__j + 1] + 2 * dr_[__j - 1] - dr_[__j - 2]) * v__
        v_[0] = a * fr_local[1 + c]
        v_[1] = (v_[0] + v_[2]) / 2
        v_[-1] = b * fr_local[7 + c]
        v_[-2] = (v_[-1] + v_[-3]) / 2
        return v_

    section.cor_y = cor__(section.vzz, section.dry, -1, 1, 0)
    section.cor_z = cor__(section.vyy, section.drz, 1, -1, 1)

    # momentos
    def mome__(dr_, m__, a):
        m_ = np.zeros(section.SCC + 1)
        for j_ in range(1, section.SCC):
            m_[j_] = (dr_[j_ + 1] - 2 * dr_[j_] + dr_[j_ - 1]) * m__
        m_[0] = fr_local[4 + a]
        m_[-1] = -fr_local[10 + a]
        return m_

    section.mome_y = mome__(section.drz, section.myy, 0)
    section.mome_z = mome__(section.dry, section.mzz, 1)

    # presiones
    def pres__(dr_, k_):
        p_ = np.zeros(section.SCC + 1)
        for i in range(len(p_)):
            p_[i] = dr_[i] * k_ * 10
        return p_

    section.press_y = pres__(section.dry, section.kv)
    section.press_z = pres__(section.drz, section.kh)

    # fuerza_axial
    f_ = np.zeros(section.SCC + 1)
    f_[0] = fr_local[0]

    for i_ in range(1, section.SCC + 1):
        f_[i_] = f_[i_ - 1] + section.pp_scc

    for ef_, j_ in enumerate(f_, 0):
        f_[ef_] = f_[ef_] + ef_ * ((section.wy * (section.long / 100) * math.sin(math.radians(section.aw))) / section.SCC)

    section.fax = f_
    # torsion Mx
    section.mx = np.full(section.SCC + 1, f[3])

    return section
