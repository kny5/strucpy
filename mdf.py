"""
Data collector program
Autor: Antonio Anaya
Email: anaya.4589@gmail.com
"""
def asking(var, toprint, vector, level, count):
    """
    Capture input to define a global variables
    assign their values and saved it on an array.
    """
    while True:
        try:
            globals()[var] = int(input(str(toprint) + " <--- "))
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
while i <= ELEM - 1:
    print("\nDatos de elemento " + str(i + 1) + ": ")
    VARS_I = 0
    VARS_GEN = [[0 for x in range(12)] for y in range(5)]
    VARS_GEN[0] = ["l_elem", "b_prim", "b_z", "h_z", "POISSON", "izz",
                   "iyy", "pp_sec", "nu_ang", "la_ang", "k_v", "k_h"]
    VARS_GEN[1] = ["Longitud", "W Contratrabe", "W Zapata", "H Contratrabe",
                   "Poisson", "Inercia Z", "Inercia Y", "PP Sección",
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
        #VARS_GEN[4] = int(input("   " + str(VARS_GEN[3][I_V]) + ": "))
        I_V += 1
    i += 1
print(VARS_GEN[2])
print(VARS_GEN[4])
