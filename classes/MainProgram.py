from functions.local_matrix import local_matrix
from functions.get_data import get_data
import numpy as np
from numpy import matlib
import sys

print(sys.getrecursionlimit())

def vector_add(one, two):
    sum = []
    for i, v in enumerate(one, 0):
        sum.append(v + two[i])
    return np.asarray(sum)


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
        self.iterations = 0
        self.trigger = False

    @property
    def nodes(self):
        return list(self.parent.dict_nodes.values())

    # def b_aproximation(self):
    #     pass

    # def set_elements(self):
    #     self.elements = list(map(Element, self.vectors))

    def asm_v(self):
        # # print("asm_v")
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

    def full_structure_matrix(self):
        self.kest = matlib.zeros(shape=(self.freedom, self.freedom))
        self.pcur_ = np.zeros(self.freedom)
        for element in self.elements:
            NStart = self.parent.dict_nodes[element.vector.start]
            NEnd = self.parent.dict_nodes[element.vector.end]
            setattr(element, 've', NStart.n_ve + NEnd.n_ve)
        for element in self.elements:
            for _index, value in enumerate(element.ve):
                if value != 0:
                    self.pcur_[value -1] += element.data.pc_[_index]
                    for __index, _value in enumerate(element.ve):
                        if _value != 0:
                            self.kest[value -1, _value -1] += element.data.kebg.item(_index, __index)

    def set_nodes_loads(self, random_loads=None):
        self.vcn = []
        self.v_springs = []
        for node in self.nodes:
            self.vcn += node.n_vcn
            self.v_springs += node.n_springs

        self.pcur_sum = vector_add(self.vcn, self.pcur_)
        if not random_loads == None:
            pcur_sum_random_loads = np.add(self.pcur_sum, np.asarray(random_loads))
            self.dn_est = np.dot(self.kest.I, pcur_sum_random_loads)
        else:
            self.dn_est = np.dot(self.kest.I, self.pcur_sum)

    def n_run(self):
        for _element in self.elements:
            local_matrix(_element)
        self.asm_v()
        self.full_structure_matrix()
        self.set_nodes_loads()
        for _element in self.elements:
            get_data(self, _element)

    def run(self):
        for _element in self.elements:
            local_matrix(_element)
        self.asm_v()
        self.full_structure_matrix()
        self.set_nodes_loads()
        for _element in self.elements:
            get_data(self, _element)

        for _element in self.elements:
            eval_deact_nodes(_element)
            deact_nodes(_element)
            deact_press_y(_element)

def clear_vals(_element):
    _element.data.nodes_todeact.clear()

def eval_deact_nodes(_element):
    for index, p in enumerate(_element.results.press_y):
        if p > 0:
            _element.data.nodes_todeact.append(index)


def deact_nodes(_element):
    for n in _element.data.nodes_todeact:
        _element.data.kzz[n, n] -= _element.data.f_a
    _element.data.new_kzz = _element.data.kzz


def deact_press_y(_element):
    for i, n in enumerate(_element.data.nodes_todeact):
        _element.results.press_y[n] = 0
        _element.data.nodes_todeact.pop(i)
