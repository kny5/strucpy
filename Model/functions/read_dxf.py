from Model.classes.geometry import Vector, Node
from numpy import subtract
import ezdxf


def read_dxf(file):
    vector_objects = []
    array_dxf = [[line.dxf.start, line.dxf.end] for line in list(ezdxf.readfile(file).modelspace().query('LINE'))]
    min_point = min(min(array_dxf))
    # set_points = set()

    for line in array_dxf:
        translated_origin = subtract(line, min_point)
        st = translated_origin[0]
        nd = translated_origin[1]
        start = (st[0], st[2], -st[1])
        end = (nd[0], nd[2], -nd[1])
        vector_objects.append(Vector(start, end))
        # set_points.add(start)
        # set_points.add(end)

    return set(vector_objects) # , set(map(Node, set_points))


def save_dxf(vectors, filename):
    file = ezdxf.new('R2018')
    model = file.modelspace()
    for vector in vectors:
        model.add_line(vector.start, vector.end)
    file.saveas(filename)
