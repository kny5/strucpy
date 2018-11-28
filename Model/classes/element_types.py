import math
from itertools import count as it_counts
import numpy as np


class Geometry:
    def __init__(self, array_np):

        x_min = array_np[:, 0].min()
        y_min = array_np[:, 1].min()
        z_min = array_np[:, 2].min()

        x_max = array_np[:, 0].max()
        y_max = array_np[:, 1].max()

        magic = [(x_max + x_min) / 2, (y_max + y_min) / 2, z_min]



        # translate = []
        #
        for vector in array_np:
            np.subtract(vector, magic)

        # self.array = np.asarray(translate)
        # data axis
        x_min = array_np[:, 0].min()
        x_max = array_np[:, 0].max()
        # y axis
        y_min = array_np[:, 1].min()
        y_max = array_np[:, 1].max()
        # z axis
        z_min = array_np[:, 2].min()
        z_max = array_np[:, 2].max()

        self.centroid = ((x_max + x_min) / 2, (y_max + y_min) / 2, (z_max + z_min) / 2)
        self.point_max = (x_max, y_max, z_max)
        self.max = max(self.point_max)


class Vector:
    def __init__(self, start, end):
        if start[2] > end[2]:
            self.start = end
            self.end = start
        else:
            self.start = start
            self.end = end

        self.long = abs((((self.end[0] - self.start[0]) ** 2) +
                         ((self.end[1] - self.start[1]) ** 2) +
                         ((self.end[2] - self.start[2]) ** 2)) ** 0.5)

        plane_xz = (((self.end[0] - self.start[0]) ** 2) +
                    ((self.end[2] - self.start[2]) ** 2)) ** 0.5

        if plane_xz != 0:
            _nu_ = math.degrees(math.asin((self.end[2] - self.start[2]) / plane_xz))
            if self.end[0] - self.start[0] < 0:
                self.nu = 180 - _nu_
            else:
                self.nu = _nu_
        else:
            self.nu = 0

        self.lm = math.degrees(math.asin((self.end[1] - self.start[1]) / self.long))

    def reformat(self):
        if self.start[2] > self.end[2]:
            start = self.start
            self.start = self.end
            self.end = start


class Node:
    n_id_gen = it_counts(1)

    def __init__(self, position):
        self.n_id = next(self.n_id_gen)
        self.position = position
        self.n_ve = []
        self.conf_springs = {'dx': 0.0, 'dy': 0.0, 'dz': 0.0, 'mx': 0.0, 'my': 0.0, 'mz': 0.0}
        self.conf_vcn = {'dx': 0.0, 'dy': 0.0, 'dz': 0.0, 'mx': 0.0, 'my': 0.0, 'mz': 0.0}
        self.conf = {'dx': True, 'dy': True, 'dz': True, 'mx': True, 'my': True, 'mz': True}
        self.n_springs = list(self.conf_springs.values())
        self.n_vcn = list(self.conf_vcn.values())


class Element:
    """Propiedades aplicadas para todos los elementos"""
    _SCC: int = 20
    _poisson: float = 0.25
    _e_id_gen = it_counts(1)

    def __init__(self, vector):
        self.e_id = next(self._e_id_gen)
        self.vector = vector
        self.kv: float = 0.0
        self.kh: float = 0.0
        self.wy: float = 0.0
        self.wz: float = 0.0
        self.aw: float = 0.0
        self.marco: float = 0.0
        self.of_type = None
        self.nodeStart = None
        self.nodeEnd = None
        self.ve = None

    def _set_asm(self):
        self.ve = self.nodeStart.n_ve + self.nodeEnd.n_ve


class Concrete:
    """Propiedades específicas del concreto"""

    b: float = 0.0
    h: float = 0.0
    b_prima: float = 0.0
    e: float = 221.359
    p_mat: float = 2.4

    def _a1(self):
        return self.b

    def _a2(self):
        return self.h

    def _area(self) -> float:
        return self.b_prima * self.h

    def _izz(self) -> float:
        return (self.b_prima * self.h ** 3) / 12

    def _iyy(self) -> float:
        return (self.h * self.b_prima ** 3) / 12

    def _j(self) -> float:
        return ((self.h / 2) * (self.b_prima / 2) ** 3) * \
               ((16 / 3) - (3.36 * ((self.b_prima / 2) / (self.h / 2)) *
                            (1 - (self.b_prima / 2) ** 4 / (12 * (self.h / 2) ** 4))))


class Custom:
    """Tipo de elemento con propiedades personalizadas"""

    b: float = 0.0
    h: float = 0.0
    izz: float = 0.0
    iyy: float = 0.0
    j_: float = 0.0
    e: float = 0.0
    p_mat: float = 0.0
    area_: float = 0.0

    def _a1(self):
        return self.b

    def _a2(self):
        return self.h

    def _area(self):
        return self.area_

    def _izz(self):
        return self.izz

    def _iyy(self):
        return self.iyy

    def _j(self):
        return self.j_


class Or:
    """Propiedades específicas del tipo OR"""

    d: float = 0.0
    bf: float = 0.0
    tf: float = 0.0
    tw: float = 0.0
    e: float = 0.0
    p_mat: float = 7.849

    armour: bool = False

    def _a1(self):
        return self.bf

    def _a2(self):
        return self.d

    def _area(self) -> float:
        return (self.d * self.bf) - \
               ((self.d - 2 * self.tf) *
                (self.bf - 2 * self.tw))

    def _izz(self) -> float:
        return 2 * ((self.bf * self.tf ** 3) / 12) + \
               2 * ((self.tw * (self.d - 2 * self.tf) ** 3) / 12) + \
               2 * ((self.bf * self.tf) * ((self.d - self.tf) / 2) ** 2)

    def _iyy(self) -> float:
        return 2 * ((self.d * self.tw ** 3) / 12) + \
               2 * ((self.tf * (self.bf - 2 * self.tw) ** 3) / 12) + \
               2 * ((self.d * self.tw) * ((self.bf - self.tw) / 2) ** 2)

    def _j(self) -> float:
        return (2 * ((self.bf - self.tw) * (self.d - self.tf)) ** 2) / \
               (((self.bf - self.tw) / self.tf) + ((self.d - self.tf) / self.tw))


class Ir:
    """Propiedades específicas del tipo IR"""

    d: float = 0.0
    tf: float = 0.0
    bf: float = 0.0
    tw: float = 0.0
    e: float = 0.0
    p_mat: float = 7.849

    armour: bool = False

    def _a1(self):
        return self.bf

    def _a2(self):
        return self.d

    def _area(self) -> float:
        return (2 * self.bf * self.tf) + ((self.d - 2 * self.tf) * self.tw)

    def _izz(self) -> float:
        return 2 * ((self.bf * (self.tf ** 3)) / 12) + \
               (self.tw * (self.d - (2 * self.tf)) ** 3 / 12) + \
               2 * ((self.bf * self.tf) * ((self.d - self.tf) / 2) ** 2)

    def _iyy(self) -> float:
        return 2 * ((self.tf * self.bf ** 3) / 12) + \
               (((self.d - 2 * self.tf) * self.tw ** 3) / 12)

    def _j(self) -> float:
        return ((2 * self.bf * self.tf ** 3) + ((self.d - self.tf) * self.tw ** 3)) / 3


class Oc:
    """Propiedades específicas del tipo OC"""
    d: float = 0.0
    t: float = 0.0
    e: float = 0.0
    p_mat: float = 7.849

    armour: bool = False

    def _a1(self):
        return self.d

    def _a2(self):
        return self.d

    def _area(self) -> float:
        return math.pi * ((self.d / 2) ** 2) - (math.pi * ((self.d - (2 * self.t)) / 2) ** 2)

    def _izz(self) -> float:
        return (0.25 * math.pi * (self.d / 2) ** 4) - \
               ((0.25 * math.pi) * ((self.d - 2 * self.t) / 2) ** 4)

    def _iyy(self):
        return self._izz()

    def _j(self) -> float:
        return ((math.pi * self.d ** 4) / 32) - ((math.pi * (self.d - 2 * self.t) ** 4) / 32)
