import dxfgrabber as dxfg
from Model.classes.element_types import Vector, Node, Element
import time
from Model.functions.set_nodes import set_nodes
from Model.functions.asm_vector import asm_v


def read_dxf(file):
    __array_vectors = []
    __vectors = []
    x = [x for x in dxfg.readfile(file).entities._entities if isinstance(x, dxfg.dxfentities.Line)]
    for entity in x:
        __array_vectors += [(entity.start[0], entity.start[2], -entity.start[1]), (entity.end[0], entity.end[2], -entity.end[1])]
        __vectors += [Vector((entity.start[0], entity.start[2], -entity.start[1]), (entity.end[0], entity.end[2], -entity.end[1]))]
    return __array_vectors, __vectors


start = time.time()
data = read_dxf('c:/repos/strucpy/dev_files/dxf/test.dxf')
nodes = list(map(Node, set(data[0])))

# vectors = set_nodes(data[1], nodes)

freedomDegrees = asm_v(nodes)
e_list = list(map(Element, data[1]))
elements = list(map(lambda x: set_nodes(x, nodes), e_list))

print(time.time()-start)
