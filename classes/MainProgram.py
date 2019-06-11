from functions.local_matrix import local_matrix
from functions.get_data import get_data
# from Model.functions.set_nodes import set_nodes
# from Model.functions.asm_vector import asm_v
import numpy as np
from numpy import matlib
# from classes.element_types import Element
# from classes.geometry import Node
# from functools import reduce
# from operator import add
from ui_views.Results import Ui_Form as Results


class Program:
    def __init__(self, parent):
        self.parent = parent
        self.vectors = set([])
        # self.nodes = list(self.parent.dict_nodes.values())
        self.elements = []
        self.vcn = []
        self.v_springs = []
        self.freedom = 0
        self.kest = []
        self.pcur_ = []
        self.dn_est = []

    @property
    def nodes(self):
        return list(self.parent.dict_nodes.values())

    # def b_aproximation(self):
    #     pass

    # def set_elements(self):
    #     self.elements = list(map(Element, self.vectors))

    def asm_v(self):
        # print("asm_v")
        self.freedom = 0
        for node in self.nodes:
            n_ve = []
            for key in node.conf.values():
                for val in key.values():
                    if type(val) is bool:
                        if val == True:
                            self.freedom += 1
                            n_ve.append(self.freedom)
                        else:
                            n_ve.append(0)
            node.n_ve = n_ve
        print('grados de libertad')
        print(self.freedom)
        # return freedom

    def full_structure_matrix(self):
        print('Estructura ' + str(self.freedom))
        self.kest = matlib.zeros(shape=(self.freedom, self.freedom))
        self.pcur_ = np.zeros(self.freedom)
        for element in self.elements:
            NStart = self.parent.dict_nodes[element.vector.start]
            NEnd = self.parent.dict_nodes[element.vector.end]
            setattr(element, 've', NStart.n_ve + NEnd.n_ve)
            print('vector de ensamble de elemento ' + str(element.e_id))
            print(element.ve)
            for _c, _i in enumerate(element.ve):
                if _i != 0:
                    self.pcur_[_i - 1] += element.data.pc_[_c]
                for _k, _j in enumerate(element.ve):
                    if _j != 0:
                        self.kest[_i - 1, _j - 1] += element.data.kebg.item(_c, _k)
        print(self.kest)

    # def set_nodes(self):
    #     list_points = reduce(add, [[vector.start, vector.end] for vector in self.vectors])
    #     self.nodes = list(map(Node, list_points))
    #     self.nodes_dict = dict(zip(list_points, self.nodes))

    def set_nodes_loads(self, random_loads=None):
        self.vcn = []
        self.v_springs = []
        for node in self.nodes:
            # print(node)
            self.vcn += node.n_vcn
            self.v_springs += node.n_springs
            # print(self.pcur_)
            # print("*" * 13)
            # print(self.vcn)
            # print(self.v_springs)
        pcur_sum = np.add(self.pcur_, self.vcn)
        print('vector carga solo de la estructura')
        print(self.pcur_)
        if not random_loads == None:
            pcur_sum_random_loads = np.add(pcur_sum, np.asarray(random_loads))
            self.dn_est = np.dot(self.kest.I, pcur_sum_random_loads)
        else:
            self.dn_est = np.dot(self.kest.I, pcur_sum)

        vdgen_p = np.zeros(12)
        for node in self.nodes:
            for k, i_ in enumerate(node.n_ve):
                if i_ != 0:
                    vdgen_p[k] = self.dn_est[0, i_ - 1]
                else:
                    pass
        self.vdgen_p = vdgen_p

    def run(self):
        # print('1')
        print('bug ...')
        print(self.elements)
        # print('2')
        for _element in self.elements:
            local_matrix(_element)

        self.asm_v()
        self.full_structure_matrix()
        # print('3')
        self.set_nodes_loads()
        # print('4')
        # print('4')
        # self.full_structure_matrix()
        # print('5')
        for _element in self.elements:
            # print('.')
            get_data(self, _element)
            # print(_element.results.__dict__)

        self.ui_results = []
        print(self.elements.__len__())
        for __element in self.elements:
            u = Results(__element)
            u.show()
            self.ui_results.append(u)

