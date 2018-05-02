FREE_DG = 750
STRUC_MTRX = np.matrix.zeros(shape=(FREE_DG, FREE_DG))
PCU = np.matrix.zeros(shape=(0, 12))

PU_AX = P_SCC_AX + PW_AX

PCU[0] = PU_AX
PCU[1] = - V_DL_ZZ[0]
PCU[2] = - V_DL_YY[0]
PCU[3] = 0 #TORSIÓN EXTREMO 1
PCU[4] = - M_DL_YY[0]
PCU[5] = M_DL_ZZ[0]
PCU[6] = PU_AX
PCU[7] = V_DL_ZZ[SCC]
PCU[8] = V_DL_YY[SCC]
PCU[9] = 0 #TORSIÓN EXTREMO 2
PCU[10] = M_DL_YY[SCC]
PCU[11] = - M_DL_ZZ[SCC]

PCU_R = T_R * PCU

P_NOD = np.matrix.zeros(shape=(0, FREE_DG))
