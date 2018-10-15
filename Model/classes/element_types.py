import math
from itertools import count as it_counts


class Vector:
    v_id_gen = it_counts(1)
    counter = 0

    def __init__(self):
        self.start = None
        self.end = None


class Node:

    n_id_gen = it_counts(1)
    counter = 0

    def __init__(self, x, y, z):
        self.n_id = str(next(self.n_id_gen))
        self.x = x
        self.y = y
        self.z = z
        self.position = (x, y, z)
        self.n_ve = []
        self.n_springs = []
        self.n_vcn = []


class Element:
    """Propiedades aplicadas para todos los elementos"""
    SCC = 20
    poisson = 0.25
    _e_id_gen = it_counts(1)

    def __init__(self, vector, kv=0, kh=0, wy=0, wz=0, aw=0, marco=0):
        self.e_id = str(next(self._e_id_gen))
        self.kv = kv  # módulo de reacción vertical
        self.kh = kh  # módulo de reacción horizontal
        self.wy = wy  # carga uniformemente dist, TON/ML y
        self.wz = wz  # carga uniforme... z
        self.aw = aw  # angulo de carga
        self.marco = marco

        self.start = vector.start
        self.end = vector.end

        self.start_conf = {'dx': True, 'dy': True, 'dz': True, 'mx': True, 'my': True, 'mz': True}
        self.end_conf = {'dx': True, 'dy': True, 'dz': True, 'mx': True, 'my': True, 'mz': True}


class Concrete(Element):
    """Propiedades específicas del concreto"""
    def __init__(self, vector, b=0, h=0, b_prima=0, kv=0, kh=0, wy=0, wz=0, aw=0, marco=0):
        Element.__init__(self, vector, kv, kh, wy, wz, aw, marco)
        self.b = b  # ancho de zapata
        self.h = h  # altura de zapata
        self.b_prima = b_prima  # ancho de Contratrabe
        self.e = 221.359  # modulo de elasticidad
        self.p_mat = 2.4  # ton/m3

    def a1(self):
        return self.b

    def a2(self):
        return self.h

    def area(self):
        x = self.b_prima * self.h
        return x

    def izz(self):
        x = (self.b_prima * self.h ** 3) / 12
        return x

    def iyy(self):
        x = (self.h * self.b_prima ** 3) / 12
        return x

    def j(self):
        x = ((self.h / 2) * (self.b_prima / 2) ** 3) * \
            ((16 / 3) - (3.36 * ((self.b_prima / 2) / (self.h / 2)) *
                         (1 - (self.b_prima / 2) ** 4 / (12 * (self.h / 2) ** 4))))
        return x


class Custom(Element):
    def __init__(self, area_=0, p_mat=0, e=0, b=0, h=0, izz_=0, iyy_=0, j_=0, kv=0, kh=0, wy=0, wz=0, aw=0, marco=0, start='(x,y,z)', end='(x,y,z)'):
        Element.__init__(self, start, end, kv, kh, wy, wz, aw, marco)
        self.b = b  # ancho de la sección
        self.h = h  # altura de la sección
        self.izz_ = izz_  # inercia del eje x
        self.iyy_ = iyy_  # inercia del eje y
        self.j_ = j_  # momento polar de inercia
        self.e = e  # modulo de elasticidad
        self.p_mat = p_mat  # peso propio
        self.area_ = area_

    def a1(self):
        return self.b

    def a2(self):
        return self.h

    def area(self):
        return self.area_

    def izz(self):
        return self.izz_

    def iyy(self):
        return self.iyy_

    def j(self):
        return self.j_


class Steel(Element):
    def __init__(self):
        Element.__init__(self)
        self.e = 0
        self.p_mat = 7.849
        self.armadura = False


class Or(Steel):
    """Propiedades específicas del tipo OR"""
    def __init__(self):
        Steel.__init__(self)
        self.d = 0
        self.bf = 0
        self.tf = 0
        self.tw = 0

    def a1(self):
        return self.bf

    def a2(self):
        return self.d

    def area(self):
        x = (self.d * self.bf) - ((self.d - 2 * self.tf) * (self.bf - 2 * self.tw))
        return x

    def izz(self):
        x = 2 * ((self.bf * self.tf ** 3) / 12) + \
            2 * ((self.tw * (self.d - 2 * self.tf) ** 3) / 12) + \
            2 * ((self.bf * self.tf) * ((self.d - self.tf) / 2) ** 2)
        return x

    def iyy(self):
        x = 2 * ((self.d * self.tw ** 3) / 12) + \
            2 * ((self.tf * (self.bf - 2 * self.tw) ** 3) / 12) + \
            2 * ((self.d * self.tw) * ((self.bf - self.tw) / 2) ** 2)
        return x

    def j(self):
        x = (2 * ((self.bf - self.tw) * (self.d - self.tf)) ** 2) / \
            (((self.bf - self.tw) / self.tf) + ((self.d - self.tf) / self.tw))
        return x


class Ir(Steel):
    """Propiedades específicas del tipo IR"""
    def __init__(self):
        Steel.__init__(self)
        self.d = 0
        self.bf = 0
        self.tf = 0
        self.tw = 0

    def a1(self):
        return self.bf

    def a2(self):
        return self.d

    def area(self):
        x = (2 * self.bf * self.tf) + ((self.d - 2 * self.tf) * self.tw)
        return x

    def izz(self):
        x = 2 * ((self.bf * (self.tf ** 3)) / 12) + \
            (self.tw * (self.d - (2 * self.tf)) ** 3 / 12) + \
            2 * ((self.bf * self.tf) * ((self.d - self.tf) / 2) ** 2)
        return x

    def iyy(self):
        x = 2 * ((self.tf * self.bf ** 3) / 12) + \
            (((self.d - 2 * self.tf) * self.tw ** 3) / 12)
        return x

    def j(self):
        x = ((2 * self.bf * self.tf ** 3) + ((self.d - self.tf) * self.tw ** 3)) / 3
        return x


class Oc(Steel):
    """Propiedades específicas del tipo OC"""
    def __init__(self):
        Steel.__init__(self)
        self.d = 0
        self.t = 0

    def a1(self):
        return self.d

    def a2(self):
        return self.d

    def area(self):
        x = math.pi * ((self.d / 2) ** 2) - (math.pi * ((self.d - (2 * self.t)) / 2) ** 2)
        return x

    def izz(self):
        x = (0.25 * math.pi * (self.d / 2) ** 4) - ((0.25 * math.pi) * ((self.d - 2 * self.t) / 2) ** 4)
        return x

    def iyy(self):
        return self.izz()

    def j(self):
        x = ((math.pi * self.d ** 4) / 32) - ((math.pi * (self.d - 2 * self.t) ** 4) / 32)
        return x
