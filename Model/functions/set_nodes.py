# def set_nodes(element, nodes):
#     # __nodes = sorted(nodes, lambda x: x.position, reverse=False)
#     for node in nodes:
#         if element.vector.start == node.position:
#             element.nodeStart = node
#         elif element.vector.end == node.position:
#             element.nodeEnd = node
#     element._set_asm()
#     return element

#
# def set_nodes(vectors, nodes):
#     for vector in vectors:
#         for node in nodes:
#             if vector.start == node.position:
#                 vector.nodeStart = node
#             elif vector.end == node.position:
#                 vector.nodeEnd = node
#     return vectors


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
