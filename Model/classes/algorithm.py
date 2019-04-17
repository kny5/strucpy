# from Model.functions.local_matrix import local_matrix
# from Model.functions.get_data import get_data
from Model.functions.set_nodes import set_nodes
from Model.functions.asm_vector import asm_v
import numpy as np
from Model.classes.element_types import Element
from Model.classes.geometry import Node
from functools import reduce
from operator import add


class Program:
    def __init__(self, parent):
        # self.Elements = parent.elements
        self.parent = parent
        self.vectors = []
        self.nodes = []
        self.elements = []
        self.vcn = []
        self.v_springs = []
        self.freedom = 0
        self.kest = []
        self.pcur_ = []
        self.dn_est = []
        self.nodes_dict = {}

    def b_aproximation(self):
        pass

    def assemble_elements(self):
        self.elements = list(map(Element, self.vectors))
        print(self.elements)

    def full_structure_matrix(self):
        self.kest = np.matlib.zeros(shape=(self.freedom, self.freedom))
        self.pcur_ = np.zeros(self.freedom)

        for element in self.elements:
            for _c, _i in enumerate(element.ve):
                if _i != 0:
                    self.pcur_[_i - 1] += element.results.pc_[_c]
                for _k, _j in enumerate(element.ve):
                    if _j != 0:
                        self.kest[_i - 1, _j - 1] += element.kebg.item(_c, _k)

    # revision
    def set_nodes_loads(self, load=[]):
        for node in self.nodes:
            self.vcn += node.n_vcn
            self.v_springs += node.n_springs
        pcur_sum = self.pcur_ + load + self.vcn
        self.dn_est = np.dot(self.kest.I, pcur_sum)

    # check if this goes to control class
    def set_elements(self):
        self.elements = list(map(Element, self.vectors))

    # moe this to control class
    def set_nodes(self):
        list_points = reduce(add, [[vector.start, vector.end] for vector in self.vectors])
        self.nodes = list(map(Node, list_points))
        self.nodes_dict = dict(zip(list_points, self.nodes))

    # move this to control class
    def run(self):
        print("Starting...")
        # ciclo primario
        objects = set_nodes(self.vectors)
        print("Zero")
        print(objects)
        self.elements = objects[0]
        self.freedom = asm_v(objects[1])
        print("one " + str(self.freedom))
        # for element in self.elements:
            # vector de ensamble y datos primarios geométricos.
            # set_nodes(self, element)

            # ciclo while donde k_mtx recibe datos para restar f_a en las posiciones indicadas,
            # mientras estado = Falso repetir.

            # matriz k
            # k_mtx(element)

            # for element in self.Elements:
            # operaciones locales
            # local_matrix(element)
        print("two")

        # operaciones generales, creación matriz general de la estructura y multiplicación de matriz, vector general.
        # self.full_structure_matrix()
        print("3")
        # estableciendo las cargas.
        # self.set_nodes_loads()

        # ciclo secundario
        # for element in self.Elements:
        #     # obteniendo resultados de general hacia individual.
        #     get_data(self, element)
        print("End...")
        print(self.elements[0].results.__dict__)

