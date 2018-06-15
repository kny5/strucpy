import numpy as np
from numpy.linalg import inv


def est_init(dict):
    y = 0
    lim = len(dict)
    for key in range(0,lim):
        x = max(dict[key].ve)
        if x > y:
            y = x
    kest = np.matlib.zeros(shape=(y + 1, y + 1))
    pcur = np.zeros(y + 1)
    return {"kest" : kest, "pcur" : pcur}


def kest_maker(dict__, est_init__):
    lim = 12
    for key in range(len(dict__)):
        ve = dict__[key].ve
        kebg = dict__[key].kebg
        # print("lim ",lim)
        for i in range(0, lim):  # vertical
            # print("lim ",lim)
            for j in range(0, lim):  # horizontal
                est_init__[ve[i], ve[j]] += kebg.item(i, j)
                #print(dict__[key])
                #print("[",i,"]","[",j,"]","valor: ",kebg.item(i, j))  # trace counter
    return est_init__


def pcur_maker(dict__, est_init__):
    lim = 12
    for key in range(len(dict__)):
        ve = dict__[key].ve
        pcur = dict__[key].pcur
        for i in range(0, lim):
            est_init__[ve[i]] += pcur[i]
    return est_init__


def vdgen(dict__, dnest):
    #print(dict__)
    #print(dnest[0])
    for key in dict__:
        ve = key.ve
        #print(ve)
        vdgen_p = [0]*12
        k = 0
        for i in ve:
            if i == 0:
                pass
            else:
                #print(i-1)
                #print(dnest[0,i-1])
                vdgen_p[k] = dnest[0,i-1]
            k += 1
        key.vd = vdgen_p
    return True


def p_global(dict__):
    for key in dict__:
        p = np.dot(key.kebg,key.vd).reshape(-1  )
        key.p_glob = p[0].tolist()[0]
    return True


def fuerza_local(dict__):
    for key in dict__:
        tr = key.tr
        p = key.p_glob
        f = np.dot(tr.T,p)
        key.f_local = f[0].tolist()[0]
    return True


def f_real_local(dict__):
    for key in dict__:
        p = np.asarray(key.pculocal)
        f = np.asarray(key.f_local)
        p[6] = - p[6]
        flr = p - f
        key.fr_local = flr.tolist()
    return True


def desp_local(dict__):
    for key in dict__:
        v = key.vd
        t = key.tr
        dl = np.dot(t.T,v)
        key.dlen = dl.tolist()[0]
    return True


def desp_impuesto(dict__, SCC):
    for key in dict__:
        y = [0]*(SCC +1)
        y[0] = -3 * key.dlen[1]
        y[1] = -2 * key.dx * key.dlen[5]
        y[SCC-1] = 2 * key.dx * key.dlen[11]
        y[SCC] = -3 * key.dlen[7]

        key.desp_imp_antes_y = y

        z = [0]*(SCC+1)
        z[0] = 3 * key.dlen[2]
        z[1] = -2 * key.dx * key.dlen[4]
        z[SCC-1] = 2 * key.dx * key.dlen[10]
        z[SCC] = 3 * key.dlen[8]

        desp_imp_y = np.dot(inv(key.kzz), y) * -1
        desp_imp_z = np.dot(inv(key.kyy), z) * -1

        key.d_imp_y = desp_imp_y.tolist()[0]
        key.d_imo_z = desp_imp_z.tolist()[0]
    return True


def d_real(dict__):
    for key in dict__:
        key.dry = (np.asarray(key.d_imp_y) + np.asarray(key.dlyy)).tolist()
        key.drz = (np.asarray(key.d_imo_z) + np.asarray(key.dlzz)).tolist()
    return True


def cortante(dict__, SCC):
    for key in dict__:

        fr = key.fr_local

        def cor__(v__, dr_, a, b, c):
            v_ = [0] * (SCC + 1)
            for j in range(2, SCC-1):
                v_[j] = (dr_[j + 2] - 2*dr_[j+1] + 2*dr_[j-1] - dr_[j - 2]) * v__

            v_[0] = a * fr[1 + c]
            v_[1] = (v_[0] + v_[2]) / 2
            v_[-1] = b * fr[7 + c]
            v_[-2] = (v_[-1] + v_[-3]) / 2
            return v_

        key.cor_y = cor__(key.vzz, key.dry, -1, 1, 0)
        key.cor_z = cor__(key.vyy, key.drz, 1, -1, 1)

    return True


def momentos(dict__, SCC):
    for key in dict__:
        fr = key.fr_local

        def mome__(dr_, m__, a):

            m_ = [0]*(SCC + 1)

            for j in range(1,SCC):
                m_[j] = (dr_[j +1] - 2*dr_[j] + dr_[j-1]) * m__

            m_[0] = fr[4 + a]
            m_[-1] = -fr[10 + a]

            return m_

        key.mome_y = mome__(key.drz, key.myy, 0)
        key.mome_z = mome__(key.dry, key.mzz, 1)

    return True


def presiones(dict__, SCC):
    for key in dict__:

        def pres__(dr_, k_):
            p_ = [0] * (SCC + 1)
            for i in range(len(p_)):
                p_[i] = dr_[i] * k_ * 10

            return p_

        key.press_y = pres__(key.dry, key.kv)
        key.press_z = pres__(key.drz, key.kh)

    return True


def fuerza_axial(dict__, SCC):
    for key in dict__:
        fr = key.fr_local
        print(fr)

        f_ = [0]*(SCC + 1)
        print(f_)

        f_[0] = key.fr_local[6]
        print(f_)

        for i in range(1, SCC+1):
            print(i)
            f_[i] = f_[i - 1] - key.pp_scc
            print(f_[i])
        key.fax = f_
    return True

