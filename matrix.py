# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import copy as cp
import numpy as np
from numpy.linalg import inv
from pandas import DataFrame as df
A = 3
B = 5
SCC = 20
D_X = 30
ENE = SCC + 1
IZZ = 213333.33
E = 221.359
MZZ = (E * IZZ) / D_X ** 2

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
print("\n")
print(df(KZZ))
print("\n")
print(df(KYY))

I_VM = 0
M_1ZZ = np.zeros(shape=(ENE, 1))
T_M_1ZZ = cp.deepcopy(M_1ZZ)
M_2ZZ = cp.deepcopy(M_1ZZ)
T_M_2ZZ = cp.deepcopy(M_1ZZ)
#print(M_1ZZ)
#print(T_M_1ZZ)
while I_VM <= SCC:
    if I_VM == 0:
        M_1ZZ[I_VM] = (D_1ZZ[1] - (2 * D_1ZZ[0]) +  D_1ZZ_MINUS_1) * MZZ
        T_M_1ZZ[I_VM] = (T_E1ZZ[1] - (2 * T_E1ZZ[0]) +  T_E1ZZ_MINUS_1) * MZZ
        M_2ZZ[I_VM] = (D_2ZZ[1] - (2 * D_2ZZ[0]) +  D_2ZZ_MINUS_1) * MZZ
        T_M_2ZZ[I_VM] = (T_E2ZZ[1] - (2 * T_E2ZZ[0]) +  T_E2ZZ_MINUS_1) * MZZ
    elif I_VM != 0 and I_VM != SCC:
        M_1ZZ[I_VM] = (D_1ZZ[I_VM + 1] - (2 * D_1ZZ[I_VM]) +  D_1ZZ[I_VM - 1]) * MZZ
        T_M_1ZZ[I_VM] = (T_E1ZZ[I_VM + 1] - (2 * T_E1ZZ[I_VM]) +  T_E1ZZ[I_VM - 1]) * MZZ
        M_2ZZ[I_VM] = (D_2ZZ[I_VM + 1] - (2 * D_2ZZ[I_VM]) +  D_2ZZ[I_VM - 1]) * MZZ
        T_M_2ZZ[I_VM] = (T_E2ZZ[I_VM + 1] - (2 * T_E2ZZ[I_VM]) +  T_E2ZZ[I_VM - 1]) * MZZ
    elif I_VM == SCC:
        M_1ZZ[I_VM] = (D_1ZZ_PLUS_1 - (2 * D_1ZZ[I_VM]) +  D_1ZZ[I_VM - 1]) * MZZ
        T_M_1ZZ[I_VM] = (T_E1ZZ_PLUS_1 - (2 * T_E1ZZ[I_VM]) +  T_E1ZZ[I_VM - 1]) * MZZ
        M_2ZZ[I_VM] = (D_2ZZ_PLUS_1 - (2 * D_2ZZ[I_VM]) +  D_2ZZ[I_VM - 1]) * MZZ
        T_M_2ZZ[I_VM] = (T_E2ZZ_PLUS_1 - (2 * T_E2ZZ[I_VM]) +  T_E2ZZ[I_VM - 1]) * MZZ
    I_VM += 1
print(M_1ZZ)
print("\n")
print(T_M_1ZZ)
print("\n")
print(M_2ZZ)
print("\n")
print(T_M_2ZZ)
