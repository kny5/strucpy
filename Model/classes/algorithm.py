# from Model.functions.local_matrix import local_matrix
# from Model.functions.get_data import get_data
# from Model.functions.set_nodes import set_nodes
# from Model.functions.asm_vector import asm_v
import numpy as np
from numpy import matlib
from Model.classes.element_types import Element
from Model.classes.geometry import Node
from functools import reduce
from operator import add
from math import sqrt


class Program:
    def __init__(self, parent):
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

    def set_elements(self):
        self.elements = list(map(Element, self.vectors))

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

    def set_nodes(self):
        list_points = reduce(add, [[vector.start, vector.end] for vector in self.vectors])
        self.nodes = list(map(Node, list_points))
        self.nodes_dict = dict(zip(list_points, self.nodes))

    def set_nodes_loads(self, random_loads=[]):
        for node in self.nodes:
            self.vcn += node.n_vcn
            self.v_springs += node.n_springs

        pcur_sum = np.add(self.pcur_, self.vcn)
        pcur_sum_random_loads = np.add(pcur_sum, np.asarray(random_loads))
        self.dn_est = np.dot(self.kest.I, pcur_sum_random_loads)

    # move this to control class
    def check_all(self):
        print("Checking input data integrity...")
        if self.vectors.__len__() > 0 \
                and self.nodes.__len__() > 0 \
                and self.elements.__len__() > 0 \
                and self.freedom > 0 \
                and self.vcn.__len__() > 0 \
                and self.v_springs.__len__() > 0 \
                and self.nodes_dict.__len__() > 0:

            if self.vectors.__len__() == self.elements.__len__() \
                        and self.freedom == self.vcn.__len__() \
                        and self.freedom == sqrt(self.kest.__len__()):

                if self.kest.__len__() > 0 and self.pcur_.__len__() > 0 \
                        and self.dn_est.__len__() > 0:
                    return True
        else:
            return False

    def check_step_1(self):
        if self.vectors.__len__() > 0:
            for vector in self.vectors:
                vector.reformat_byz()

            return True
        else:
            return False

    def check_step_2(self):
        if self.nodes.__len__() > 0:
            return True
        else:
            return False

    def run(self):
        pass