import numpy as np


def matrix_data(dict__):
    def max_ve():
        max_val = 0
        for ky in dict__:
            try_ve = max(ky.ve)
            if try_ve > max_val:
                max_val = try_ve
        return max_val
    m_ve = max_ve()
# matrix_data
    kest = np.matlib.zeros(shape=(m_ve + 1, m_ve + 1))
    pcur_ = np.zeros(m_ve + 1)

    for key in dict__:
        ve = key.ve
        kebg = key.kebg
        pcur = key.pc_
        for i_ in range(12):  # vertical
            pcur_[ve[i_]] += pcur[i_]
            for j in range(12):  # horizontal
                kest[ve[i_], ve[j]] += kebg.item(i_, j)

    kest = np.delete(kest, 0, axis=0)
    kest = np.delete(kest, 0, axis=1)
    pcur_ = np.delete(pcur_, 0, axis=0)

    dn_est = np.dot(kest.I, pcur_)
    return dn_est


def vdgen(dict__, _scc=20):
    dn_est = matrix_data(dict__)
    for key in dict__:
        vdgen_p = np.empty(12)
        for k, i_ in enumerate(key.ve):
            if i_ == 0:
                pass
            else:
                vdgen_p[k] = dn_est[0, i_ - 1]
    # p_global
            p_global = np.dot(key.kebg, vdgen_p).A1
    # fuerza_local
            tr = key.tr
            f = np.dot(tr.T, p_global).A1
    # f_real_local
            pcu_loc = key.pculocal
            pcu_loc[6] = - pcu_loc[6]
            fr_local = pcu_loc - f
    # desp_local
            dlen = np.dot(tr.T, vdgen_p).A1
    # desp_
            y = np.zeros(_scc + 1)
            y[0] = -3 * dlen[1]
            y[1] = -2 * key.dx * dlen[5]
            y[-2] = 2 * key.dx * dlen[11]
            y[-1] = -3 * dlen[7]

            key.desp_imp_antes_y = y

            z = np.zeros(_scc + 1)

            z[0] = 3 * dlen[2]
            z[1] = -2 * key.dx * dlen[4]
            z[-2] = 2 * key.dx * dlen[10]
            z[-1] = 3 * dlen[8]

            desp_imp_y = np.dot(-key.kzz.I, y).A1
            desp_imp_z = np.dot(-key.kyy.I, z).A1
    # d_real
            dry = desp_imp_y + key.dlyy
            drz = desp_imp_z + key.dlzz

    # cortante
            def cor__(v__, dr_, a, b, c):
                v_ = np.empty(_scc + 1)
                for __j in range(2, _scc - 1):
                    v_[__j] = (dr_[__j + 2] - 2*dr_[__j+1] + 2*dr_[__j-1] - dr_[__j - 2]) * v__

                v_[0] = a * fr_local[1 + c]
                v_[1] = (v_[0] + v_[2]) / 2
                v_[-1] = b * fr_local[7 + c]
                v_[-2] = (v_[-1] + v_[-3]) / 2
                return v_

            key.cor_y = cor__(key.vzz, dry, -1, 1, 0)
            key.cor_z = cor__(key.vyy, drz, 1, -1, 1)

    # momentos
            def mome__(dr_, m__, a):

                m_ = np.empty(_scc + 1)

                for j_ in range(1, _scc):
                    m_[j_] = (dr_[j_ + 1] - 2*dr_[j_] + dr_[j_ - 1]) * m__

                m_[0] = fr_local[4 + a]
                m_[-1] = -fr_local[10 + a]

                return m_

            key.mome_y = mome__(drz, key.myy, 0)
            key.mome_z = mome__(dry, key.mzz, 1)

    # presiones
            def pres__(dr_, k_):
                p_ = np.empty(_scc + 1)
                for i in range(len(p_)):
                    p_[i] = dr_[i] * k_ * 10
                return p_
            key.press_y = pres__(dry, key.kv)
            key.press_z = pres__(drz, key.kh)
            key.dry = dry
            key.drz = drz

    # fuerza_axial
            f_ = np.zeros(_scc + 1)
            f_[0] = fr_local[6]

            for i_ in range(1, _scc + 1):
                f_[i_] = f_[i_ - 1] - key.pp_scc
                #print(f_[i_])
            key.fax = f_
    return True
