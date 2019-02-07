import math
from itertools import count as it_counts


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

    def asm(self):
        self.ve = self.nodeStart.n_ve + self.nodeEnd.n_ve


class Concrete:
    """Propiedades específicas del concreto"""

    def __init__(self):
        self.b: float = 0.0
        self.h: float = 0.0
        self.b_prima: float = 0.0
        self.e: float = 221.359
        self.p_mat: float = 2.4

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

    def __init__(self):
        self.b: float = 0.0
        self.h: float = 0.0
        self.izz: float = 0.0
        self.iyy: float = 0.0
        self.j_: float = 0.0
        self.e: float = 0.0
        self.p_mat: float = 0.0
        self.area_: float = 0.0

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

    def __init__(self):
        self.d: float = 0.0
        self.bf: float = 0.0
        self.tf: float = 0.0
        self.tw: float = 0.0
        self.e: float = 0.0
        self.p_mat: float = 7.849
        self.armour: bool = False

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

    def __init__(self):
        self.d: float = 0.0
        self.tf: float = 0.0
        self.bf: float = 0.0
        self.tw: float = 0.0
        self.e: float = 0.0
        self.p_mat: float = 7.849
        self.armour: bool = False

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

    def __init__(self):
        self.d: float = 0.0
        self.t: float = 0.0
        self.e: float = 0.0
        self.p_mat: float = 7.849
        self.armour: bool = False

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
