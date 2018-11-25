from Model.functions.local_matrix import local_matrix
from Model.functions.get_data import get_data
from Model.functions.set_nodes import set_nodes
from Model.functions.k_mtx import k_mtx
import numpy as np


class Buffer:

    def __init__(self, id):
        super().__init__()
        self.id = id
        self.Elements = []
        self.Nodes = []
        self.vcn = []
        self.v_springs = []
        self.freedom = 0

    def b_aproximation(self):
        pass

    def __structure_matrix(self):
        setattr(self, 'kest', np.matlib.zeros(shape=(self.freedom, self.freedom)))
        setattr(self, 'pcur_', np.zeros(self.freedom))

        for element in self.Elements:
            for _c, _i in enumerate(element.ve):
                if _i != 0:
                    self.pcur_[_i - 1] += element.pc_[_c]
                for _k, _j in enumerate(element.ve):
                    if _j != 0:
                        self.kest[_i - 1, _j - 1] += element.kebg.item(_c, _k)

    def __set_loads(self, load=0):
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

            # ciclo while donde k_mtx recibe datos para restar f_a en las posiciones indicadas,
            # mientras estado = Falso repetir.

            # matriz k
            k_mtx(element)

            # for element in self.Elements:
            # operaciones locales
            local_matrix(element)

        # operaciones generales, creación matriz general de la estructura y multiplicación de matriz, vector general.
        self.__structure_matrix()

        # estableciendo las cargas.
        self.__set_loads()

        # ciclo secundario
        for element in self.Elements:
            # obteniendo resultados de general hacia individual.
            get_data(self, element)

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
