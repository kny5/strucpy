def asking(var, nombre):
    while True:
        try:
            globals()[var] = int(input(str(nombre) + " <--- "))
        except ValueError:
            print("Ingrese un valor numérico válido.")
            continue
        else:
            break
    print("Ingresado " + str(nombre))
    return

asking("elem","Elementos")
asking("mat","Materiales")

i = 0
poisson = 0.25

variables = [[0 for x in range(12)] for y in range(elem)] #definiendo matriz para guardar valores de variables

v_matrix = [[0 for x in range(12)] for y in range(elem)]

while (i <= elem - 1):
    print("\n \nDatos de elemento " + str(i + 1) + ": ")
    asking("l_elem","Longitud")
    asking("b_prim","Ancho de contratrabe")
    asking("b_z","Ancho de Zapata")
    asking("h_z","Altura de contratrabe")
    asking("izz","Inercia eje Z")
    asking("iyy","Inercia eje Y")
    asking("pp_sec","Peso propio de sección")
    asking("nu_ang","Angulo XZ")
    asking("la_ang","Angulo XY")
    asking("k_v","Modulo reacción Vertical")
    asking("k_h","Modulo reacción Horizontal")
    variables[i] = [l_elem, b_prim, b_z, h_z, poisson, izz, iyy, pp_sec, nu_ang, la_ang, k_v, k_h]
    #print(datos)
    #i += 1 #debug point 1

    i_v = 0
    v_ens = [0 for i_v in range(12)]
    while(i_v <= 11):
        v_ens_name = ["dx1", "dy1", "dz1", "mx1", "my1", "mz1", "dx2", "dy2", "dz2", "mx2", "my2", "mz2"]
        v_ens[i_v] = int(input( "   " + str(v_ens_name[i_v]) + ": " ))
        i_v += 1
    #print(v_ens) #debug point 2
    v_matrix[i] = v_ens
    i += 1
print(variables)
print("\n")
print(v_ens)
