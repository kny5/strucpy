def set_nodes(element, nodes):
    for node in nodes:
        if element.vector.start == node.position:
            element.nodeStart = node
        elif element.vector.end == node.position:
            element.nodeEnd = node
    element._set_asm()
    return element


# def set_nodes(vectors, nodes):
#     for vector in vectors:
#         for node in nodes:
#             if vector.start == node.position:
#                 vector.nodeStart = node
#             elif vector.end == node.position:
#                 vector.nodeEnd = node
#     return vectors
