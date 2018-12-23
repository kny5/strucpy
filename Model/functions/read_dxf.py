import dxfgrabber as dxfg
from Model.classes.element_types import Vector
import time
from Model.functions.set_nodes import set_nodes
from Model.functions.asm_vector import asm_v
# from operator import add
# from functools import reduce


def read_dxf(file):
    convention_switch_array = []
    vector_objects = []
    array_dxf = [[line.start, line.end] for line in dxfg.readfile(file).entities._entities if isinstance(line, dxfg.dxfentities.Line)]
    for line in array_dxf:
        start = (line[0][0], line[0][2], -line[0][1])
        end = (line[1][0], line[1][2], -line[1][1])
        convention_switch_array += [start, end]
        vector_objects.append(Vector(start, end))

    max_point_convention = max(convention_switch_array)
    min_point_convention = min(convention_switch_array)

    return convention_switch_array, vector_objects, max_point_convention, min_point_convention


start = time.time()
data = read_dxf('c:/repos/strucpy/dev_files/dxf/irregular2.dxf')
print(time.time()-start)
vectors = data[1]
elements_nodes = set_nodes(vectors, data[0])
print(time.time()-start)
freedomDegrees = asm_v(elements_nodes[1])
asm_vector = [x.asm() for x in elements_nodes[0]]
print(time.time()-start)
