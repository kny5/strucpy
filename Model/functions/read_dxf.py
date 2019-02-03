import dxfgrabber as dxfg
from Model.classes.element_types import Vector
from numpy import subtract
# import time
# from Model.functions.set_nodes import set_nodes
# from Model.functions.asm_vector import asm_v
# from operator import add
# from functools import reduce


def read_dxf(file):
    # convention_switch_array = []
    vector_objects = []
    # points = set([])
    # start_arr = []
    # end_arr = []
    array_dxf = [[line.start, line.end] for line in dxfg.readfile(file).entities._entities if isinstance(line, dxfg.dxfentities.Line)]
    min_point = min(min(array_dxf))
    # max_point = max(max(array_dxf))

    for line in array_dxf:
        # print("#" * 10)
        # print(line.__len__())
        translated_origin = subtract(line, min_point)
        st = translated_origin[0]
        nd = translated_origin[1]
        start = (st[0], st[2], -st[1])
        end = (nd[0], nd[2], -nd[1])
        # points.add(start)
        # points.add(end)
        # convention_switch_array += [start, end]
        vector_objects.append(Vector(start, end))

    # max_point_convention = max(convention_switch_array)
    # min_point_convention = min(convention_switch_array)

    return vector_objects # , list(points)


# start = time.time()
# data = read_dxf('c:/repos/strucpy/dev_files/dxf/irregular2.dxf')
# print(time.time()-start)
# vectors = data[1]
# elements_nodes = set_nodes(vectors, data[0])
# print(time.time()-start)
# freedomDegrees = asm_v(elements_nodes[1])
# asm_vector = [x.asm() for x in elements_nodes[0]]
# print(time.time()-start)
