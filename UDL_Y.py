import numpy as np
import math
import copy as cp
#casos de material

L_Y = 0 #load distribution in Y
I_PP = 0
    #steel
#sección "i"
SCC = 0
FY = 0
MY = 0
E = 0
DX = 0
PU_Y = np.matrix.zeros(shape=(0, SCC + 1))
M_DL_Y = cp.deepcopy(PU_Y)
V_DL_Y = cp.deepcopy(PU_Y)
W_SCC_Y = (((L_Y * LE) / 100) / SCC) * (DX ** 3 / (E * IY))

while I_PU <= SCC + 1:
    if I_PU == 0:
        PU_Y[0] = 0
    elif I_PU == SCC:
        PU_Y[SCC] = 0
    elif I_PU != 0 and I_PU != SCC + 1:
        PU_Y[I_PU] = W_SCC_Y
    I_PU += 1

DL_Y = FY * PU_Y

DL_Y_MINUS_2 = (8 * DL_Y[1]) - DL_Y[2]

DL_Y_MINUS_1 = DL_Y[1]

DL_Y_PLUS_1 = DL_Y[SCC - 1]

DL_Y_PLUS_2 = (8 * DL_Y[SCC - 1]) - DL_Y[SCC - 2]


I_TWO = 0
while I_TWO <= SCC:
    if I_TWO == 0:
        M_DL_Y[0] = (DL_Y[1] - (2 * DL_Y[0]) + DL_Y_MINUS_1) * MY
    elif I_TWO == SCC:
        M_DL_Y[SCC] = (DL_Y_PLUS_1 - (2 * DL_Y[SCC]) + DL_Y_MINUS_1) * MY
    elif I_TWO != 0 and I_TWO != SCC:
        M_DL_Y[I_TWO] = (DL_Y[I_TWO + 1] - (2 * DL_Y[I_TWO]) + DL_Y[I_TWO - 1]) * MY
    I_TWO += 1

I_THREE = 0
while I_THREE <= SCC:
    if I_THREE == 0:
        V_DL_Y[0] = ((DL_Y[2] - (2 * DL_Y[1]) + (2 * DL_Y_MINUS_1) - DL_Y_MINUS_2) * VY) + ((PU_Y[1] / 2) * (E * IY) / DX ** 3) #EXTREMO 1
    elif I_THREE == SCC:
        V_DL_Y[SCC] = (DL_Y_PLUS_2 - (2 * DL_Y_PLUS_1) + (2 * DL_Y[SCC - 1]) - DL_Y[SCC - 2] * VY) - ((PU_Y[1] / 2) * (E * IY) / DX ** 3)#EXTREMO 2
    elif I_THREE != 0 and I_THREE != SCC:
        V_DL_Y[I_THREE] = (DL_Y[I_THREE + 2] - (2 * DL_Y[I_THREE + 1]) + (2 * DL_Y[I_THREE - 1]) - DL_Y[I_THREE - 2]) * VY
    I_THREE += 1
