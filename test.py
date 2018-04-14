def asking(var, toprint, vector, y, count):
    """
    Capture input to define a global variable
    and his value.
    """
    while True:
        try:
            globals()[var] = int(input(str(toprint) + " <--- "))
        except ValueError:
            print("Ingrese un valor numérico válido.")
            continue
        else:
            break
    vector[y][count] = globals()[var]
    print("Ingresado")
    return
i = 0
vector = [[0 for x in range(3)] for y in range(2)]

print("\n\n")
print(vector)
print("\n\n")
asking("chi", "sho", vector, 1, i)

print("\n\n")
print(vector)
