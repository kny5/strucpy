"""
Program to capture variables and values.
"""
def asking(var, nombre):
    """
    Capture input to define a global variable
    and his value.
    """
    while True:
        try:
            globals()[var] = int(input(str(nombre) + " <--- "))
        except ValueError:
            print("Ingrese un valor numérico válido.")
            continue
        else:
            break
    print("Ingresado")
    return
ELEM = 0
i = 0
POISSON = 0.25
asking("ELEM", "Elementos")
asking("mat", "Materiales")
while i <= ELEM - 1:
    print("\nDatos de elemento " + str(i + 1) + ": ")
    VARS_I = 0
    VARS_GEN = [[0 for x in range(12)] for y in range(3)]
    VARS_GEN[0] = ["l_elem", "b_prim", "b_z", "h_z", "POISSON", "izz",
                   "iyy", "pp_sec", "nu_ang", "la_ang", "k_v", "k_h"]
    VARS_GEN[1] = ["Longitud", "W Contratrabe", "W Zapata", "H Contratrabe",
                   "Poisson", "Inercia Z", "Inercia Y", "PP Sección",
                   "Angulo XZ", "Angulo XY", "Reacción V", "Reacción H"]
    while VARS_I <= len(VARS_GEN[0]) - 1:
        asking(str(VARS_GEN[0][VARS_I]), str(VARS_GEN[1][VARS_I]))
        VARS_I += 1
    VARS_GEN[2] = [l_elem, b_prim, b_z, h_z, POISSON, izz,
                   iyy, pp_sec, nu_ang, la_ang, k_v, k_h]
    print(VARS_GEN)
    I_V = 0
    #V_ENS = [0 for I_V in range(12)]
    V_ENS = [[0 for x in range(12)] for y in range(3)]
    print("\nVector de ensamble:\n")
    while I_V <= 11:
        V_ENS[0] = ["dx1", "dy1", "dz1", "mx1", "my1", "mz1",
                    "dx2", "dy2", "dz2", "mx2", "my2", "mz2"]
        V_ENS[1] = int(input("   " + str(V_ENS_NAME[0][I_V]) + ": "))
        I_V += 1
    V_ENS[0] = [dx1, dy1, dz1, mx1, my1, mz1,
                dx2, dy2, dz2, mx2, my2, mz2]
    i += 1
