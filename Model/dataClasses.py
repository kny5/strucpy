import math
import itertools

"""
Catalogo de clases
"""


class workspace:
    def __init__(self, x, y, z):
        self.id = " "
        self.max_x = x
        self.max_y = y
        self.max_z = z
        self.origin = [0, 0, 0]
        self.max_all = [x, y, z]


class Nodo():
    id_gen = itertools.count(1)
    def __new__(self, x, y, z, universe):
        while x in range(0, universe.max_x) and y in range(0, universe.max_y) and z in range(0, universe.max_z):
            try:
                return super(Nodo, self).__new__(self)
                break

            except:
                return None

    def __init__(self, x, y, z, *args):
        self.id = str(next(self.id_gen))
        self.x = x
        self.y = y
        self.z = z
        self.position = [x, y, z]

    def set_ve(self, dx, dy, dz, mx, my, mz):
        self.ve__ = [dx, dy, dz, mx, my, mz]

class Elemento:
    """Propiedades generales de elemento"""
    countrefs = 0

    id_gen = itertools.count(1)

    def __init__(self):
        self.l = 0
        self.id = str(next(self.id_gen))
        self.nu = 0  # ángulo plano xz
        self.lm = 0  # ángulo plano xy
        self.kv = 0  # módulo de reacción vertical
        self.kh = 0  # módulo de reacción horizontal
        self.wy = 0  # carga uniformemente dist, TON/ML y
        self.wz = 0  # carga uniforme... z
        self.aw = 0  # angulo de carga
        self.apoyos = []

    def set_nodos(self, nodo_0, nodo_1):
        self.nodos = [nodo_0, nodo_1]
        self.abs = [self.nodos[1].x - self.nodos[0].x,\
                    self.nodos[1].y - self.nodos[0].y,\
                    self.nodos[1].z - self.nodos[0].z]

    def long(self):
        ab = abs(((self.abs[0] ** 2) + (self.abs[1] ** 2) + (self.abs[2] ** 2)) ** 0.5)
        return ab

    def alpha(self):
        alpha = math.degrees(math.acos(self.abs[0]/self.long()))
        return alpha

    def beta(self):
        beta = math.degrees(math.acos(self.abs[1]/self.long()))
        return beta

    def gama(self):
        gama = math.degrees(math.acos(self.abs[2]/self.long()))
        return gama

    def vector_ensamble(self):
        ve = []
        for i in self.nodos[0].ve__:
            ve.append(i)
        for j in self.nodos[1].ve__:
            ve.append(j)
        return ve


class Concreto(Elemento):
    """Propiedades específicas del concreto"""
    Elemento.countrefs += 1

    def __init__(self, *args):
        Elemento.__init__(self, *args)
        self.b = 0  # ancho de zapata
        self.h = 0  # altura de zapata
        self.b_prima = 0  # ancho de Contratrabe
        self.e = 0  # modulo de elasticidad
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
            ((16 / 3) - (3.36 * ((self.b_prima / 2) / (self.h / 2)) * \
                         (1 - (self.b_prima / 2) ** 4 / (12 * (self.h / 2) ** 4))))
        return x


class Especial(Elemento):
    Elemento.countrefs += 1

    def __init__(self, *args):
        Elemento.__init__(self, *args)
        self.b = 0  # ancho de la sección
        self.h = 0  # altura de la sección
        self.ixx = 0  # inercia del eje x
        self.iyy = 0  # inercia del eje y
        self.j = 0  # momento polar de inercia
        self.e = 0  # modulo de elasticidad
        self.peso_p = 0  # peso propio
        self.a1 = self.b
        self.a2 = self.h
        self.area = 0


class Acero(Elemento):
    def __init__(self, *args):
        Elemento.__init__(self, *args)
        self.e = 0
        self.p_mat = 7.849


class Or(Acero):
    """Propiedades específicas del tipo OR"""
    Elemento.countrefs += 1

    def __init__(self, *args):
        Acero.__init__(self, *args)
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


class Ir(Acero):
    """Propiedades específicas del tipo IR"""
    Elemento.countrefs += 1

    def __init__(self, *args):
        Acero.__init__(self, *args)
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


class Oc(Acero):
    """Propiedades específicas del tipo OC"""
    Elemento.countrefs += 1

    def __init__(self, *args):
        Acero.__init__(self, *args)
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
        x = self.izz()
        return x

    def j(self):
        x = ((math.pi * self.d ** 4) / 32) - ((math.pi * (self.d - 2 * self.t) ** 4) / 32)
        return x
