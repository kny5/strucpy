def asking(var, nombre):
    while True:
        try:
            var = int(input(str(nombre) + " <--- "))
        except ValueError:
            print("Ingrese un valor numérico válido.")
            continue
        else:
            break    
    print("Ingresado " + str(nombre) + " = " + str(var))
    return

asking("b1", "hola")

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