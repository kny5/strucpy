from Model.classes.element_types import Section
from Model.classes.geometry import Node
from functools import reduce
from operator import add


def set_nodes(vectors):
    # list_points = sorted(set(arr_points))
    list_points = reduce(add, [[vector.start, vector.end] for vector in vectors])
    nodes = list(map(Node, list_points))
    dict_points = dict(zip(list_points, nodes))
    sections = list(map(Section, vectors))
    for section in sections:
        section.nodeStart = dict_points[section.vector.start]
        section.nodeEnd = dict_points[section.vector.end]
    return sections, nodes
