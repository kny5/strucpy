# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import math
import copy as cp
import numpy as np
from numpy.linalg import inv
from pandas import DataFrame as df
A = 3
B = 5
SCC = 20
D_X = 25
ENE = SCC + 1
IZZ = 3333333.3
IYY = 533333.33
E = 221.359
MZZ = (E * IZZ) / D_X ** 2
MYY = (E * IYY) / (D_X ** 2)
VZZ = (E * IZZ) / (2 * (D_X ** 3))
VYY = (E * IYY) /(2 * (D_X **3 ))
BP = 40
LE = 500
HZ = 100
AXIAL = (E * BP * HZ) / LE
POISSON = 0.25
JM = ((HZ / 2) * ((BP / 2) ** 3)) * ((16/3) - (3.36 * ((BP / 2) / (HZ / 2)) * (1 - ((BP / 2) ** 4) / (12 * (HZ / 2) ** 4))))
G = E / (2 * ( 1 + POISSON))
T = (G * JM) / LE

NU = 30
LAMDA = 80

KZZ = np.zeros(shape=(ENE, ENE))
F_1ZZ = np.zeros(shape=(ENE, 1))
T_F_1ZZ = np.zeros(shape=(ENE, 1))
F_2ZZ = np.zeros(shape=(ENE, 1))
T_F_2ZZ = np.zeros(shape=(ENE, 1))
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
            KZZ[I_M][I_M - 2] = 1
            KZZ[I_M][I_M - 1] = -4
            KZZ[I_M][I_M] = 6 + C
            KZZ[I_M][I_M + 1] = -4
            KZZ[I_M][I_M + 2] = 1
        elif I_M == 0:
            KZZ[0][0] = 3
            F_1ZZ[0][0] = 3
        elif I_M == SCC:
            KZZ[SCC][SCC] = 3
        elif I_M == 1:
            KZZ[1][1] = 7 + C
            KZZ[1][0] = -4
            KZZ[1][2] = -4
            KZZ[1][3] = 1
            T_F_1ZZ[1][0] = 2 * D_X
        elif I_M == SCC -1:
            KZZ[SCC - 1][SCC - 1] = 7 + C
            KZZ[SCC - 1][SCC] = -4
            KZZ[SCC - 1][SCC - 2] = -4
            KZZ[SCC - 1][SCC - 3] = 1
            T_F_2ZZ[SCC - 1][0] = 2 * D_X
        if I_M == SCC:
            KZZ[SCC][SCC] = 3
            F_2ZZ[SCC][0] = 3
        I_M += 1
    FZZ = inv(np.asmatrix(KZZ)) #matríz inversa de KZZ
    D_1ZZ = - np.dot(FZZ, F_1ZZ)
    T_E1ZZ = - np.dot(FZZ, T_F_1ZZ)
    D_2ZZ = - np.dot(FZZ, F_2ZZ)
    T_E2ZZ = - np.dot(FZZ, T_F_2ZZ)
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
    #print(KZZ)"debug"
    if CYCLE == 0:
        #print("Debug")
        KYY = cp.deepcopy(KZZ)
        FYY = cp.deepcopy(FZZ)
        D_1YY = cp.deepcopy(D_1ZZ)
        D_1YY_MINUS_2 = cp.deepcopy(D_1ZZ_MINUS_2)
        D_1YY_MINUS_1 = cp.deepcopy(D_1ZZ_MINUS_1)
        D_1YY_PLUS_1 = cp.deepcopy(D_1ZZ_PLUS_1)
        D_1YY_PLUS_2 = cp.deepcopy(D_1ZZ_PLUS_2)
        D_2YY = cp.deepcopy(D_2ZZ)
        D_2YY_MINUS_2 = cp.deepcopy(D_2ZZ_MINUS_2)
        D_2YY_MINUS_1 = cp.deepcopy(D_2ZZ_MINUS_1)
        D_2YY_PLUS_1 = cp.deepcopy(D_2ZZ_PLUS_1)
        D_2YY_PLUS_2 = cp.deepcopy(D_2ZZ_PLUS_2)
        T_E2YY = cp.deepcopy(T_E2ZZ)
        T_E2YY_MINUS_2 = cp.deepcopy(T_E2ZZ_MINUS_2)
        T_E2YY_MINUS_1 = cp.deepcopy(T_E2ZZ_MINUS_1)
        T_E2YY_PLUS_2 = cp.deepcopy(T_E2ZZ_PLUS_2)
        T_E2YY_PLUS_1 = cp.deepcopy(T_E2ZZ_PLUS_1)
        T_E1YY = cp.deepcopy(T_E1ZZ)
        T_E1YY_MINUS_2 = cp.deepcopy(T_E1ZZ_MINUS_2)
        T_E1YY_MINUS_1 = cp.deepcopy(T_E1ZZ_MINUS_1)
        T_E1YY_PLUS_2 = cp.deepcopy(T_E1ZZ_PLUS_2)
        T_E1YY_PLUS_1 = cp.deepcopy(T_E1ZZ_PLUS_1)
    I_M = 0
    CYCLE += 1
#print("\n")
#print(df(KZZ))
#print("\n")
#print(df(KYY))

I_VM = 0
M_1ZZ = np.zeros(shape=(ENE, 1))
T_M_1ZZ = cp.deepcopy(M_1ZZ)
M_2ZZ = cp.deepcopy(M_1ZZ)
T_M_2ZZ = cp.deepcopy(M_1ZZ)
M_1YY = cp.deepcopy(M_1ZZ)
T_M_1YY = cp.deepcopy(M_1ZZ)
M_2YY = cp.deepcopy(M_1ZZ)
T_M_2YY = cp.deepcopy(M_1ZZ)

V_1ZZ = cp.deepcopy(M_1ZZ)
V_2ZZ = cp.deepcopy(M_1ZZ)
T_V_1ZZ = cp.deepcopy(M_1ZZ)
T_V_2ZZ = cp.deepcopy(M_1ZZ)

V_1YY = cp.deepcopy(M_1ZZ)
V_2YY = cp.deepcopy(M_1ZZ)
T_V_1YY = cp.deepcopy(M_1ZZ)
T_V_2YY = cp.deepcopy(M_1ZZ)

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

KEB = np.zeros(shape=(12,12))
T_R = cp.deepcopy(KEB)
    #region one
KEB[0][0] = AXIAL
KEB[1][1] = - V_1ZZ[0]
KEB[1][5] = - T_V_1ZZ[0]
KEB[2][2] = - V_1YY[0]
KEB[2][4] = T_V_1YY[0]
KEB[3][3] = T
KEB[4][2] = - M_1YY[0]
KEB[4][4] = T_M_1YY[0]
KEB[5][1] = M_1ZZ[0]
KEB[5][5] = T_M_1ZZ[0]
    #region two
KEB[6][0] = - AXIAL
KEB[7][1] = V_1ZZ[SCC]
KEB[7][5] = T_V_1ZZ[SCC]
KEB[8][2] = V_1YY[SCC]
KEB[8][4] = - T_V_1YY[SCC]
KEB[9][3] = - T
KEB[10][2] = M_1YY[SCC]
KEB[10][4] = - T_M_1YY[SCC]
KEB[11][1] = - M_1ZZ[SCC]
KEB[11][5] = - T_M_1ZZ[SCC]
    #region three
KEB[0][6] = - AXIAL
KEB[1][7] = - V_2ZZ[0]
KEB[2][11] = T_V_2ZZ[0]
KEB[2][8] = - V_2YY[0]
KEB[2][10] = - T_V_2YY[0]
KEB[3][9] = - T
KEB[4][8] = - M_2YY[0]
KEB[4][10] = - T_M_2YY[0]
KEB[5][7] = M_2ZZ[0]
KEB[5][11] = - T_M_2ZZ[0]
    #region four
KEB[6][6] = AXIAL
KEB[7][7] = V_2ZZ[SCC]
KEB[7][11] = - T_V_2ZZ[SCC]
KEB[8][8] = V_2YY[SCC]
KEB[8][10] = T_V_2YY[SCC]
KEB[9][9] = T
KEB[10][8] = M_2YY[SCC]
KEB[10][10] = T_M_2YY[SCC]
KEB[11][7] = - M_2ZZ[SCC]
KEB[11][11] = T_M_2ZZ[SCC]
#rotational matrix
#region one
a = math.cos(math.radians(NU))
b = math.sin(math.radians(NU))
c = math.cos(math.radians(LAMDA))
d = math.sin(math.radians(LAMDA))
T_R[0][0] = a * c
T_R[1][0] = - a * d
T_R[2][0] = - b
T_R[0][1] = d
T_R[1][1] = c
T_R[0][2] = b * c
T_R[1][2] = - b * d
T_R[2][2] = a
T_R[3][3] = a * c
T_R[4][3] = - a * d
T_R[5][3] = - b
T_R[3][4] = d
T_R[4][4] = c
T_R[3][5] = b * c
T_R[4][5] = - b * d
T_R[5][5] = a
#region two
T_R[6][6] = a * c
T_R[7][6] = - a * d
T_R[8][6] = - b
T_R[6][7] = d
T_R[7][7] = c
T_R[6][8] = b * c
T_R[7][8] = - b * d
T_R[8][8] = a
T_R[9][9] = a * c
T_R[10][9] = - a * d
T_R[11][9] = - b
T_R[9][10] = d
T_R[10][10] = c
T_R[9][11] = b * c
T_R[10][11] = - b * d
T_R[11][11] = a

print("\n")

KEBG = np.matrix(KEB * T_R * np.transpose(T_R))
print(df(KEBG))
