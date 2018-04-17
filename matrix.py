# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import numpy as np
from numpy.linalg import inv
A = 3
B = 5
SECCIONES = 20
DELTA_X = 25
ENE = SECCIONES + 1
MTRX = np.zeros(shape = (ENE, ENE))
FU1ZZ = np.zeros(shape = (ENE, 1))
ANG_FU1ZZ = np.zeros(shape = (ENE, 1))
FU2ZZ = np.zeros(shape = (ENE, 1))
ANG_FU2ZZ = np.zeros(shape = (ENE, 1))
#KYY = MTRX
#FU1YY = FU1ZZ
#ANG_FU1YY = ANG_FU1ZZ
#FU2YY = FU2ZZ
#ANG_FU2YY = ANG_FU2ZZ
I_M = 0
CYCLE = 0
C = A
while CYCLE <= 1:
    if CYCLE == 0:
        C = float(A)
    else:
        C = float(B)
    while I_M <= SECCIONES:
        if I_M != SECCIONES and I_M != 0 and I_M != 1 and I_M != SECCIONES - 1:
            MTRX[I_M][I_M - 2] = 1
            MTRX[I_M][I_M - 1] = -4
            MTRX[I_M][I_M] = 6 + C
            MTRX[I_M][I_M + 1] = -4
            MTRX[I_M][I_M + 2] = 1
        if I_M == 0:
            MTRX[0][0] = 3
            FU1ZZ[0][0] = 3
        if I_M == SECCIONES:
            MTRX[SECCIONES][SECCIONES] = 3
        if I_M == 1:
            MTRX[1][1] = 7 + C
            MTRX[1][0] = -4
            MTRX[1][2] = -4
            MTRX[1][3] = 1
            ANG_FU1ZZ[1][0] = 2 * DELTA_X
        if I_M == SECCIONES -1:
            MTRX[SECCIONES - 1][SECCIONES - 1] = 7 + C
            MTRX[SECCIONES - 1][SECCIONES] = -4
            MTRX[SECCIONES - 1][SECCIONES - 2] = -4
            MTRX[SECCIONES - 1][SECCIONES - 3] = 1
            ANG_FU2ZZ[SECCIONES - 1][0] = 2 * DELTA_X
        if I_M == SECCIONES:
            MTRX[SECCIONES][SECCIONES] = 3
            FU2ZZ[SECCIONES][0] = 3
        I_M += 1
    #M_FZZ = np.asmatrix(MTRX)
    FZZ = inv(MTRX) #matríz inversa de MTRX
    DE1ZZ = np.dot(FZZ, FU1ZZ) * (-1)
    ANG_E1ZZ = np.dot(FZZ, ANG_FU1ZZ) * (-1)
    DE2ZZ = np.dot(FZZ, FU2ZZ) * (-1)
    ANG_E2ZZ = np.dot(FZZ, ANG_FU2ZZ) * (-1)
    DE1ZZ_2 = - float(DE1ZZ[2]) + (8 * float(DE1ZZ[1])) - (6 * float(DE1ZZ[0]))
    DE1ZZ_1 = float(DE1ZZ[1])
    DE1ZZ_21 = float(DE1ZZ[19])
    DE1ZZ_22 = (8 * float(DE1ZZ[19])) - float(DE1ZZ[18])
    ANG_E1ZZ_2 = float(-ANG_E1ZZ[2]) + (8 * (float(ANG_E1ZZ[1])) + (8 * DELTA_X))
    ANG_E1ZZ_1 = ((2 * DELTA_X) + float(ANG_E1ZZ[1]))
    ANG_E1ZZ_21 = float(ANG_E1ZZ[19])
    ANG_E1ZZ_22 = (8 * (float(ANG_E1ZZ[19]))) - float(ANG_E1ZZ[18])
    DE2ZZ_2 = (8 * float(DE2ZZ[1])) - float(DE2ZZ[2])
    DE2ZZ_1 = float(DE2ZZ[1])
    DE2ZZ_21 = float(DE2ZZ[19])
    DE2ZZ_22 = - float(DE2ZZ[18]) + (8 * float(DE2ZZ[19])) - (6 * float(DE2ZZ[20]))
    ANG_E2ZZ_2 = (8 * float(ANG_E2ZZ[1])) - float(ANG_E2ZZ[2])
    ANG_E2ZZ_1 = float(ANG_E2ZZ[1])
    ANG_E2ZZ_21 = ((2 * DELTA_X) + float(ANG_E2ZZ[19]))
    ANG_E2ZZ_22 = - float(ANG_E2ZZ[18]) + (8 * float(ANG_E2ZZ[19])) + (8 * DELTA_X)

    CYCLE += 1
#print(DE1ZZ)
