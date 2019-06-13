""" not in use, already written in control class"""
# from Model.classes.element_types import Element
from classes import Node
from functools import reduce
from operator import add


def set_nodes(self):
    list_points = reduce(add, [vector.pos for vector in self.program.vectors if vector.parent is None])
    nodes = list(map(Node, list_points))
    dict_points = dict(zip(list_points, nodes))

    for key in dict_points.keys():
        if not key in self.dict_nodes:
            self.dict_nodes[key] = dict_points[key]

    # elements = control_elements

    # for element in elements:
    #     element.nodeStart = dict_points[element.vector.start]
    #     element.nodeEnd = dict_points[element.vector.end]
        # element.nodeStart.assigned = True
        # element.nodeEnd.assigned = True
    return # elements, nodes
