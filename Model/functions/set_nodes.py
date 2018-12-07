from Model.classes.element_types import Node, Element


def set_nodes(vectors, arr_points):
    list_points = sorted(set(arr_points))
    nodes = list(map(Node, list_points))
    dict_points = dict(zip(list_points, nodes))
    elements = list(map(Element, vectors))
    for element in elements:
        element.nodeStart = dict_points[element.vector.start]
        element.nodeEnd = dict_points[element.vector.end]
    return elements, nodes
