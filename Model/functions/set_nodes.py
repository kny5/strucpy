from Model.classes.element_types import Element
from Model.classes.geometry import Node
from functools import reduce
from operator import add


def set_nodes(vectors):
    list_points = reduce(add, [[vector.start, vector.end] for vector in vectors])
    nodes = list(map(Node, list_points))
    dict_points = dict(zip(list_points, nodes))

    elements = list(map(Element, vectors))

    for element in elements:
        element.nodeStart = dict_points[element.vector.start]
        element.nodeEnd = dict_points[element.vector.end]
    return elements, nodes
