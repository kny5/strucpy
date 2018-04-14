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
