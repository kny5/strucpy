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
KZZ = [[0 for x in range(SECCIONES + 1)]for y in range(SECCIONES + 1)]
FU1ZZ = [[0 for x in range(1)]for y in range(SECCIONES + 1)]
ANG_FU1ZZ = [[0 for x in range(1)]for y in range(SECCIONES + 1)]
FU2ZZ = [[0 for x in range(1)]for y in range(SECCIONES + 1)]
ANG_FU2ZZ = [[0 for x in range(1)]for y in range(SECCIONES + 1)]
KYY = KZZ
FU1YY = FU1ZZ
ANG_FU1YY = ANG_FU1ZZ
FU2YY = FU2ZZ
ANG_FU2YY = ANG_FU2ZZ
I_KZZ = 0
while I_KZZ <= SECCIONES:
    if I_KZZ != SECCIONES and I_KZZ != 0 and I_KZZ != 1 and I_KZZ != SECCIONES - 1:
        KZZ[I_KZZ][I_KZZ - 2] = 1
        KZZ[I_KZZ][I_KZZ - 1] = -4
        KZZ[I_KZZ][I_KZZ] = 6 + A
        KZZ[I_KZZ][I_KZZ + 1] = -4
        KZZ[I_KZZ][I_KZZ + 2] = 1
    if I_KZZ == 0:
        KZZ[0][0] = 3
        FU1ZZ[0][0] = 3
    if I_KZZ == SECCIONES:
        KZZ[SECCIONES][SECCIONES] = 3
    if I_KZZ == 1:
        KZZ[1][1] = 7 + A
        KZZ[1][0] = -4
        KZZ[1][2] = -4
        KZZ[1][3] = 1
        ANG_FU1ZZ[1][0] = 2 * DELTA_X
    if I_KZZ == SECCIONES -1:
        KZZ[SECCIONES - 1][SECCIONES - 1] = 7 + A
        KZZ[SECCIONES - 1][SECCIONES] = -4
        KZZ[SECCIONES - 1][SECCIONES - 2] = -4
        KZZ[SECCIONES - 1][SECCIONES - 3] = 1
        ANG_FU2ZZ[SECCIONES - 1][0] = 2 * DELTA_X
    if I_KZZ == SECCIONES:
        KZZ[SECCIONES][SECCIONES] = 3
        FU2ZZ[SECCIONES][0] = 3
    I_KZZ += 1
    FZZ_m = np.asmatrix(KZZ)
FZZ = inv(FZZ_m) #matríz inversa de KZZ
DE1ZZ = np.dot(FZZ, np.asmatrix(FU1ZZ)) * (-1)
ANG_E1ZZ = np.dot(FZZ, np.asmatrix(ANG_FU1ZZ)) * (-1)
DE2ZZ = np.dot(FZZ, np.asmatrix(FU2ZZ)) * (-1)
ANG_E2ZZ = np.dot(FZZ, np.asmatrix(ANG_FU2ZZ)) * (-1)
DE1ZZ_2 = (float(DE1ZZ[2]) * (-1)) + (8 * float(DE1ZZ[1])) - (6 * float(DE1ZZ[0]))
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

#print(DE1ZZ)
