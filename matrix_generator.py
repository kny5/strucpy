"""
Archivo con la función para crear las matricez hasta la KEBG
"""
from copy import deepcopy as dcopy
from copy import copy as cp
import numpy as np
import math

def kebg_pcur(object):
    """ FUNCIÓN kebg"""
    A = object.A()
    B = object.B()
    D_X = object.dx()
    NU = object.nu
    LM = object.lm
    MZZ = object.mzz()
    MYY = object.myy()
    VZZ = object.vzz()
    VYY = object.vyy()
    AXIAL = object.axial()
    T = object.torsion()
    area = object.area()
    p_mat = object.p_mat
    l = object.l
    e = object.e
    izz = object.izz()
    wy = object.wy
    wz = object.wz
    aw = object.aw
    iyy = object.iyy()
    SCC = object.SCC
    POISSON = object.POISSON

    KZZ = np.matlib.zeros(shape=((SCC + 1), (SCC + 1)))
    F_1ZZ = np.matlib.zeros(shape=((SCC + 1), 1))
    T_F_1ZZ = dcopy(F_1ZZ)
    F_2ZZ = dcopy(F_1ZZ)
    T_F_2ZZ = dcopy(F_1ZZ)
    I_M = 0
    CYCLE = 0
    C = 0
    while CYCLE <= 1:
        if CYCLE == 0:
            C = cp(B)
        else:
            C = cp(A)
        while I_M <= SCC:
            if I_M != SCC and I_M != 0 and I_M != 1 and I_M != SCC - 1:
                KZZ[I_M,I_M - 2] = 1
                KZZ[I_M,I_M - 1] = -4
                KZZ[I_M,I_M] = 6 + C
                KZZ[I_M,I_M + 1] = -4
                KZZ[I_M,I_M + 2] = 1
            elif I_M == 0:
                KZZ[0,0] = 3
                F_1ZZ[0,0] = 3
            elif I_M == SCC:
                KZZ[SCC,SCC] = 3
            elif I_M == 1:
                KZZ[1,1] = 7 + C
                KZZ[1,0] = -4
                KZZ[1,2] = -4
                KZZ[1,3] = 1
                T_F_1ZZ[1,0] = 2 * D_X
            elif I_M == SCC -1:
                KZZ[SCC - 1,SCC - 1] = 7 + C
                KZZ[SCC - 1,SCC] = -4
                KZZ[SCC - 1,SCC - 2] = -4
                KZZ[SCC - 1,SCC - 3] = 1
                T_F_2ZZ[SCC - 1,0] = 2 * D_X
            if I_M == SCC:
                KZZ[SCC,SCC] = 3
                F_2ZZ[SCC,0] = 3
            I_M += 1
        
        D_1ZZ = - KZZ.I * F_1ZZ #debug inverted values

        T_E1ZZ = - np.dot(KZZ.I, T_F_1ZZ)
        D_2ZZ = - np.dot(KZZ.I, F_2ZZ)
        T_E2ZZ = - np.dot(KZZ.I, T_F_2ZZ)
        D_1ZZ_MINUS_2 = - D_1ZZ[2] + (8 * D_1ZZ[1]) - (6 * D_1ZZ[0])
        D_1ZZ_MINUS_1 = D_1ZZ[1]
        D_1ZZ_PLUS_1 = D_1ZZ[SCC - 1]
        D_1ZZ_PLUS_2 = (8 * D_1ZZ[SCC - 1]) - D_1ZZ[SCC - 2]
        T_E1ZZ_MINUS_2 = - T_E1ZZ[2] + (8 * T_E1ZZ[1]) + (8 * D_X)
        T_E1ZZ_MINUS_1 = (2 * D_X) + T_E1ZZ[1]
        T_E1ZZ_PLUS_1 = T_E1ZZ[SCC - 1]
        T_E1ZZ_PLUS_2 = (8 * T_E1ZZ[SCC - 1]) - T_E1ZZ[SCC - 2]
        D_2ZZ_MINUS_2 = (8 * D_2ZZ[1]) - D_2ZZ[2]
        D_2ZZ_MINUS_1 = D_2ZZ[1]
        D_2ZZ_PLUS_1 = D_2ZZ[SCC - 1]
        D_2ZZ_PLUS_2 = - D_2ZZ[SCC - 2] + (8 * D_2ZZ[SCC - 1]) - (6 * D_2ZZ[SCC])
        T_E2ZZ_MINUS_2 = (8 * T_E2ZZ[1]) - T_E2ZZ[2]
        T_E2ZZ_MINUS_1 = T_E2ZZ[1]
        T_E2ZZ_PLUS_1 = ((2 * D_X) + T_E2ZZ[SCC - 1])
        T_E2ZZ_PLUS_2 = - T_E2ZZ[SCC - 2] + (8 * T_E2ZZ[SCC - 1]) + (8 * D_X)

        if CYCLE == 0:
            KYY = dcopy(KZZ)
            D_1YY = dcopy(D_1ZZ)
            D_1YY_MINUS_2 = dcopy(D_1ZZ_MINUS_2)
            D_1YY_MINUS_1 = dcopy(D_1ZZ_MINUS_1)
            D_1YY_PLUS_1 = dcopy(D_1ZZ_PLUS_1)
            D_1YY_PLUS_2 = dcopy(D_1ZZ_PLUS_2)
            D_2YY = dcopy(D_2ZZ)
            D_2YY_MINUS_2 = dcopy(D_2ZZ_MINUS_2)
            D_2YY_MINUS_1 = dcopy(D_2ZZ_MINUS_1)
            D_2YY_PLUS_1 = dcopy(D_2ZZ_PLUS_1)
            D_2YY_PLUS_2 = dcopy(D_2ZZ_PLUS_2)
            T_E2YY = dcopy(T_E2ZZ)
            T_E2YY_MINUS_2 = dcopy(T_E2ZZ_MINUS_2)
            T_E2YY_MINUS_1 = dcopy(T_E2ZZ_MINUS_1)
            T_E2YY_PLUS_2 = dcopy(T_E2ZZ_PLUS_2)
            T_E2YY_PLUS_1 = dcopy(T_E2ZZ_PLUS_1)
            T_E1YY = dcopy(T_E1ZZ)
            T_E1YY_MINUS_2 = dcopy(T_E1ZZ_MINUS_2)
            T_E1YY_MINUS_1 = dcopy(T_E1ZZ_MINUS_1)
            T_E1YY_PLUS_2 = dcopy(T_E1ZZ_PLUS_2)
            T_E1YY_PLUS_1 = dcopy(T_E1ZZ_PLUS_1)
        I_M = 0
        CYCLE += 1
    I_VM = 0
    M_1ZZ = np.matlib.zeros(shape=((SCC + 1), 1))
    T_M_1ZZ = dcopy(M_1ZZ)
    M_2ZZ = dcopy(M_1ZZ)
    T_M_2ZZ = dcopy(M_1ZZ)
    M_1YY = dcopy(M_1ZZ)
    T_M_1YY = dcopy(M_1ZZ)
    M_2YY = dcopy(M_1ZZ)
    T_M_2YY = dcopy(M_1ZZ)

    V_1ZZ = dcopy(M_1ZZ)
    V_2ZZ = dcopy(M_1ZZ)
    T_V_1ZZ = dcopy(M_1ZZ)
    T_V_2ZZ = dcopy(M_1ZZ)

    V_1YY = dcopy(M_1ZZ)
    V_2YY = dcopy(M_1ZZ)
    T_V_1YY = dcopy(M_1ZZ)
    T_V_2YY = dcopy(M_1ZZ)

    while I_VM <= SCC:
        if I_VM == 0:
            M_1ZZ[I_VM] = (D_1ZZ[1] - (2 * D_1ZZ[0]) +  D_1ZZ_MINUS_1) * MZZ
            T_M_1ZZ[I_VM] = (T_E1ZZ[1] - (2 * T_E1ZZ[0]) +  T_E1ZZ_MINUS_1) * MZZ

            M_2ZZ[I_VM] = (D_2ZZ[1] - (2 * D_2ZZ[0]) +  D_2ZZ_MINUS_1) * MZZ
            T_M_2ZZ[I_VM] = (T_E2ZZ[1] - (2 * T_E2ZZ[0]) +  T_E2ZZ_MINUS_1) * MZZ

            M_1YY[I_VM] = (D_1YY[1] - (2 * D_1YY[0]) +  D_1YY_MINUS_1) * MYY
            T_M_1YY[I_VM] = (T_E1YY[1] - (2 * T_E1YY[0]) +  T_E1YY_MINUS_1) * MYY

            M_2YY[I_VM] = (D_2YY[1] - (2 * D_2YY[0]) +  D_2YY_MINUS_1) * MYY
            T_M_2YY[I_VM] = (T_E2YY[1] - (2 * T_E2YY[0]) +  T_E2YY_MINUS_1) * MYY

        elif I_VM != 0 and I_VM != SCC:
            M_1ZZ[I_VM] = (D_1ZZ[I_VM + 1] - (2 * D_1ZZ[I_VM]) +  D_1ZZ[I_VM - 1]) * MZZ
            T_M_1ZZ[I_VM] = (T_E1ZZ[I_VM + 1] - (2 * T_E1ZZ[I_VM]) +  T_E1ZZ[I_VM - 1]) * MZZ

            M_2ZZ[I_VM] = (D_2ZZ[I_VM + 1] - (2 * D_2ZZ[I_VM]) +  D_2ZZ[I_VM - 1]) * MZZ
            T_M_2ZZ[I_VM] = (T_E2ZZ[I_VM + 1] - (2 * T_E2ZZ[I_VM]) +  T_E2ZZ[I_VM - 1]) * MZZ

            M_1YY[I_VM] = (D_1YY[I_VM + 1] - (2 * D_1YY[I_VM]) +  D_1YY[I_VM - 1]) * MYY
            T_M_1YY[I_VM] = (T_E1YY[I_VM + 1] - (2 * T_E1YY[I_VM]) +  T_E1YY[I_VM - 1]) * MYY

            M_2YY[I_VM] = (D_2YY[I_VM + 1] - (2 * D_2YY[I_VM]) +  D_2YY[I_VM - 1]) * MYY
            T_M_2YY[I_VM] = (T_E2YY[I_VM + 1] - (2 * T_E2YY[I_VM]) +  T_E2YY[I_VM - 1]) * MYY

        elif I_VM == SCC:
            M_1ZZ[I_VM] = (D_1ZZ_PLUS_1 - (2 * D_1ZZ[I_VM]) +  D_1ZZ[I_VM - 1]) * MZZ
            T_M_1ZZ[I_VM] = (T_E1ZZ_PLUS_1 - (2 * T_E1ZZ[I_VM]) +  T_E1ZZ[I_VM - 1]) * MZZ

            M_2ZZ[I_VM] = (D_2ZZ_PLUS_1 - (2 * D_2ZZ[I_VM]) +  D_2ZZ[I_VM - 1]) * MZZ
            T_M_2ZZ[I_VM] = (T_E2ZZ_PLUS_1 - (2 * T_E2ZZ[I_VM]) +  T_E2ZZ[I_VM - 1]) * MZZ

            M_1YY[I_VM] = (D_1YY_PLUS_1 - (2 * D_1YY[I_VM]) +  D_1YY[I_VM - 1]) * MYY
            T_M_1YY[I_VM] = (T_E1YY_PLUS_1 - (2 * T_E1YY[I_VM]) +  T_E1YY[I_VM - 1]) * MYY

            M_2YY[I_VM] = (D_2YY_PLUS_1 - (2 * D_2YY[I_VM]) +  D_2YY[I_VM - 1]) * MYY
            T_M_2YY[I_VM] = (T_E2YY_PLUS_1 - (2 * T_E2YY[I_VM]) +  T_E2YY[I_VM - 1]) * MYY
        I_VM += 1

    I_VC = 0

    while I_VC <= SCC:
        if I_VC == 0:
            V_1ZZ[I_VC] = (D_1ZZ[I_VC + 2] - (2 * D_1ZZ[I_VC + 1]) + (2 * D_1ZZ_MINUS_1) - D_1ZZ_MINUS_2) * VZZ
            V_2ZZ[I_VC] = (D_2ZZ[I_VC + 2] - (2 * D_2ZZ[I_VC + 1]) + (2 * D_2ZZ_MINUS_1) - D_2ZZ_MINUS_2) * VZZ
            T_V_1ZZ[I_VC] = (T_E1ZZ[I_VC + 2] - (2 * T_E1ZZ[I_VC + 1]) + (2 * T_E1ZZ_MINUS_1) - T_E1ZZ_MINUS_2) * VZZ
            T_V_2ZZ[I_VC] = (T_E2ZZ[I_VC + 2] - (2 * T_E2ZZ[I_VC + 1]) + (2 * T_E2ZZ_MINUS_1) - T_E2ZZ_MINUS_2) * VZZ

            V_1YY[I_VC] = (D_1YY[I_VC + 2] - (2 * D_1YY[I_VC + 1]) + (2 * D_1YY_MINUS_1) - D_1YY_MINUS_2) * VYY
            V_2YY[I_VC] = (D_2YY[I_VC + 2] - (2 * D_2YY[I_VC + 1]) + (2 * D_2YY_MINUS_1) - D_2YY_MINUS_2) * VYY
            T_V_1YY[I_VC] = (T_E1YY[I_VC + 2] - (2 * T_E1YY[I_VC + 1]) + (2 * T_E1YY_MINUS_1) - T_E1YY_MINUS_2) * VYY
            T_V_2YY[I_VC] = (T_E2YY[I_VC + 2] - (2 * T_E2YY[I_VC + 1]) + (2 * T_E2YY_MINUS_1) - T_E2YY_MINUS_2) * VYY

        elif I_VC == 1:
            V_1ZZ[I_VC] = (D_1ZZ[I_VC + 2] - (2 * D_1ZZ[I_VC + 1]) + (2 * D_1ZZ[0]) - D_1ZZ_MINUS_1) * VZZ
            V_2ZZ[I_VC] = (D_2ZZ[I_VC + 2] - (2 * D_2ZZ[I_VC + 1]) + (2 * D_2ZZ[0]) - D_2ZZ_MINUS_1) * VZZ
            T_V_1ZZ[I_VC] = (T_E1ZZ[I_VC + 2] - (2 * T_E1ZZ[I_VC + 1]) + (2 * T_E1ZZ[0]) - T_E1ZZ_MINUS_1) * VZZ
            T_V_2ZZ[I_VC] = (T_E2ZZ[I_VC + 2] - (2 * T_E2ZZ[I_VC + 1]) + (2 * T_E2ZZ[0]) - T_E2ZZ_MINUS_1) * VZZ

            V_1YY[I_VC] = (D_1YY[I_VC + 2] - (2 * D_1YY[I_VC + 1]) + (2 * D_1YY[0]) - D_1YY_MINUS_1) * VYY
            V_2YY[I_VC] = (D_2YY[I_VC + 2] - (2 * D_2YY[I_VC + 1]) + (2 * D_2YY[0]) - D_2YY_MINUS_1) * VYY
            T_V_1YY[I_VC] = (T_E1YY[I_VC + 2] - (2 * T_E1YY[I_VC + 1]) + (2 * T_E1YY[0]) - T_E1YY_MINUS_1) * VYY
            T_V_2YY[I_VC] = (T_E2YY[I_VC + 2] - (2 * T_E2YY[I_VC + 1]) + (2 * T_E2YY[0]) - T_E2YY_MINUS_1) * VYY

        elif I_VC != 0 and I_VC != 1 and I_VC != SCC and I_VC != SCC - 1:
            V_1ZZ[I_VC] = (D_1ZZ[I_VC + 2] - (2 * D_1ZZ[I_VC + 1]) + (2 * D_1ZZ[I_VC - 1]) - D_1ZZ[I_VC - 2]) * VZZ
            V_2ZZ[I_VC] = (D_2ZZ[I_VC + 2] - (2 * D_2ZZ[I_VC + 1]) + (2 * D_2ZZ[I_VC - 1]) - D_2ZZ[I_VC - 2]) * VZZ
            T_V_1ZZ[I_VC] = (T_E1ZZ[I_VC + 2] - (2 * T_E1ZZ[I_VC + 1]) + (2 * T_E1ZZ[I_VC - 1]) - T_E1ZZ[I_VC - 2]) * VZZ
            T_V_2ZZ[I_VC] = (T_E2ZZ[I_VC + 2] - (2 * T_E2ZZ[I_VC + 1]) + (2 * T_E2ZZ[I_VC - 1]) - T_E2ZZ[I_VC - 2]) * VZZ

            V_1YY[I_VC] = (D_1YY[I_VC + 2] - (2 * D_1YY[I_VC + 1]) + (2 * D_1YY[I_VC - 1]) - D_1YY[I_VC - 2]) * VYY
            V_2YY[I_VC] = (D_2YY[I_VC + 2] - (2 * D_2YY[I_VC + 1]) + (2 * D_2YY[I_VC - 1]) - D_2YY[I_VC - 2]) * VYY
            T_V_1YY[I_VC] = (T_E1YY[I_VC + 2] - (2 * T_E1YY[I_VC + 1]) + (2 * T_E1YY[I_VC - 1]) - T_E1YY[I_VC - 2]) * VYY
            T_V_2YY[I_VC] = (T_E2YY[I_VC + 2] - (2 * T_E2YY[I_VC + 1]) + (2 * T_E2YY[I_VC - 1]) - T_E2YY[I_VC - 2]) * VYY

        if I_VC == SCC - 1:
            V_1ZZ[I_VC] = (D_1ZZ_PLUS_1 - (2 * D_1ZZ[SCC]) + (2 * D_1ZZ[I_VC - 1]) - D_1ZZ[I_VC - 2]) * VZZ
            V_2ZZ[I_VC] = (D_2ZZ_PLUS_1 - (2 * D_2ZZ[SCC]) + (2 * D_2ZZ[I_VC - 1]) - D_2ZZ[I_VC - 2]) * VZZ
            T_V_1ZZ[I_VC] = (T_E1ZZ_PLUS_1 - (2 * T_E1ZZ[SCC]) + (2 * T_E1ZZ[I_VC - 1]) - T_E1ZZ[I_VC - 2]) * VZZ
            T_V_2ZZ[I_VC] = (T_E2ZZ_PLUS_1 - (2 * T_E2ZZ[SCC]) + (2 * T_E2ZZ[I_VC - 1]) - T_E2ZZ[I_VC - 2]) * VZZ

            V_1YY[I_VC] = (D_1YY_PLUS_1 - (2 * D_1YY[SCC]) + (2 * D_1YY[I_VC - 1]) - D_1YY[I_VC - 2]) * VYY
            V_2YY[I_VC] = (D_2YY_PLUS_1 - (2 * D_2YY[SCC]) + (2 * D_2YY[I_VC - 1]) - D_2YY[I_VC - 2]) * VYY
            T_V_1YY[I_VC] = (T_E1YY_PLUS_1 - (2 * T_E1YY[SCC]) + (2 * T_E1YY[I_VC - 1]) - T_E1YY[I_VC - 2]) * VYY
            T_V_2YY[I_VC] = (T_E2YY_PLUS_1 - (2 * T_E2YY[SCC]) + (2 * T_E2YY[I_VC - 1]) - T_E2YY[I_VC - 2]) * VYY

        elif I_VC == SCC:
            V_1ZZ[I_VC] = (D_1ZZ_PLUS_2 - (2 * D_1ZZ_PLUS_1) + (2 * D_1ZZ[I_VC - 1]) - D_1ZZ[I_VC - 2]) * VZZ
            V_2ZZ[I_VC] = (D_2ZZ_PLUS_2 - (2 * D_2ZZ_PLUS_1) + (2 * D_2ZZ[I_VC - 1]) - D_2ZZ[I_VC - 2]) * VZZ
            T_V_1ZZ[I_VC] = (T_E1ZZ_PLUS_2 - (2 * T_E1ZZ_PLUS_1) + (2 * T_E1ZZ[I_VC - 1]) - T_E1ZZ[I_VC - 2]) * VZZ
            T_V_2ZZ[I_VC] = (T_E2ZZ_PLUS_2 - (2 * T_E2ZZ_PLUS_1) + (2 * T_E2ZZ[I_VC - 1]) - T_E2ZZ[I_VC - 2]) * VZZ

            V_1YY[I_VC] = (D_1YY_PLUS_2 - (2 * D_1YY_PLUS_1) + (2 * D_1YY[I_VC - 1]) - D_1YY[I_VC - 2]) * VYY
            V_2YY[I_VC] = (D_2YY_PLUS_2 - (2 * D_2YY_PLUS_1) + (2 * D_2YY[I_VC - 1]) - D_2YY[I_VC - 2]) * VYY
            T_V_1YY[I_VC] = (T_E1YY_PLUS_2 - (2 * T_E1YY_PLUS_1) + (2 * T_E1YY[I_VC - 1]) - T_E1YY[I_VC - 2]) * VYY
            T_V_2YY[I_VC] = (T_E2YY_PLUS_2 - (2 * T_E2YY_PLUS_1) + (2 * T_E2YY[I_VC - 1]) - T_E2YY[I_VC - 2]) * VYY

        I_VC += 1

    KEB = np.matlib.zeros(shape=(12,12))
    T_R = dcopy(KEB)
        #region one
    KEB[0,0] = AXIAL
    KEB[1,1] = - V_1ZZ[0]
    KEB[1,5] = - T_V_1ZZ[0]
    KEB[2,2] = - V_1YY[0]
    KEB[2,4] = T_V_1YY[0]
    KEB[3,3] = T
    KEB[4,2] = - M_1YY[0]
    KEB[4,4] = T_M_1YY[0]
    KEB[5,1] = M_1ZZ[0]
    KEB[5,5] = T_M_1ZZ[0]
        #region two
    KEB[6,0] = - AXIAL
    KEB[7,1] = V_1ZZ[SCC]
    KEB[7,5] = T_V_1ZZ[SCC]
    KEB[8,2] = V_1YY[SCC]
    KEB[8,4] = - T_V_1YY[SCC]
    KEB[9,3] = - T
    KEB[10,2] = M_1YY[SCC]
    KEB[10,4] = - T_M_1YY[SCC]
    KEB[11,1] = - M_1ZZ[SCC]
    KEB[11,5] = - T_M_1ZZ[SCC]
        #region three
    KEB[0,6] = - AXIAL
    KEB[1,7] = - V_2ZZ[0]
    KEB[1,11] = T_V_2ZZ[0]
    KEB[2,8] = - V_2YY[0]
    KEB[2,10] = - T_V_2YY[0]
    KEB[3,9] = - T
    KEB[4,8] = - M_2YY[0]
    KEB[4,10] = - T_M_2YY[0]
    KEB[5,7] = M_2ZZ[0]
    KEB[5,11] = - T_M_2ZZ[0]
        #region four
    KEB[6,6] = AXIAL
    KEB[7,7] = V_2ZZ[SCC]
    KEB[7,11] = - T_V_2ZZ[SCC]
    KEB[8,8] = V_2YY[SCC]
    KEB[8,10] = T_V_2YY[SCC]
    KEB[9,9] = T
    KEB[10,8] = M_2YY[SCC]
    KEB[10,10] = T_M_2YY[SCC]
    KEB[11,7] = - M_2ZZ[SCC]
    KEB[11,11] = T_M_2ZZ[SCC]
    #rotational matrix
    COS_NU = math.cos(math.radians(NU))
    SIN_NU = math.sin(math.radians(NU))
    COS_LM = math.cos(math.radians(LM))
    SIN_NU = math.sin(math.radians(LM))
    #region one
    T_R[0,0] = COS_NU * COS_LM
    T_R[0,1] = - COS_NU * SIN_NU
    T_R[0,2] = - SIN_NU
    T_R[1,0] = SIN_NU
    T_R[1,1] = COS_LM
    T_R[2,0] = SIN_NU * COS_LM
    T_R[2,1] = - SIN_NU * SIN_NU
    T_R[2,2] = COS_NU
    T_R[3,3] = COS_NU * COS_LM
    T_R[3,4] = - COS_NU * SIN_NU
    T_R[3,5] = - SIN_NU
    T_R[4,3] = SIN_NU
    T_R[4,4] = COS_LM
    T_R[5,3] = SIN_NU * COS_LM
    T_R[5,4] = - SIN_NU * SIN_NU
    T_R[5,5] = COS_NU
    #regn,i two
    T_R[6,6] = COS_NU * COS_LM
    T_R[6,7] = - COS_NU * SIN_NU
    T_R[6,8] = - SIN_NU
    T_R[7,6] = SIN_NU
    T_R[7,7] = COS_LM
    T_R[8,6] = SIN_NU * COS_LM
    T_R[8,7] = - SIN_NU * SIN_NU
    T_R[8,8] = COS_NU
    T_R[9,9] = COS_NU * COS_LM
    T_R[9,10] = - COS_NU * SIN_NU
    T_R[9,11] = - SIN_NU
    T_R[10,9] = SIN_NU
    T_R[10,10] = COS_LM
    T_R[11,9] = SIN_NU * COS_LM
    T_R[11,10] = - SIN_NU * SIN_NU
    T_R[11,11] = COS_NU

    KEBG = np.dot(np.dot(T_R, KEB), T_R.T)

    def PCU_R(area, p_mat, l, lm, SCC, dx, e, izz, wy, wz, aw, iyy, KZZ, KYY, MZZ, MYY, VZZ, VYY, T_R):

        pp = area * (p_mat / 10000)
        p_axial = ((- math.sin(math.radians(lm)) * pp * (l / 100)) / 2) + (
                    (- math.sin(math.radians(aw)) * wy * (l / 100)) / 2)
        p_scc_y = ((pp * (l / 100) * (math.cos(math.radians(lm)))) / SCC) * ((dx ** 3) / (e * izz))
        p_scc_z = 0
        w_scc_y = ((((wy * l) / 100) * math.cos(math.radians(aw))) / SCC) * ((dx ** 3) / (e * izz))
        w_scc_z = ((wz * (l / 100)) / SCC) * ((dx ** 3) / (e * iyy))
        FACTOR1 = (e * izz) / (dx ** 3)
        FACTOR2 = (e * iyy) / (dx ** 3)

        def VectorConst1(thing1, thing2):
            vector = np.matlib.zeros(shape=(SCC + 1, 1))
            I = 0
            while I <= SCC:
                if I != 0 and I != SCC:
                    vector[I] = thing1 + thing2
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
                if I == SCC - 1:
                    vector[I] = (PLUS_1 - (2 * DL[I + 1]) + (2 * DL[I - 1]) - DL[I - 2]) * V
                if I == SCC:
                    vector[SCC] = ((PLUS_2 - (2 * PLUS_1) + (2 * DL[SCC - 1]) - DL[SCC - 2]) * V) - (
                                (vplocal[1] / 2) * FACTOR)
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

    PCUR = PCU_R(area, p_mat, l, LM, SCC, D_X, e, izz, wy, wz, aw, iyy, KZZ, KYY, MZZ, MYY, VZZ, VYY, T_R)

    return {'KEBG':KEBG, 'PCUR':PCUR}

