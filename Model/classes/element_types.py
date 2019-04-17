"""Este archivo debe pasar a revisión, debido a que type contiene atributos de una sección,
por lo que debería de crearse una clase especial llamada, section type y material."""
import math
from itertools import count as it_counts


class Parameters:
    sections = 20
    poisson = 0.25


class Element(Parameters):
    _e_id_gen = it_counts(1)

    def __init__(self, vector):
        vector.set_parent(self)
        super().__init__()
        self.e_id = next(self._e_id_gen)
        self.vector = vector
        self.loads = Loads()
        self.type = None
        self.marco: int = 0
        self.data = Data()
        self.results = Results()
        self.kv: float = 0.0
        self.kh: float = 0.0

    # move this to control class
    def set_type(self, index):
        materials = [Concrete, Custom, Or, Ir, Oc]
        selected = materials[index]
        self.type = selected()
        return


class Results:
    def __init__(self):
        pass


class Data:
    def __init__(self):
        self.kzz = None
        self.kyy = None
        self.mzz = None
        self.myy = None
        self.vzz = None
        self.vyy = None
        self.tr = None
        self.keb = None
        self.kebg = None
        self.pp_scc = None
        self.dlzz = None
        self.dlyy = None
        self.mdlzz = None
        self.mdlyy = None
        self.pculocal = None
        self.pc_ = None


class Loads:
    def __init__(self, wy=0.0, wz=0.0, aw=0.0):
        self.wy: float = wy
        self.wz: float = wz
        self.aw: float = aw


# Materiales disponibles

class Concrete:
    """Propiedades específicas del concreto"""

    def __init__(self):
        self.b: float = 0.0
        self.h: float = 0.0
        self.b_prima: float = 0.0
        self.e: float = 221.359
        self.p_mat: float = 2.4

    @property
    def a1(self):
        return self.b

    @property
    def a2(self):
        return self.h

    @property
    def area(self) -> float:
        return self.b_prima * self.h

    @property
    def izz(self) -> float:
        return (self.b_prima * self.h ** 3) / 12

    @property
    def iyy(self) -> float:
        return (self.h * self.b_prima ** 3) / 12

    @property
    def j(self) -> float:
        return ((self.h / 2) * (self.b_prima / 2) ** 3) * \
               ((16 / 3) - (3.36 * ((self.b_prima / 2) / (self.h / 2)) *
                            (1 - (self.b_prima / 2) ** 4 / (12 * (self.h / 2) ** 4))))


class Custom:
    """Tipo de elemento con propiedades personalizadas"""

    def __init__(self):
        self.b: float = 0.0
        self.h: float = 0.0
        self.izz_: float = 0.0
        self.iyy_: float = 0.0
        self.j_: float = 0.0
        self.e: float = 0.0
        self.p_mat: float = 0.0
        self.area_: float = 0.0

    @property
    def a1(self):
        return self.b

    @property
    def a2(self):
        return self.h

    @property
    def area(self):
        return self.area_

    @property
    def izz(self):
        return self.izz_

    @property
    def iyy(self):
        return self.iyy_

    @property
    def j(self):
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

    @property
    def a1(self):
        return self.bf

    @property
    def a2(self):
        return self.d

    @property
    def area(self) -> float:
        return (self.d * self.bf) - \
               ((self.d - 2 * self.tf) *
                (self.bf - 2 * self.tw))

    @property
    def izz(self) -> float:
        return 2 * ((self.bf * self.tf ** 3) / 12) + \
               2 * ((self.tw * (self.d - 2 * self.tf) ** 3) / 12) + \
               2 * ((self.bf * self.tf) * ((self.d - self.tf) / 2) ** 2)

    @property
    def iyy(self) -> float:
        return 2 * ((self.d * self.tw ** 3) / 12) + \
               2 * ((self.tf * (self.bf - 2 * self.tw) ** 3) / 12) + \
               2 * ((self.d * self.tw) * ((self.bf - self.tw) / 2) ** 2)

    @property
    def j(self) -> float:
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

    @property
    def a1(self):
        return self.bf

    @property
    def a2(self):
        return self.d

    @property
    def area(self) -> float:
        return (2 * self.bf * self.tf) + ((self.d - 2 * self.tf) * self.tw)

    @property
    def izz(self) -> float:
        return 2 * ((self.bf * (self.tf ** 3)) / 12) + \
               (self.tw * (self.d - (2 * self.tf)) ** 3 / 12) + \
               2 * ((self.bf * self.tf) * ((self.d - self.tf) / 2) ** 2)

    @property
    def iyy(self) -> float:
        return 2 * ((self.tf * self.bf ** 3) / 12) + \
               (((self.d - 2 * self.tf) * self.tw ** 3) / 12)

    @property
    def j(self) -> float:
        return ((2 * self.bf * self.tf ** 3) + ((self.d - self.tf) * self.tw ** 3)) / 3


class Oc:
    """Propiedades específicas del tipo OC"""

    def __init__(self):
        self.d: float = 0.0
        self.t: float = 0.0
        self.e: float = 0.0
        self.p_mat: float = 7.849
        self.armour: bool = False

    @property
    def a1(self):
        return self.d

    @property
    def a2(self):
        return self.d

    @property
    def area(self) -> float:
        return math.pi * ((self.d / 2) ** 2) - (math.pi * ((self.d - (2 * self.t)) / 2) ** 2)

    @property
    def izz(self) -> float:
        return (0.25 * math.pi * (self.d / 2) ** 4) - \
               ((0.25 * math.pi) * ((self.d - 2 * self.t) / 2) ** 4)

    @property
    def iyy(self):
        return self.izz

    @property
    def j(self) -> float:
        return ((math.pi * self.d ** 4) / 32) - ((math.pi * (self.d - 2 * self.t) ** 4) / 32)
