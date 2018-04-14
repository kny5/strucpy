def asking(var, nombre):
    while True:
        try:
            #globals()[var] = int(input(str(nombre) + " <--- "))
            var = int(input(str(nombre) + " <--- "))
        except ValueError:
            print("Ingrese un valor numérico válido.")
            continue
        else:
            break
    print("Ingresado " + str(nombre))
    file = open('output', 'a')
    file.write(str(var) + "\n")
    file.close
    return

asking("hola","concha")
asking("loli","lola")
asking("gato","mio")


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
