from Model.classes.element_types import Concrete, Or, Oc, Custom, Ir
from Model.classes.node import Node
from Model.functions.set_nodes import set_nodes

class Buffer:

    nodes = Node
    Concreto = Concrete
    OR = Or
    OC = Oc
    Especial = Custom
    IR = Ir

    def __init__(self, id):
        super().__init__()
        self.id = id
        self.Elements = []
        self.Nodes = []
        self.freedom_degrees = []
        self.nodal_loads_vector = []
        self.nodal_loads_matrix = []
        self.marcos = []
        self.dn_est = None
        self.ac_nodo = []
        self.Max_val = []

    def set_nodes(self, elemento):
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

    def run(self, method):
        if method == 'normal':

            for element in self.Elements:
                element.set_nodes()
            y = False
            while not y:
                for element in self.Elements:
                    self.set_local_data(element)
                self.set_general_matrix()
                y = self.results(element)

        elif method == 'montecarlo':
            pass
        elif method == 'aproximar_b':
            pass

    def add_element(self, type, id, start, end):
        for element in self.Elements:
            if element.e_id == id:
                return False
            elif element.start == start and element.end == end:
                return False
        try:
            x = type
            x.e_id = id
            x.start = start
            x.end = end
            self.Elements.append(x)
            return True
        except TypeError:
            return False

    def delete_element_by_id(self, element_id):
        for element in self.Elements:
            if element.e_id == element_id:
                self.Elements.remove(element)
        return True

    def delete_element_by_point(self, point):
        for element in self.Elements:
            if element.start == point or element.end == point:
                self.Elements.remove(element)
        return True


x = Buffer(1)
x.add_element(Concrete(), 1, (0,0,0), (300,0,0))
x.add_element(Concrete(), 2, (0,0,0), (100,0,0))
x.add_element(Concrete(), 3, (100,0,0), (300,0,0))

for elemento in x.Elements:
    x.set_nodes(elemento)
