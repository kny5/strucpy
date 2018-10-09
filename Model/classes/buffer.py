from Model.classes.element_types import Concrete, Or, Oc, Custom, Ir, Node
from Model.functions.local_matrix import local_matrix
from Model.functions.get_data import get_data
from Model.functions.set_nodes import set_nodes
from Model.functions.k_mtx import k_mtx
import numpy as np
from matplotlib import pyplot as plt


class Buffer:

    def __init__(self, id):
        super().__init__()
        self.id = id
        self.Elements = []
        self.Nodes = []
        self.freedom = 0
        self.vcn = []
        self.v_springs = []

    def plot(self, id):
        for element in self.Elements:
            if element.e_id == id:
                for value in element.__dict__.values():
                    if isinstance(value, np.ndarray) and value.size == 21:
                        try:
                            plt.subplot(value)
                            plt.show()
                        except TypeError:
                            plt.plot(value)
                            plt.show()

    def b_aproximation(self):
        pass

    def structure_matrix(self):
        setattr(self, 'kest', np.matlib.zeros(shape=(self.freedom, self.freedom)))
        setattr(self, 'pcur_', np.zeros(self.freedom))

        for element in self.Elements:
            for _c, _i in enumerate(element.ve):
                if _i != 0:
                    self.pcur_[_i - 1] += element.pc_[_c]
                for _k, _j in enumerate(element.ve):
                    if _j != 0:
                        self.kest[_i - 1, _j - 1] += element.kebg.item(_c, _k)

    def set_loads(self, load=0):
        self.vcn = []
        self.v_springs = []
        for node in self.Nodes:
            self.vcn += node.n_vcn
            self.v_springs += node.n_springs
        pcur_sum = self.pcur_ + load + self.vcn
        setattr(self, 'dn_est', np.dot(self.kest.I, pcur_sum))

    def run(self):
        # ciclo primario
        for element in self.Elements:
            # vector de ensamble y datos primarios geométricos.
            set_nodes(self, element)

    # ciclo while donde k_mtx recibe datos para restar f_a en las posiciones indicadas, mientras estado = Falso repetir.

            # matriz k
            k_mtx(element)

            # for element in self.Elements:
            # operaciones locales
            local_matrix(element)

        # operaciones generales, creación matriz general de la estructura y multiplicación de matriz, vector general.
        self.structure_matrix()

        # estableciendo las cargas.
        self.set_loads()

        # ciclo secundario
        for element in self.Elements:
            # obteniendo resultados de general hacia individual.
            get_data(self, element)

    def add_to_node(self, id, node, *kwargs):
        for element in self.Elements:
            if element.e_id == id:
                for arg in kwargs:
                    if node == 'start':
                        element.start_conf.__setitem__(arg[0], arg[1])
                    elif node == 'end':
                        element.end_conf.__setitem__(arg[0], arg[1])

    def add_element(self, element_type, id=None):
        x = element_type
        x.e_id = id
        self.Elements.append(x)
        return True

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

    def select_element_by_id(self, id):
        pass


x = Buffer(1)
x.add_element(Concrete(h=120, b=150, b_prima=40, kv=2, start=(0, 0, 300), end=(900, 0, 300)), id=1)
x.add_element(Concrete(h=120, b=150, b_prima=40, kv=2, start=(0, 0, 0), end=(900, 0, 0)), id=2)
x.add_element(Concrete(h=120, b=150, b_prima=40, kv=2, start=(0, 0, 0), end=(0, 0, 300)), id=3)
x.add_element(Concrete(h=120, b=150, b_prima=40, kv=2, start=(900, 0, 0), end=(900, 0, 300)), id=4)
x.add_element(Concrete(h=40, b=40, b_prima=40, start=(0, 0, 300), end=(0, 500, 300)), id=5)
x.add_element(Concrete(h=40, b=40, b_prima=40, start=(900, 0, 300), end=(900, 500, 300)), id=6)
x.add_element(Concrete(h=40, b=40, b_prima=40, start=(0, 0, 0), end=(0, 500, 0)), id=7)
x.add_element(Concrete(h=40, b=40, b_prima=40, start=(900, 0, 0), end=(900, 500, 0)), id=8)
x.add_element(Concrete(h=40, b=40, b_prima=40, start=(0, 500, 300), end=(900, 500, 300)), id=9)
x.add_element(Concrete(h=40, b=40, b_prima=40, start=(0, 500, 0), end=(900, 500, 0)), id=10)
x.add_element(Concrete(h=40, b=40, b_prima=40, start=(0, 500, 0), end=(0, 500, 300)), id=11)
x.add_element(Concrete(h=40, b=40, b_prima=40, start=(900, 500, 0), end=(900, 500, 300)), id=12)
x.add_to_node(5, 'end', ('dy', (10, 0)))
x.run()

y = Buffer(2)
y.add_element(Concrete(h=120, b=150, b_prima=40, kv=2, start=(0, 0, 300), end=(900, 0, 300), marco=1), id=1)
y.add_element(Concrete(h=120, b=150, b_prima=40, kv=2, start=(0, 0, 0), end=(900, 0, 0), marco=1), id=2)
y.add_element(Concrete(h=120, b=150, b_prima=40, kv=2, start=(0, 0, 0), end=(0, 0, 300)), id=3)
y.add_element(Concrete(h=120, b=150, b_prima=40, kv=2, start=(900, 0, 0), end=(900, 0, 300)), id=4)
y.add_element(Concrete(h=40, b=40, b_prima=40, start=(0, 0, 300), end=(0, 500, 300)), id=5)
y.add_element(Concrete(h=40, b=40, b_prima=40, start=(900, 0, 300), end=(900, 500, 300)), id=6)
y.add_element(Concrete(h=40, b=40, b_prima=40, start=(0, 0, 0), end=(0, 500, 0)), id=7)
y.add_element(Concrete(h=40, b=40, b_prima=40, start=(900, 0, 0), end=(900, 500, 0)), id=8)
y.add_element(Concrete(h=40, b=40, b_prima=40, start=(0, 500, 300), end=(900, 500, 300)), id=9)
y.add_element(Concrete(h=40, b=40, b_prima=40, start=(0, 500, 0), end=(900, 500, 0)), id=10)
y.add_element(Concrete(h=40, b=40, b_prima=40, start=(0, 500, 0), end=(0, 500, 300)), id=11)
y.add_element(Concrete(h=40, b=40, b_prima=40, start=(900, 500, 0), end=(900, 500, 300)), id=12)
y.run()

z = Buffer(3)

z.add_element(Or(), id=1)
z.add_element(Or(), id=2)
z.add_element(Or(), id=3)

