import dxfgrabber as dxfg
from Model.classes.element_types import Vector
import time
from Model.functions.set_nodes import set_nodes
from Model.functions.asm_vector import asm_v
# from operator import add
# from functools import reduce


def read_dxf(file):
    __array_vectors = []
    __vectors = []
    x = [x for x in dxfg.readfile(file).entities._entities if isinstance(x, dxfg.dxfentities.Line)]
    for entity in x:
        __array_vectors += [(entity.start[0], entity.start[2], -entity.start[1]), (entity.end[0], entity.end[2], -entity.end[1])]
        __vectors += [Vector((entity.start[0], entity.start[2], -entity.start[1]), (entity.end[0], entity.end[2], -entity.end[1]))]
    return __array_vectors, __vectors


start = time.time()

data = read_dxf('c:/repos/strucpy/dev_files/dxf/lienzo.dxf')

print(time.time()-start)

vectors = data[1]

elements_nodes = set_nodes(vectors, data[0])

print(time.time()-start)

freedomDegrees = asm_v(elements_nodes[1])

asm_vector = [x.asm() for x in elements_nodes[0]]

# loads = []

print(time.time()-start)