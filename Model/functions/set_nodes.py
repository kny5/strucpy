from Model.classes.element_types import Node


def set_nodes(vectors):
    __set = set([])
    for vector in vectors:
        __set.update(vector.start)
        __set.update(vector.end)
    for node in __set:
        __x = Node(node)
        for vector in vectors:
            if vector.start == node:
                vector.nodeStart = __x
            elif vector.end == node:
                vector.nodeEnd = __x
    # save this as nodes
    return list(__set)

