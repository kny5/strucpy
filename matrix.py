# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
from copy import copy as cp
import numpy as np
from numpy.linalg import inv
A = 3
B = 5
SCC = 20
D_X = 25
ENE = SCC + 1
M = np.zeros(shape=(ENE, ENE))
F_1ZZ = np.zeros(shape=(ENE, 1))
T_F_1ZZ = np.zeros(shape=(ENE, 1))
F_2ZZ = np.zeros(shape=(ENE, 1))
T_F_2ZZ = np.zeros(shape=(ENE, 1))
KZZ = np.copy(M)
KYY = np.copy(M)
#F_1YY = F_1ZZ
#T_F_1YY = T_F_1ZZ
#F_2YY = F_2ZZ
#T_F_2YY = T_F_2ZZ
I_M = 0
CYCLE = 0
C = 0
while CYCLE <= 1:
    if CYCLE == 0:
        C = cp(A)
    else:
        C = cp(B)
    while I_M <= SCC:
        if I_M != SCC and I_M != 0 and I_M != 1 and I_M != SCC - 1:
            M[I_M][I_M - 2] = 1
            M[I_M][I_M - 1] = -4
            M[I_M][I_M] = 6 + C
            M[I_M][I_M + 1] = -4
            M[I_M][I_M + 2] = 1
        elif I_M == 0:
            M[0][0] = 3
            F_1ZZ[0][0] = 3
        elif I_M == SCC:
            M[SCC][SCC] = 3
        elif I_M == 1:
            M[1][1] = 7 + C
            M[1][0] = -4
            M[1][2] = -4
            M[1][3] = 1
            T_F_1ZZ[1][0] = 2 * D_X
        elif I_M == SCC -1:
            M[SCC - 1][SCC - 1] = 7 + C
            M[SCC - 1][SCC] = -4
            M[SCC - 1][SCC - 2] = -4
            M[SCC - 1][SCC - 3] = 1
            T_F_2ZZ[SCC - 1][0] = 2 * D_X
        elif I_M == SCC:
            M[SCC][SCC] = 3
            F_2ZZ[SCC][0] = 3
        I_M += 1
    M_FZZ = np.asmatrix(M)
    FZZ = inv(M_FZZ) #matríz inversa de M
    D_1ZZ = - np.dot(FZZ, F_1ZZ)
    T_E1ZZ = - np.dot(FZZ, T_F_1ZZ)
    D_2ZZ = - np.dot(FZZ, F_2ZZ)
    T_E2ZZ = - np.dot(FZZ, T_F_2ZZ)
    D_1ZZ_MINUS_2 = - float(D_1ZZ[2]) + (8 * float(D_1ZZ[1])) - (6 * float(D_1ZZ[0]))
    D_1ZZ_MINUS_1 = float(D_1ZZ[1])
    D_1ZZ_PLUS_1 = float(D_1ZZ[SCC - 1])
    D_1ZZ_PLUS_2 = (8 * float(D_1ZZ[SCC - 1])) - float(D_1ZZ[SCC - 2])
    T_E1ZZ_MINUS_2 = - float(T_E1ZZ[2]) + (8 * (float(T_E1ZZ[1])) + (8 * D_X))
    T_E1ZZ_MINUS_1 = ((2 * D_X) + float(T_E1ZZ[1]))
    T_E1ZZ_PLUS_1 = float(T_E1ZZ[SCC - 1])
    T_E1ZZ_PLUS_2 = (8 * (float(T_E1ZZ[SCC - 1]))) - float(T_E1ZZ[SCC - 2])
    D_2ZZ_MINUS_2 = (8 * float(D_2ZZ[1])) - float(D_2ZZ[2])
    D_2ZZ_MINUS_1 = float(D_2ZZ[1])
    D_2ZZ_PLUS_1 = float(D_2ZZ[SCC - 1])
    D_2ZZ_PLUS_2 = - float(D_2ZZ[SCC - 2]) + (8 * float(D_2ZZ[SCC - 1])) - (6 * float(D_2ZZ[SCC]))
    T_E2ZZ_MINUS_2 = (8 * float(T_E2ZZ[1])) - float(T_E2ZZ[2])
    T_E2ZZ_MINUS_1 = float(T_E2ZZ[1])
    T_E2ZZ_PLUS_1 = ((2 * D_X) + float(T_E2ZZ[SCC - 1]))
    T_E2ZZ_PLUS_2 = - float(T_E2ZZ[SCC - 2]) + (8 * float(T_E2ZZ[SCC - 1])) + (8 * D_X)

    CYCLE += 1
print(FZZ)
