import numpy as np
import math


def get_data(self, elemento):

    vdgen_p = np.zeros(12)
    for k, i_ in enumerate(elemento.ve):
        if i_ == 0:
            pass
        else:
            vdgen_p[k] = self.dn_est[0, i_ - 1]
    # p_global
    p_global = np.dot(elemento.kebg, vdgen_p).A1
    # fuerza_local
    tr = elemento.tr
    f = np.dot(tr.T, p_global).A1
    # f_real_local
    pcu_loc = elemento.pculocal
    pcu_loc[6] = - pcu_loc[6]
    elemento.springs = np.asarray(elemento.springs)
    f_g_springs = np.multiply(vdgen_p, elemento.springs)
    f_l_springs = np.dot(tr.T, f_g_springs).A1
    fr_local = pcu_loc - f + f_l_springs
    # desp_local
    dlen = np.dot(tr.T, vdgen_p).A1
    # desp_
    y = np.zeros(elemento.SCC + 1)
    y[0] = -3 * dlen[1]
    y[1] = -2 * (elemento.long / elemento.SCC) * dlen[5]
    y[-2] = 2 * (elemento.long / elemento.SCC) * dlen[11]
    y[-1] = -3 * dlen[7]

    elemento.desp_imp_antes_y = y

    z = np.zeros(elemento.SCC + 1)
    z[0] = 3 * dlen[2]
    z[1] = -2 * (elemento.long / elemento.SCC) * dlen[4]
    z[-2] = 2 * (elemento.long / elemento.SCC) * dlen[10]
    z[-1] = 3 * dlen[8]

    desp_imp_y = np.dot(-elemento.kzz.I, y).A1
    desp_imp_z = np.dot(-elemento.kyy.I, z).A1

    # d_real
    elemento.dry = desp_imp_y + elemento.dlyy
    elemento.drz = desp_imp_z - elemento.dlzz

    # cortante
    def cor__(v__, dr_, a, b, c):
        v_ = np.zeros(elemento.SCC + 1)
        for __j in range(2, elemento.SCC - 1):
            v_[__j] = (dr_[__j + 2] - 2 * dr_[__j + 1] + 2 * dr_[__j - 1] - dr_[__j - 2]) * v__
        v_[0] = a * fr_local[1 + c]
        v_[1] = (v_[0] + v_[2]) / 2
        v_[-1] = b * fr_local[7 + c]
        v_[-2] = (v_[-1] + v_[-3]) / 2
        return v_

    elemento.cor_y = cor__(elemento.vzz, elemento.dry, -1, 1, 0)
    elemento.cor_z = cor__(elemento.vyy, elemento.drz, 1, -1, 1)

    # momentos
    def mome__(dr_, m__, a):
        m_ = np.zeros(elemento.SCC + 1)
        for j_ in range(1, elemento.SCC):
            m_[j_] = (dr_[j_ + 1] - 2 * dr_[j_] + dr_[j_ - 1]) * m__
        m_[0] = fr_local[4 + a]
        m_[-1] = -fr_local[10 + a]
        return m_

    elemento.mome_y = mome__(elemento.drz, elemento.myy, 0)
    elemento.mome_z = mome__(elemento.dry, elemento.mzz, 1)

    # presiones
    def pres__(dr_, k_):
        p_ = np.zeros(elemento.SCC + 1)
        for i in range(len(p_)):
            p_[i] = dr_[i] * k_ * 10
        return p_

    elemento.press_y = pres__(elemento.dry, elemento.kv)
    elemento.press_z = pres__(elemento.drz, elemento.kh)

    # if elemento.kv > 0:
    #     setattr(elemento, "toActivate", [])
    #     for _i, active in enumerate(elemento.press_y):
    #
    #         if _i == 0 or _i == elemento.SCC:
    #             elemento.toActivate.append(True)
    #
    #         elif active > 0:
    #             elemento.toActivate.append(False)
    #
    #         else:
    #             elemento.toActivate.append(True)
    #
    #     if not all(elemento.toActivate):
    #         return False

    # fuerza_axial
    f_ = np.zeros(elemento.SCC + 1)
    f_[0] = fr_local[0]

    for i_ in range(1, elemento.SCC + 1):
        f_[i_] = f_[i_ - 1] + elemento.pp_scc

    for ef_, j_ in enumerate(f_, 0):
        f_[ef_] = f_[ef_] + ef_ * ((elemento.wy * (elemento.long / 100) * math.sin(math.radians(elemento.aw))) / elemento.SCC)

    elemento.fax = f_
    # torsion Mx
    elemento.mx = np.full(elemento.SCC + 1, f[3])

    return True
