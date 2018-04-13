#entrada de datos
#Entrada de elementos
elem = int(input("Número de elementos: ")) #número de elementos a usar.
mat = int(input("Número de materiales: ")) #número de materiales a usar.
i = 0
datos = [[0 for x in range(12)] for y in range(elem)] #definiendo matriz para guardar datos de elementos
while (i <= elem - 1):
    print("Datos de elemento " + str(i + 1) + ": ")
    l_elem = int(input("   Longitud: "))
    b_prim = int(input("   Ancho de contratrabe: "))
    b_z = int(input("   Ancho de zapata: "))
    h_z = int(input("   Altura de contratrabe: "))
    poisson = 0.25
    izz = int(input("   Inercia en eje Z: "))
    iyy = int(input("   Inercia en eje Y: "))
    pp_sec = int(input("   Peso propio de la sección: "))
    nu_ang = int(input("   Angulo respecto al plano xz: "))
    la_ang = int(input("   Angulo resecto al plano xy: "))
    k_v = int(input("   Modulo de reacción vertical: "))
    k_h = int(input("   Modulo de reacción horizontal: "))
    datos[i] = [l_elem, b_prim, b_z, h_z, poisson, izz, iyy, pp_sec, nu_ang, la_ang, k_v, k_h]
    #print(datos)
    #i += 1 #debug point
    i_v = 0
    v_ens = [0 for i_v in range(12)]
    while(i_v <= 11):
        v_ens_name = ["dx1", "dy1", "dz1", "mx1", "my1", "mz1", "dx2", "dy2", "dz2", "mx2", "my2", "mz2"]
        v_ens[i_v] = int(input( "   " + str(v_ens_name[i_v]) + ": " ))
        i_v += 1
    #print(v_ens)
    i += 1
print(datos)
print(v_ens)
