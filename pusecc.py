import math
import numpy as np
from numpy import matlib
def vplocal(area, p_mat, l, lm, SCC, dx, e, izz, wy, wz, aw, iyy, KZZ, KYY):

    pp = area * (p_mat / 10000)

    p_scc_axial =  (- math.sin(math.radians(lm)) * pp * (l / 100)) / 2

    p_scc_y = ((pp * (l / 100) * math.cos(math.radians(lm))) / SCC) * ((dx ** 3) / (e * izz))

    p_scc_z = 0

    w_scc_y = ((((wy * l) / 100) * math.cos(math.radians(aw))) / SCC) * ((dx ** 3)/(e * izz))

    w_scc_z = ((wz * (l /100)) / SCC) * ((dx ** 3) / (e * iyy))

    def VectorConst(thing1, thing2):
        vector = np.matlib.zeros(shape=(SCC + 1, 1))
        I = 0
        while I <= SCC:
            if I != 0 and I != SCC:
                vector[I] = thing1 +  thing2
            I += 1
        return vector

    vplocal_y = VectorConst(p_scc_y, w_scc_y)

    vplocal_z = VectorConst(p_scc_z, w_scc_z)

    DLZ = KYY.I * vplocal_z

    DLY = KZZ.I * vplocal_y

    DL_Y_MINUS_2 = (8 * DLY[1]) - DLY[2]

    DL_Y_MINUS_1 = DLY[1]

    DL_Y_PLUS_1 = DLY[SCC - 1]

    DL_Y_PLUS_2 = (8 * DLY[SCC - 1]) - DLY[SCC - 2]

    return DLZ
