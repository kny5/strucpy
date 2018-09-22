import math
#from Model.classes.node import Node


def set_nodes(elemento):
    elemento._nodoStart = None
    elemento._nodoEnd = None
    elemento.lm = None
    elemento.l = None
    elemento.nu = None
    elemento.ve = None

    if elemento.start != elemento.end:

        if len(self.Elements) == 0 and len(self.Nodes) == 0:
            elemento._nodoStart = self.nodes(elemento.start, **elemento.start_conf)
            elemento._nodoEnd = self.nodes(elemento.end, **elemento.end_conf)
        else:
            for nodo in self.Nodes:
                if nodo.position == elemento.start:
                    elemento._nodoStart = nodo
                elif nodo.position == elemento.end:
                    elemento._nodoEnd = nodo

        if elemento._nodoStart is None:
            elemento._nodoStart = self.nodes(elemento.start, **elemento.start_conf)
        if elemento._nodoEnd is None:
            elemento._nodoEnd = self.nodes(elemento.end, **elemento.end_conf)

        elemento.ve = elemento._nodoStart.ve_parcial + elemento._nodoEnd.ve_parcial

        elemento.l = abs((((elemento.end[0] - elemento.start[0]) ** 2) +
                          ((elemento.end[1] - elemento.start[1]) ** 2) +
                          ((elemento.end[2] - elemento.start[2]) ** 2)) ** 0.5)
        plane_xz = (((elemento._nodoEnd.x - elemento._nodoStart.x) ** 2) +
                    ((elemento._nodoEnd.z - elemento._nodoStart.z) ** 2)) ** 0.5

        if plane_xz != 0:
            _nu_ = math.degrees(math.asin((elemento._nodoEnd.z - elemento._nodoStart.z) / plane_xz))
            if elemento._nodoEnd.x - elemento._nodoStart.x < 0:
                elemento.nu = 180 - _nu_
            else:
                elemento.nu = _nu_
        else:
            elemento.nu = 0
        elemento.lm = math.degrees(math.asin((elemento._nodoEnd.y - elemento._nodoStart.y) / elemento.l))
        elemento.apoyos = elemento._nodoStart.n_apoyo + elemento._nodoEnd.n_apoyo
    else:
        print("Error No Start or End points")
        print('values are the same')
        print(elemento.start, elemento.end)
        return False

    print(("¬" * int(elemento.id)) + " " + elemento.id)
    print(elemento.ve)

    return True
