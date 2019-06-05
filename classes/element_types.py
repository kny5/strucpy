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
        super().__init__()
        self.e_id = next(self._e_id_gen)
        vector.set_parent(self)
        self.vector = vector
        self.loads = Loads()
        self.type = None
        self.marco: str = "Default"
        self.data = Data()
        self.results = Results()

    def set_type(self, index):
        if index == 0:
            pass
        else:
            materials = [Concrete, Or, Ir, Oc, Custom]
            selected = materials[index - 1]
            self.type = selected()

    @property
    def ve(self):
        return list(self(self.vector.start))


class Results:
    mx = None
    fax = None
    press_y = None
    press_z = None
    mome_y = None
    mome_z = None
    cor_y = None
    cor_z = None
    dry = None
    drz = None
    desp_imp_antes_y = None


class Data:
    kzz = None
    kyy = None
    mzz = None
    myy = None
    vzz = None
    vyy = None
    tr = None
    keb = None
    kebg = None
    pp_scc = None
    dlzz = None
    dlyy = None
    mdlzz = None
    mdlyy = None
    pculocal = None
    pc_ = None


class Loads:
    wy: float = 0.0
    wz: float = 0.0
    aw: float = 0.0
    kv: float = 0.0
    kh: float = 0.0


# Materiales disponibles
class Concrete:
    """Propiedades específicas del concreto"""
    b: float = 0.0
    h: float = 0.0
    b_prima: float = 0.0
    e: float = 221.359
    p_mat: float = 2.4

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
    b: float = 0.0
    h: float = 0.0
    izz_: float = 0.0
    iyy_: float = 0.0
    j_: float = 0.0
    e: float = 0.0
    p_mat: float = 0.0
    area_: float = 0.0

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
    d: float = 0.0
    bf: float = 0.0
    tf: float = 0.0
    tw: float = 0.0
    e: float = 0.0
    p_mat: float = 7.849
    armour: bool = False

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
    d: float = 0.0
    tf: float = 0.0
    bf: float = 0.0
    tw: float = 0.0
    e: float = 0.0
    p_mat: float = 7.849
    armour: bool = False

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
    d: float = 0.0
    t: float = 0.0
    e: float = 0.0
    p_mat: float = 7.849
    armour: bool = False

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
