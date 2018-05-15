"""
Archivo con la función para crear las matricez hasta la KEBG
"""
from numpy import matlib as mlib
import copy as cp
import numpy as np
import math
def kebg(A, B, SCC, DX, POISSON, NU, LM, MZ, MY, VZ, VY, AXIAL, T):

    KZ = mlib.zeros(shape=(SCC + 1, SCC + 1))
    F_1Z = mlib.zeros(shape=(SCC + 1, 1))
    T_F_1Z = cp.deepcopy(F_1Z)
    F_2Z = cp.deepcopy(F_1Z)
    T_F_2Z = cp.deepcopy(F_1Z)
    I_M = 0
    CYCLE = 0
    C = 0
    while CYCLE <= 1:
        if CYCLE == 0:
            C = cp.copy(B)
        else:
            C = cp.copy(A)
        while I_M <= SCC:
            if I_M != SCC and I_M != 0 and I_M != 1 and I_M != SCC - 1:
                KZ[I_M, I_M - 2] = 1
                KZ[I_M, I_M - 1] = -4
                KZ[I_M, I_M] = 6 + C
                KZ[I_M, I_M + 1] = -4
                KZ[I_M, I_M + 2] = 1
            elif I_M == 0:
                KZ[0, 0] = 3
                F_1Z[0, 0] = 3
            elif I_M == SCC:
                KZ[SCC, SCC] = 3
            elif I_M == 1:
                KZ[1, 1] = 7 + C
                KZ[1, 0] = -4
                KZ[1, 2] = -4
                KZ[1, 3] = 1
                T_F_1Z[1, 0] = 2 * DX
            elif I_M == SCC - 1:
                KZ[SCC - 1, SCC - 1] = 7 + C
                KZ[SCC - 1, SCC] = -4
                KZ[SCC - 1, SCC - 2] = -4
                KZ[SCC - 1, SCC - 3] = 1
                T_F_2Z[SCC - 1, 0] = 2 * DX
            if I_M == SCC:
                KZ[SCC, SCC] = 3
                F_2Z[SCC, 0] = 3
            I_M += 1
        D_1Z = - KZ.I * F_1Z #debug inverted values
        T_E1Z = - np.dot(KZ.I, T_F_1Z)
        D_2Z = - np.dot(KZ.I, F_2Z)
        T_E2Z = - np.dot(KZ.I, T_F_2Z)
        D_1Z_MINUS_2 = - D_1Z[2] + (8 * D_1Z[1]) - (6 * D_1Z[0])
        D_1Z_MINUS_1 = D_1Z[1]
        D_1Z_PLUS_1 = D_1Z[SCC - 1]
        D_1Z_PLUS_2 = (8 * D_1Z[SCC - 1]) - D_1Z[SCC - 2]
        T_E1Z_MINUS_2 = - T_E1Z[2] + (8 * T_E1Z[1]) + (8 * DX)
        T_E1Z_MINUS_1 = (2 * DX) + T_E1Z[1]
        T_E1Z_PLUS_1 = T_E1Z[SCC - 1]
        T_E1Z_PLUS_2 = (8 * T_E1Z[SCC - 1]) - T_E1Z[SCC - 2]
        D_2Z_MINUS_2 = (8 * D_2Z[1]) - D_2Z[2]
        D_2Z_MINUS_1 = D_2Z[1]
        D_2Z_PLUS_1 = D_2Z[SCC - 1]
        D_2Z_PLUS_2 = - D_2Z[SCC - 2] + (8 * D_2Z[SCC - 1]) - (6 * D_2Z[SCC])
        T_E2Z_MINUS_2 = (8 * T_E2Z[1]) - T_E2Z[2]
        T_E2Z_MINUS_1 = T_E2Z[1]
        T_E2Z_PLUS_1 = ((2 * DX) + T_E2Z[SCC - 1])
        T_E2Z_PLUS_2 = - T_E2Z[SCC - 2] + (8 * T_E2Z[SCC - 1]) + (8 * DX)
        #print(KZ) #"debug"
        if CYCLE == 0:
            #print("Debug")
            KY = cp.deepcopy(KZ)
            D_1Y = cp.deepcopy(D_1Z)
            D_1Y_MINUS_2 = cp.deepcopy(D_1Z_MINUS_2)
            D_1Y_MINUS_1 = cp.deepcopy(D_1Z_MINUS_1)
            D_1Y_PLUS_1 = cp.deepcopy(D_1Z_PLUS_1)
            D_1Y_PLUS_2 = cp.deepcopy(D_1Z_PLUS_2)
            D_2Y = cp.deepcopy(D_2Z)
            D_2Y_MINUS_2 = cp.deepcopy(D_2Z_MINUS_2)
            D_2Y_MINUS_1 = cp.deepcopy(D_2Z_MINUS_1)
            D_2Y_PLUS_1 = cp.deepcopy(D_2Z_PLUS_1)
            D_2Y_PLUS_2 = cp.deepcopy(D_2Z_PLUS_2)
            T_E2Y = cp.deepcopy(T_E2Z)
            T_E2Y_MINUS_2 = cp.deepcopy(T_E2Z_MINUS_2)
            T_E2Y_MINUS_1 = cp.deepcopy(T_E2Z_MINUS_1)
            T_E2Y_PLUS_2 = cp.deepcopy(T_E2Z_PLUS_2)
            T_E2Y_PLUS_1 = cp.deepcopy(T_E2Z_PLUS_1)
            T_E1Y = cp.deepcopy(T_E1Z)
            T_E1Y_MINUS_2 = cp.deepcopy(T_E1Z_MINUS_2)
            T_E1Y_MINUS_1 = cp.deepcopy(T_E1Z_MINUS_1)
            T_E1Y_PLUS_2 = cp.deepcopy(T_E1Z_PLUS_2)
            T_E1Y_PLUS_1 = cp.deepcopy(T_E1Z_PLUS_1)
        I_M = 0
        CYCLE += 1
    I_VM = 0
    M_1Z = mlib.zeros(shape=(SCC + 1, 1))
    T_M_1Z = cp.deepcopy(M_1Z)
    M_2Z = cp.deepcopy(M_1Z)
    T_M_2Z = cp.deepcopy(M_1Z)
    M_1Y = cp.deepcopy(M_1Z)
    T_M_1Y = cp.deepcopy(M_1Z)
    M_2Y = cp.deepcopy(M_1Z)
    T_M_2Y = cp.deepcopy(M_1Z)

    V_1Z = cp.deepcopy(M_1Z)
    V_2Z = cp.deepcopy(M_1Z)
    T_V_1Z = cp.deepcopy(M_1Z)
    T_V_2Z = cp.deepcopy(M_1Z)

    V_1Y = cp.deepcopy(M_1Z)
    V_2Y = cp.deepcopy(M_1Z)
    T_V_1Y = cp.deepcopy(M_1Z)
    T_V_2Y = cp.deepcopy(M_1Z)

    while I_VM <= SCC:
        if I_VM == 0:
            M_1Z[I_VM] = (D_1Z[1] - (2 * D_1Z[0]) +  D_1Z_MINUS_1) * MZ
            T_M_1Z[I_VM] = (T_E1Z[1] - (2 * T_E1Z[0]) +  T_E1Z_MINUS_1) * MZ

            M_2Z[I_VM] = (D_2Z[1] - (2 * D_2Z[0]) +  D_2Z_MINUS_1) * MZ
            T_M_2Z[I_VM] = (T_E2Z[1] - (2 * T_E2Z[0]) +  T_E2Z_MINUS_1) * MZ

            M_1Y[I_VM] = (D_1Y[1] - (2 * D_1Y[0]) +  D_1Y_MINUS_1) * MY
            T_M_1Y[I_VM] = (T_E1Y[1] - (2 * T_E1Y[0]) +  T_E1Y_MINUS_1) * MY

            M_2Y[I_VM] = (D_2Y[1] - (2 * D_2Y[0]) +  D_2Y_MINUS_1) * MY
            T_M_2Y[I_VM] = (T_E2Y[1] - (2 * T_E2Y[0]) +  T_E2Y_MINUS_1) * MY

        elif I_VM != 0 and I_VM != SCC:
            M_1Z[I_VM] = (D_1Z[I_VM + 1] - (2 * D_1Z[I_VM]) +  D_1Z[I_VM - 1]) * MZ
            T_M_1Z[I_VM] = (T_E1Z[I_VM + 1] - (2 * T_E1Z[I_VM]) +  T_E1Z[I_VM - 1]) * MZ

            M_2Z[I_VM] = (D_2Z[I_VM + 1] - (2 * D_2Z[I_VM]) +  D_2Z[I_VM - 1]) * MZ
            T_M_2Z[I_VM] = (T_E2Z[I_VM + 1] - (2 * T_E2Z[I_VM]) +  T_E2Z[I_VM - 1]) * MZ

            M_1Y[I_VM] = (D_1Y[I_VM + 1] - (2 * D_1Y[I_VM]) +  D_1Y[I_VM - 1]) * MY
            T_M_1Y[I_VM] = (T_E1Y[I_VM + 1] - (2 * T_E1Y[I_VM]) +  T_E1Y[I_VM - 1]) * MY

            M_2Y[I_VM] = (D_2Y[I_VM + 1] - (2 * D_2Y[I_VM]) +  D_2Y[I_VM - 1]) * MY
            T_M_2Y[I_VM] = (T_E2Y[I_VM + 1] - (2 * T_E2Y[I_VM]) +  T_E2Y[I_VM - 1]) * MY

        elif I_VM == SCC:
            M_1Z[I_VM] = (D_1Z_PLUS_1 - (2 * D_1Z[I_VM]) +  D_1Z[I_VM - 1]) * MZ
            T_M_1Z[I_VM] = (T_E1Z_PLUS_1 - (2 * T_E1Z[I_VM]) +  T_E1Z[I_VM - 1]) * MZ

            M_2Z[I_VM] = (D_2Z_PLUS_1 - (2 * D_2Z[I_VM]) +  D_2Z[I_VM - 1]) * MZ
            T_M_2Z[I_VM] = (T_E2Z_PLUS_1 - (2 * T_E2Z[I_VM]) +  T_E2Z[I_VM - 1]) * MZ

            M_1Y[I_VM] = (D_1Y_PLUS_1 - (2 * D_1Y[I_VM]) +  D_1Y[I_VM - 1]) * MY
            T_M_1Y[I_VM] = (T_E1Y_PLUS_1 - (2 * T_E1Y[I_VM]) +  T_E1Y[I_VM - 1]) * MY

            M_2Y[I_VM] = (D_2Y_PLUS_1 - (2 * D_2Y[I_VM]) +  D_2Y[I_VM - 1]) * MY
            T_M_2Y[I_VM] = (T_E2Y_PLUS_1 - (2 * T_E2Y[I_VM]) +  T_E2Y[I_VM - 1]) * MY
        I_VM += 1

    I_VC = 0
    I_P2 = I_VC + 2
    I_P1 = I_VC + 1
    I_M1 = I_VC - 1
    I_M2 = I_VC - 2
    D_1Z_ONE = (D_1Z[I_P2] - (2 * D_1Z[I_P1]))
    D_2Z_TWO = (D_2Z[I_P2] - (2 * D_2Z[I_P1]))
    T_1Z_THREE = T_E1Z[I_P2] - (2 * T_E1Z[I_P1])
    T_2Z_FOUR = T_E2Z[I_P2] - (2 * T_E2Z[I_P1])
    D_1Y_FIVE = D_1Y[I_P2] - (2 * D_1Y[I_P1])
    D_2Y_SIX = D_2Y[I_P2] - (2 * D_2Y[I_P1])
    T_1Y_SEVEN = T_E1Y[I_P2] - (2 * T_E1Y[I_P1])
    T_2Y_EIGHT = T_E2Y[I_P2] - (2 * T_E2Y[I_P1])
    D_1Z_VZ = ((2 * D_1Z[I_M1]) - D_1Z[I_M2]) * VZ
    D_2Z_VZ = ((2 * D_2Z[I_M1]) - D_2Z[I_M2]) * VZ
    T_1Z_VZ = ((2 * T_E1Z[I_M1]) - T_E1Z[I_M2]) * VZ
    T_2Z_VZ = ((2 * T_E2Z[I_M1]) - T_E2Z[I_M2]) * VZ
    D_1Y_VY = ((2 * D_1Y[I_M1]) - D_1Y[I_M2]) * VY
    D_2Y_VY = ((2 * D_2Y[I_M1]) - D_2Y[I_M2]) * VY
    T_1Y_VY = ((2 * T_E1Y[I_M1]) - T_E1Y[I_M2]) * VY
    T_2Y_VY = ((2 * T_E2Y[I_M1]) - T_E2Y[I_M2]) * VY

    while I_VC <= SCC:
        if I_VC == 0:
            V_1Z[I_VC] = D_1Z_ONE + (2 * D_1Z_MINUS_1) - D_1Z_MINUS_2 * VZ
            V_2Z[I_VC] = D_2Z_TWO + (2 * D_2Z_MINUS_1) - D_2Z_MINUS_2 * VZ
            T_V_1Z[I_VC] = T_1Z_THREE + (2 * T_E1Z_MINUS_1) - T_E1Z_MINUS_2 * VZ
            T_V_2Z[I_VC] = T_2Z_FOUR + (2 * T_E2Z_MINUS_1) - T_E2Z_MINUS_2 * VZ

            V_1Y[I_VC] = (D_1Y_FIVE + (2 * D_1Y_MINUS_1) - D_1Y_MINUS_2) * VY
            V_2Y[I_VC] = (D_2Y_SIX + (2 * D_2Y_MINUS_1) - D_2Y_MINUS_2) * VY
            T_V_1Y[I_VC] = (T_1Y_SEVEN + (2 * T_E1Y_MINUS_1) - T_E1Y_MINUS_2) * VY
            T_V_2Y[I_VC] = (T_2Y_EIGHT + (2 * T_E2Y_MINUS_1) - T_E2Y_MINUS_2) * VY

        elif I_VC == 1:
            V_1Z[I_VC] = D_1Z_ONE + (2 * D_1Z[0]) - D_1Z_MINUS_1 * VZ
            V_2Z[I_VC] = D_2Z_TWO + (2 * D_2Z[0]) - D_2Z_MINUS_1 * VZ
            T_V_1Z[I_VC] = T_1Z_THREE + (2 * T_E1Z[0]) - T_E1Z_MINUS_1 * VZ
            T_V_2Z[I_VC] = T_2Z_FOUR + (2 * T_E2Z[0]) - T_E2Z_MINUS_1 * VZ

            V_1Y[I_VC] = (D_1Y_FIVE + (2 * D_1Y[0]) - D_1Y_MINUS_1) * VY
            V_2Y[I_VC] = (D_2Y_SIX + (2 * D_2Y[0]) - D_2Y_MINUS_1) * VY
            T_V_1Y[I_VC] = (T_1Y_SEVEN + (2 * T_E1Y[0]) - T_E1Y_MINUS_1) * VY
            T_V_2Y[I_VC] = (T_2Y_EIGHT + (2 * T_E2Y[0]) - T_E2Y_MINUS_1) * VY

        elif I_VC != 0 and I_VC != 1 and I_VC != SCC and I_VC != SCC - 1:
            V_1Z[I_VC] = D_1Z_ONE + (2 * D_1Z[I_M1]) - D_1Z[I_M2] * VZ
            V_2Z[I_VC] = D_2Z_TWO + (2 * D_2Z[I_M1]) - D_2Z[I_M2] * VZ
            T_V_1Z[I_VC] = T_1Z_THREE + (2 * T_E1Z[I_M1]) - T_E1Z[I_M2] * VZ
            T_V_2Z[I_VC] = T_2Z_FOUR + (2 * T_E2Z[I_M1]) - T_E2Z[I_M2] * VZ

            V_1Y[I_VC] = D_1Y_FIVE + D_1Y_VY
            V_2Y[I_VC] = D_2Y_SIX + D_2Y_VY
            T_V_1Y[I_VC] = T_1Y_SEVEN + T_1Y_VY
            T_V_2Y[I_VC] = T_2Y_EIGHT + T_2Y_VY

        if I_VC == SCC - 1:
            V_1Z[I_VC] = D_1Z_PLUS_1 - (2 * D_1Z[SCC]) + D_1Z_VZ
            V_2Z[I_VC] = D_2Z_PLUS_1 - (2 * D_2Z[SCC]) + D_2Z_VZ
            T_V_1Z[I_VC] = T_E1Z_PLUS_1 - (2 * T_E1Z[SCC]) + T_1Z_VZ
            T_V_2Z[I_VC] = T_E2Z_PLUS_1 - (2 * T_E2Z[SCC]) + T_2Z_VZ

            V_1Y[I_VC] = D_1Y_PLUS_1 - (2 * D_1Y[SCC]) + D_1Y_VY
            V_2Y[I_VC] = D_2Y_PLUS_1 - (2 * D_2Y[SCC]) + D_2Y_VY
            T_V_1Y[I_VC] = T_E1Y_PLUS_1 - (2 * T_E1Y[SCC]) + T_1Y_VY
            T_V_2Y[I_VC] = T_E2Y_PLUS_1 - (2 * T_E2Y[SCC]) + T_2Y_VY

        elif I_VC == SCC:
            V_1Z[I_VC] = D_1Z_PLUS_2 - (2 * D_1Z_PLUS_1) + D_1Z_VZ
            V_2Z[I_VC] = D_2Z_PLUS_2 - (2 * D_2Z_PLUS_1) + D_2Z_VZ
            T_V_1Z[I_VC] = T_E1Z_PLUS_2 - (2 * T_E1Z_PLUS_1) + T_1Z_VZ
            T_V_2Z[I_VC] = T_E2Z_PLUS_2 - (2 * T_E2Z_PLUS_1) + T_2Z_VZ

            V_1Y[I_VC] = D_1Y_PLUS_2 - (2 * D_1Y_PLUS_1) + D_1Y_VY
            V_2Y[I_VC] = D_2Y_PLUS_2 - (2 * D_2Y_PLUS_1) + D_2Y_VY
            T_V_1Y[I_VC] = T_E1Y_PLUS_2 - (2 * T_E1Y_PLUS_1) + T_1Y_VY
            T_V_2Y[I_VC] = T_E2Y_PLUS_2 - (2 * T_E2Y_PLUS_1) + T_2Y_VY

        I_VC += 1

    KEB = mlib.zeros(shape=(12, 12))
    #KEB = np.zeros(shape=(12,12))
    T_R = cp.deepcopy(KEB)
        #region one
    KEB[0, 0] = AXIAL
    KEB[1, 1] = - V_1Z[0]
    KEB[1, 5] = - T_V_1Z[0]
    KEB[2, 2] = - V_1Y[0]
    KEB[2, 4] = T_V_1Y[0]
    KEB[3, 3] = T
    KEB[4, 2] = - M_1Y[0]
    KEB[4, 4] = T_M_1Y[0]
    KEB[5, 1] = M_1Z[0]
    KEB[5, 5] = T_M_1Z[0]
        #region two
    KEB[6, 0] = - AXIAL
    KEB[7, 1] = V_1Z[SCC]
    KEB[7, 5] = T_V_1Z[SCC]
    KEB[8, 2] = V_1Y[SCC]
    KEB[8, 4] = - T_V_1Y[SCC]
    KEB[9, 3] = - T
    KEB[10, 2] = M_1Y[SCC]
    KEB[10, 4] = - T_M_1Y[SCC]
    KEB[11, 1] = - M_1Z[SCC]
    KEB[11, 5] = - T_M_1Z[SCC]
        #region three
    KEB[0, 6] = - AXIAL
    KEB[1, 7] = - V_2Z[0]
    KEB[2, 11] = T_V_2Z[0]
    KEB[2, 8] = - V_2Y[0]
    KEB[2, 10] = - T_V_2Y[0]
    KEB[3, 9] = - T
    KEB[4, 8] = - M_2Y[0]
    KEB[4, 10] = - T_M_2Y[0]
    KEB[5, 7] = M_2Z[0]
    KEB[5, 11] = - T_M_2Z[0]
        #region four
    KEB[6, 6] = AXIAL
    KEB[7, 7] = V_2Z[SCC]
    KEB[7, 11] = - T_V_2Z[SCC]
    KEB[8, 8] = V_2Y[SCC]
    KEB[8, 10] = T_V_2Y[SCC]
    KEB[9, 9] = T
    KEB[10, 8] = M_2Y[SCC]
    KEB[10, 10] = T_M_2Y[SCC]
    KEB[11, 7] = - M_2Z[SCC]
    KEB[11, 11] = T_M_2Z[SCC]
    #rotational matrix
    #region one
    COS_NU = math.cos(math.radians(NU))
    SIN_NU = math.sin(math.radians(NU))
    COS_LM = math.cos(math.radians(LM))
    SIN_LM = math.sin(math.radians(LM))

    T_R[0, 0] = COS_NU * COS_LM
    T_R[0, 1] = - COS_NU * SIN_LM
    T_R[0, 2] = - SIN_NU
    T_R[1, 0] = SIN_LM
    T_R[1, 1] = COS_LM
    T_R[2, 0] = SIN_NU * COS_LM
    T_R[2, 1] = - SIN_NU * SIN_LM
    T_R[2, 2] = COS_NU
    T_R[3, 3] = COS_NU * COS_LM
    T_R[3, 4] = - COS_NU * SIN_LM
    T_R[3, 5] = - SIN_NU
    T_R[4, 3] = SIN_LM
    T_R[4, 4] = COS_LM
    T_R[5, 3] = SIN_NU * COS_LM
    T_R[5, 4] = - SIN_NU * SIN_LM
    T_R[5, 5] = COS_NU
    #regn,i two
    T_R[6, 6] = COS_NU * COS_LM
    T_R[6, 7] = - COS_NU * SIN_LM
    T_R[6, 8] = - SIN_NU
    T_R[7, 6] = SIN_LM
    T_R[7, 7] = COS_LM
    T_R[8, 6] = SIN_NU * COS_LM
    T_R[8, 7] = - SIN_NU * SIN_LM
    T_R[8, 8] = COS_NU
    T_R[9, 9] = COS_NU * COS_LM
    T_R[9, 10] = - COS_NU * SIN_LM
    T_R[9, 11] = - SIN_NU
    T_R[10, 9] = SIN_LM
    T_R[10, 10] = COS_LM
    T_R[11, 9] = SIN_NU * COS_LM
    T_R[11, 10] = - SIN_NU * SIN_LM
    T_R[11, 11] = COS_NU

    KEBG = np.dot(np.dot(T_R, KEB), T_R.T)

    return D_1Z_ONE