"""
Librería de funciones para interactuar con línea de comandos
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
