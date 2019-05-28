from functions.local_matrix import local_matrix
from functions.get_data import get_data
# from Model.functions.set_nodes import set_nodes
# from Model.functions.asm_vector import asm_v
import numpy as np
from numpy import matlib
from classes.element_types import Element
from classes.geometry import Node
from functools import reduce
from operator import add


class Program:
    def __init__(self, parent):
        self.parent = parent
        self.vectors = set([])
        self.nodes = list(self.parent.dict_nodes.values())
        self.elements = []
        self.vcn = []
        self.v_springs = []
        self.freedom = 0
        self.kest = []
        self.pcur_ = []
        self.dn_est = []

    # def b_aproximation(self):
    #     pass

    # def set_elements(self):
    #     self.elements = list(map(Element, self.vectors))

    def asm_v(self):
        # print("asm_v")
        self.freedom = 0
        for node in self.nodes:
            n_ve = []
            for _bool in node.conf.values():
                if _bool:
                    self.freedom += 1
                    n_ve.append(self.freedom)
                else:
                    n_ve.append(0)
            node.n_ve = n_ve
        # print(freedom)
        # return freedom

    def full_structure_matrix(self):
        self.kest = matlib.zeros(shape=(self.freedom, self.freedom))
        self.pcur_ = np.zeros(self.freedom)

        for element in self.elements:
            for _c, _i in enumerate(element.ve):
                if _i != 0:
                    self.pcur_[_i - 1] += element.results.pc_[_c]
                for _k, _j in enumerate(element.ve):
                    if _j != 0:
                        self.kest[_i - 1, _j - 1] += element.kebg.item(_c, _k)

    # def set_nodes(self):
    #     list_points = reduce(add, [[vector.start, vector.end] for vector in self.vectors])
    #     self.nodes = list(map(Node, list_points))
    #     self.nodes_dict = dict(zip(list_points, self.nodes))

    def set_nodes_loads(self, random_loads=None):
        self.vcn = []
        self.v_springs = []
        for node in self.nodes:
            print(node)
            self.vcn.append(node.n_vcn)
            self.v_springs.append(node.n_springs)
            print(self.vcn)
            print(self.v_springs)
        pcur_sum = np.add(self.pcur_, self.vcn)
        if not random_loads == None:
            pcur_sum_random_loads = np.add(pcur_sum, np.asarray(random_loads))
            self.dn_est = np.dot(self.kest.I, pcur_sum_random_loads)
        else:
            self.dn_est = np.dot(self.kest.I, pcur_sum)

    def run(self):
        print('1')
        self.asm_v()
        print('2')
        self.set_nodes_loads()
        print('3')
        for element in self.elements:
            if not local_matrix(element):
                return
            print('.')
        print('4')
        self.full_structure_matrix()
        print('5')
        for _element in self.elements:
            print('.')
            get_data(_element)
