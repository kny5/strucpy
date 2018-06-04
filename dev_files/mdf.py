"""
Data collector program
Autor: Antonio Anaya
Email: anaya.4589@gmail.com
"""
import csv
#from cli import askin
def asking(var, toprint, vector, level, count):
    """
    Capture input to define a global variables
    assign their values and saved it on an array.
    """
    while True:
        try:
            globals()[var] = float(input(str(toprint) + " <--- "))
        except ValueError:
            print("Ingrese un valor numérico válido.")
            continue
        else:
            break
    if vector != "null":
        vector[level][count] = globals()[var]
    else:
        print("Sin vector asignado")
    print("Guardado")
    return
ELEM = 0
i = 0
POISSON = 0.25
asking("ELEM", "Elementos", "null", 0, 0)
asking("mat", "Materiales", "null", 0, 0)
ELEMENTOS = [[0 for x in range(12)] for y in range(int(ELEM))]
while i <= ELEM - 1:
    print("\nDatos de elemento " + str(i + 1) + ": ")
    VARS_I = 0
    VARS_GEN = [[0 for x in range(12)] for y in range(5)]
    VARS_GEN[0] = ["l_elem", "b_prim", "b_z", "h_z", "izz",
                   "iyy", "pp_sec", "nu_ang", "la_ang", "k_v", "k_h"]
    VARS_GEN[1] = ["Longitud", "W Contratrabe", "W Zapata", "H Contratrabe",
                   "Inercia Z", "Inercia Y", "PP Sección",
                   "Angulo XZ", "Angulo XY", "Reacción V", "Reacción H"]
    while VARS_I <= len(VARS_GEN[0]) - 1:
        asking(str(VARS_GEN[0][VARS_I]), str(VARS_GEN[1][VARS_I]), VARS_GEN, 2, VARS_I)
        VARS_I += 1
    I_V = 0
    print("\nVector de ensamble:\n")
    while I_V <= 11:
        VARS_GEN[3] = ["dx1", "dy1", "dz1", "mx1", "my1", "mz1",
                       "dx2", "dy2", "dz2", "mx2", "my2", "mz2"]
        asking(str(VARS_GEN[3][I_V]), str(VARS_GEN[3][I_V]), VARS_GEN, 4, I_V)
        I_V += 1
    ELEMENTOS[i] = VARS_GEN
    i += 1
#print(ELEMENTOS)

#operaciones con variables
SECCIONES = 20 #define la precisión y aumenta tamaño de matríz
E = 221.359 #MODULO DE ELASTICIDAD DE MATERIAL
DELTA_X = l_elem / SECCIONES
KZZ = (k_v * b_z) / 1000
KNZZ = KZZ * DELTA_X
A = (KNZZ * DELTA_X ** 3) / (E * izz)
KYY = (k_h * h_z) / 1000
KNYY = KYY * DELTA_X
B = (KNYY * DELTA_X ** 3) / (E * iyy)
#a = h_z / 2
#b = b_prim / 2
j_m = ((h_z / 2) * ((b_prim / 2) ** 3)) * ((16/3) - (3.36 * ((b_prim / 2) / (h_z / 2)) * (1 - ((b_prim / 2) ** 4) / (12 * (h_z / 2) ** 4))))
g = E / (2 * ( 1 + POISSON))
tor = (g * j_m) / l_elem
axial = (E * b_prim * h_z) / l_elem
k_zero = k_v * 10 #10 es una constante para cambiar de KG A Toneladas cm3
k_uno = k_h * 10 #mismo
MZZ = (E * izz) / (DELTA_X ** 2)
vzz = (E * izz) / (2 * (DELTA_X ** 3))
MYY = (E * iyy) / (DELTA_X ** 2)
vyy = (E * iyy) /(2 * (DELTA_X **3 ))

KZZ = [[0 for x in range(SECCIONES + 1)]for y in range(SECCIONES + 1)]

i_kzz = 0
while i_kzz <= SECCIONES:
    if i_kzz == 0 && i_kzz == SECCIONES:
        KZZ[0][0] = 3

    i_kzz += 1

with open("output.csv", "w") as f:
    CSVOUT = csv.writer(f)
    CSVOUT.writerows(ELEMENTOS)
