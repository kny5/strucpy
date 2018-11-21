import math
import numpy as np
from numpy import matlib
def PCU_R(area, p_mat, l, lm, SCC, dx, e, izz, wy, wz, aw, iyy, KZZ, KYY, MZZ, MYY, VZZ, VYY, T_R):

    pp = area * (p_mat / 10000)
    p_axial = ((- math.sin(math.radians(lm)) * pp * (l / 100)) / 2) + ((- math.sin(math.radians(aw)) * wy * (l / 100)) / 2)
    p_scc_y = ((pp * (l / 100) * (math.cos(math.radians(lm)))) / SCC) * ((dx ** 3) / (e * izz))
    p_scc_z = 0
    w_scc_y = ((((wy * l) / 100) * math.cos(math.radians(aw))) / SCC) * ((dx ** 3)/(e * izz))
    w_scc_z = ((wz * (l /100)) / SCC) * ((dx ** 3) / (e * iyy))
    FACTOR1 = (e * izz) / (dx ** 3)
    FACTOR2 = (e * iyy) / (dx ** 3)

    def VectorConst1(thing1, thing2):
        vector = np.matlib.zeros(shape=(SCC + 1, 1))
        I = 0
        while I <= SCC:
            if I != 0 and I != SCC:
                vector[I] = thing1 +  thing2
            I += 1
        return vector

    def VectorConst2(DL, M, MINUS_1, PLUS_1):
        vector = np.matlib.zeros(shape=(SCC + 1, 1))
        I = 0
        while I <= SCC:
            if I == 0:
                vector[I] = (DL[1] - (2 * DL[0]) + MINUS_1) * M
            if I != 0 and I != SCC:
                vector[I] = (DL[I + 1] - (2 * DL[I]) + DL[I - 1]) * M
            if I == SCC:
                vector[SCC] = (DL[SCC - 1] - (2 * DL[SCC]) + PLUS_1) * M
            I += 1
        return vector

    def VectorConst3(DL, MINUS_1, MINUS_2, PLUS_1, PLUS_2, V, vplocal, FACTOR):
        vector = np.matlib.zeros(shape=(SCC + 1, 1))
        I = 0
        while I <= SCC:
            if I == 0:
                vector[I] = ((DL[2] - (2 * DL[1]) + (2 * MINUS_1) - MINUS_2) * V) + ((vplocal[1] / 2) * FACTOR)
            if I == 1:
                vector[I] = (DLY[I + 2] - (2 * DLY[I + 1]) + (2 * DL[I - 1]) - MINUS_1) * V
            if I != 0 and I != SCC and I != 1 and I != SCC - 1:
                vector[I] = (DL[I + 2] - (2 * DL[I + 1]) + (2 * DL[I - 1]) - DL[I - 2]) * V
            if I == SCC -1:
                vector[I] = (PLUS_1 - (2 * DL[I + 1]) + (2 * DL[I - 1]) - DL[I - 2]) * V
            if I == SCC:
                vector[SCC] = ((PLUS_2 - (2 * PLUS_1) + (2 * DL[SCC - 1]) - DL[SCC - 2]) * V) - ((vplocal[1] / 2) * FACTOR)
            I += 1
        return vector

    vplocal_y = VectorConst1(p_scc_y, w_scc_y)
    vplocal_z = VectorConst1(p_scc_z, w_scc_z)

    DLZ = (KYY.I * vplocal_z) * - 1
    DLY = (KZZ.I * vplocal_y) * - 1
    DL_Y_MINUS_2 = (8 * DLY[1]) - DLY[2]
    DL_Y_MINUS_1 = DLY[1]
    DL_Y_PLUS_1 = DLY[SCC - 1]
    DL_Y_PLUS_2 = (8 * DLY[SCC - 1]) - DLY[SCC - 2]
    DL_Z_MINUS_2 = (8 * DLZ[1]) - DLZ[2]
    DL_Z_MINUS_1 = DLZ[1]
    DL_Z_PLUS_1 = DLZ[SCC - 1]
    DL_Z_PLUS_2 = (8 * DLZ[SCC - 1]) - DLZ[SCC - 2]
    M_DLY = VectorConst2(DLY, MZZ, DL_Y_MINUS_1, DL_Y_PLUS_1)
    M_DLZ = VectorConst2(DLZ, MYY, DL_Z_MINUS_1, DL_Z_PLUS_1)
    V_DLY = VectorConst3(DLY, DL_Y_MINUS_1, DL_Y_MINUS_2, DL_Y_PLUS_1, DL_Y_PLUS_2, VZZ, vplocal_y, FACTOR1)
    V_DLZ = VectorConst3(DLZ, DL_Z_MINUS_1, DL_Z_MINUS_2, DL_Z_PLUS_1, DL_Z_PLUS_2, VYY, vplocal_z, FACTOR2)

    ################################################

    PCULOCAL = np.matlib.zeros(shape=(12, 1))
    PCULOCAL[0] = p_axial
    PCULOCAL[1] = - V_DLY[0]
    PCULOCAL[2] = - DLZ[0]
    PCULOCAL[3] = 0
    PCULOCAL[4] = - M_DLZ[0]
    PCULOCAL[5] = M_DLY[0]
    PCULOCAL[6] = p_axial
    PCULOCAL[7] = V_DLY[SCC]
    PCULOCAL[8] = V_DLZ[SCC]
    PCULOCAL[9] = 0
    PCULOCAL[10] = M_DLZ[SCC]
    PCULOCAL[11] = - M_DLY[SCC]
    PCU_R = np.dot(T_R, PCULOCAL)

    return PCU_R

