from Model.classes.element_types import Vector, Element


def elementize(vector):
    return Element(vector)


vectors = [Vector((0,0,0), (1,1,1)), Vector((1,1,1), (2,2,2))]
Elements = list(map(elementize, vectors))

