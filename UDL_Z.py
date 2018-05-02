import numpy as np
import math
import copy as cp
#casos de material
W = 0 #TON/ML
T_LOAD = 0 #LOAD ANGLE
    #concrete
PP = ((BP * HZ) / 10000) * 2.4
#casos de secciones
    #steel
#sección "or"
BF = 0
D = 0
TW = 0
TF = 0
PV_STEEL = 0.0007849
I_PP = 0
PP = ((BF * D) - (BF - 2 * TW) * (D - 2 * TF)) * PV_STEEL
    #steel
#sección "i"
PP = ((BF * TF * 2) + ((D - 2 * TF) * TW)) * PV_STEEL

PU_SCC_Z = (((PP * (LE / 100) * COS_LM) / SCC) * (DX ** 3 / (E * IZ))

P_SCC_AX = - ((SIN_LM * PP * LE) / 100) / 2

PP_SCC = np.matrix.zeros(shape=(0, SCC + 1))
PW_SCC = cp.deepcopy(PP_SCC)
PU_Z = cp.deepcopy(PP_SCC)
M_DL_Z = cp.deepcopy(PP_SCC)
V_DL_Z = cp.deepcopy(PP_SCC)
while I_PP <= SCC + 1:
    if I_PP == 0:
        PP_SCC[0] = 0
    elif I_PP == SCC + 1:
        PP_SCC[SECC + 1] = 0
    elif I_PP != 0 I_PP != SCC + 1:
        PP_SCC[I_PP] = PU_SCC_Z
    I_PP += 1

W_SCC_Z = ((((W * LE) / 100) * math.cos(T_LOAD)) / SCC) * (DX ** 3 / (E * IZ))

PW_AX = - (math.sin(T_LOAD) * W * LE/100) / 2
I_PW = 0
while I_PW <= SCC + 1:
    if I_PW == 0:
        PW_SCC[0] = 0
    elif I_PW == SCC + 1:
        PW_SCC[SECC + 1] = 0
    elif I_PW != 0 I_PW != SCC + 1:
        PW_SCC[I_PW] = W_SCC_Z
    I_PW += 1

PU_Z = PP_SCC + PW_SCC

DL_Z = FZ * PU_Z * - 1

DL_Z_MINUS_2 = (8 * DL_Z[1]) - DL_Z[2]

DL_Z_MINUS_1 = DL_Z[1]

DL_Z_PLUS_1 = DL_Z[SCC - 1]

DL_Z_PLUS_2 = (8 * DL_Z[SCC - 1]) - DL_Z[SCC - 2]


I_M_DL = 0
while I_M_DL <= SCC:
    if I_M_DL == 0:
        M_DL_Z[0] = (DL_Z[1] - (2 * DL_Z[0]) + DL_Z_MINUS_1) * MZ
    elif I_M_DL == SCC:
        M_DL_Z[SCC] = (DL_Z_PLUS_1 - (2 * DL_Z[SCC]) + DL_Z_MINUS_1) * MZ
    elif I_M_DL != 0 I_M_DL != SCC:
        M_DL_Z[I_M_DL] = (DL_Z[I_M_DL + 1] - (2 * DL_Z[I_M_DL]) + DL_Z[I_M_DL - 1]) * MZ
    I_M_DL += 1

I_V_DL = 0
while I_V_DL <= SCC:
    if I_M_DL == 0:
        V_DL_Z[0] =  ((DL_Z[2] - (2 * DL_Z[1]) + (2 * DL_Z_MINUS_1) - DL_Z_MINUS_2) * VZ) + ((PU_Z[1] / 2) * (E * IZ) / DX ** 3) #EXTREMO 1
    elif I_M_DL == SCC:
        V_DL_Z[SCC] = (DL_Z_PLUS_2 - (2 * DL_Z_PLUS_1) + (2 * DL_Z[SCC - 1]) - DL_Z[SCC - 2] * VZ) - ((PU_Z[1] / 2) * (E * IZ) / DX ** 3)#EXTREMO 2
    elif I_M_DL != 0 I_M_DL != SCC:
        V_DL_Z[I_V_DL] = ((DL_Z[I_V_DL + 2] - (2 * DL_Z[I_V_DL + 1]) + (2 * DL_Z[I_V_DL - 1])) - DL_Z[I_V_DL - 2])) * VZ
    I_M_DL += 1
