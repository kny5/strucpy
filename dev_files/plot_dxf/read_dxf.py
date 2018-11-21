import dxfgrabber as dxfg
from element_types import Vector


def read_dxf(file):
    vectors = [Vector(entity.start, entity.end)
               for entity in dxfg.readfile(file).entities._entities
               if isinstance(entity, dxfg.dxfentities.Line)]

    return vectors
