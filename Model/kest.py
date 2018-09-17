import numpy as np
import math
from Model.Classes import Main

Elementos = Main.Elementos

Nodos = Main.Nodos

Max_val = Main.Max_val

def vdgen():
    print('Iniciando calculos')

    for key in Elementos:
        #key.add()
        key.set_nodes()
        key.calculations()

    try:
        kest = np.matlib.zeros(shape=(max(Max_val) + 1, max(Max_val) + 1))
        pcur_ = np.zeros(max(Max_val) + 1)

    except ValueError:
        print('No se han iniciado correctamente los calculos de elementos')
        return False

    for key in Elementos:
        for i_ in range(12):  # vertical
            pcur_[key.ve[i_]] += key.pc_[i_]
            for j in range(12):  # horizontal
                kest[key.ve[i_], key.ve[j]] += key.kebg.item(i_, j)

    print('[Grados]:\t' + '[' + str(max(Max_val)) + ']')

    kest = np.delete(kest, 0, axis=0)
    kest = np.delete(kest, 0, axis=1)
    pcur_ = np.delete(pcur_, 0, axis=0)

    pcur_ = pcur_ + Main.v_c_n
    dn_est = np.dot(kest.I, pcur_)

    for key in Elementos:
        _scc = key.SCC
        vdgen_p = np.zeros(12)
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
        key.apoyos = np.asarray(key.apoyos)
        f_g_springs = np.multiply(vdgen_p, key.apoyos)
        f_l_springs = np.dot(tr.T, f_g_springs).A1
        fr_local = pcu_loc - f + f_l_springs
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
        key.dry = desp_imp_y + key.dlyy
        key.drz = desp_imp_z - key.dlzz

        # cortante
        def cor__(v__, dr_, a, b, c):
            v_ = np.zeros(_scc + 1)
            for __j in range(2, _scc - 1):
                v_[__j] = (dr_[__j + 2] - 2*dr_[__j+1] + 2*dr_[__j-1] - dr_[__j - 2]) * v__
            v_[0] = a * fr_local[1 + c]
            v_[1] = (v_[0] + v_[2]) / 2
            v_[-1] = b * fr_local[7 + c]
            v_[-2] = (v_[-1] + v_[-3]) / 2
            return v_

        key.cor_y = cor__(key.vzz, key.dry, -1, 1, 0)
        key.cor_z = cor__(key.vyy, key.drz, 1, -1, 1)

        # momentos
        def mome__(dr_, m__, a):
            m_ = np.zeros(_scc + 1)
            for j_ in range(1, _scc):
                m_[j_] = (dr_[j_ + 1] - 2*dr_[j_] + dr_[j_ - 1]) * m__
            m_[0] = fr_local[4 + a]
            m_[-1] = -fr_local[10 + a]
            return m_

        key.mome_y = mome__(key.drz, key.myy, 0)
        key.mome_z = mome__(key.dry, key.mzz, 1)

        # presiones
        def pres__(dr_, k_):
            p_ = np.zeros(_scc + 1)
            for i in range(len(p_)):
                p_[i] = dr_[i] * k_ * 10
            return p_

        key.press_y = pres__(key.dry, key.kv)
        key.press_z = pres__(key.drz, key.kh)

        key.toDeactivate = []

        for sccToDeactivate in key.press_y:
            #print(sccToDeactivate)
            if float(sccToDeactivate) > 0.0 and not key.armadura:
                #print('desactivar')
                key.toDeactivate.append(True)
            else:
                key.toDeactivate.append(False)

        deactivator = all(key.toDeactivate)

        # fuerza_axial
        f_ = np.zeros(_scc + 1)
        f_[0] = fr_local[0]

        for i_ in range(1, _scc + 1):
            f_[i_] = f_[i_ - 1] + key.pp_scc

        for ef_, j_ in enumerate(f_,0):
            f_[ef_] = f_[ef_] + ef_ * ((key.wy * (key.l / 100) * math.sin(math.radians(key.aw))) / _scc)

        key.fax = f_
        # torsion Mx
        key.mx = np.full(_scc +1, f[3])

        key.excel_output()

    return deactivator
