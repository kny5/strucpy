import math
import itertools
from gc import get_objects

"""
Catalogo de clases
"""

ac_nodo = 0


class Nodo:
    n_id_gen = itertools.count(1)

    def __init__(self, position, **kwargs):
        self.n_id = str(next(self.n_id_gen))
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.position = position
#   def set_ve(self, dx=True, dy=True, dz=True, mx=True, my=True, mz=True):
        self._veBool = (kwargs['dx'], kwargs['dy'], kwargs['dz'], kwargs['mx'], kwargs['my'], kwargs['mz'])
        self.ve_parcial = []
        for _bool in self._veBool:
            if _bool == True:
                global ac_nodo
                ac_nodo += 1
                self.ve_parcial.append(ac_nodo)
            else:
                self.ve_parcial.append(0)
    def tolist(self):
        return [self.position[0], self.position[1], self.position[2]]


class Elemento:
    """Propiedades generales de elemento"""
    countrefs = 0

    e_id_gen = itertools.count(1)

    def __init__(self):
        #self.l = 0
        self.e_id = str(next(self.e_id_gen))
        self.nu = 0  # ángulo plano xz
        self.lm = 0  # ángulo plano xy
        self.kv = 0  # módulo de reacción vertical
        self.kh = 0  # módulo de reacción horizontal
        self.wy = 0  # carga uniformemente dist, TON/ML y
        self.wz = 0  # carga uniforme... z
        self.aw = 0  # angulo de carga
        self.apoyos = None
        self.start = None
        self.end = None
        self._nodoStart = None
        self._nodoEnd = None
        self.start_conf = {'dx': True, 'dy': True, 'dz': True, 'mx': True, 'my': True, 'mz': True}
        self.end_conf = {'dx': True, 'dy': True, 'dz': True, 'mx': True, 'my': True, 'mz': True}
        self.ve = None


    def set_nodes(self):
        if self.ve is not None:
            print('updating?')
            #global ac_nodo
            #ac_nodo = 0
        if self.start != self.end:# and self.start is not None and self.end is not None and self.ve is None:
            if self.e_id == 1:
                self._nodoStart = Nodo(self.start, **self.start_conf)
                self._nodoEnd = Nodo(self.end, **self.end_conf)
                self.ve = self._nodoStart.ve_parcial + self._nodoEnd.ve_parcial
            else:
                for obs_ in get_objects():
                    if isinstance(obs_, Nodo):
                        print('Existen instancias de Nodo')
                        if obs_.position == self.start:
                            self._nodoStart = obs_
                            print('nodo existente para start')
                        elif obs_.position == self.end:
                            self._nodoEnd = obs_
                            print('nodo existente para end')

            if self._nodoStart is None:
                self._nodoStart = Nodo(self.start, **self.start_conf)
            if self._nodoEnd is None:
                self._nodoEnd = Nodo(self.end, **self.end_conf)
                # else
            self.ve = self._nodoStart.ve_parcial + self._nodoEnd.ve_parcial
            self.l = abs((((self.end[0] - self.start[0]) ** 2) + ((self.end[1] - self.start[1]) ** 2) + (
                        (self.end[2] - self.start[2]) ** 2)) ** 0.5)

        else:
            print("Error No Start or End points")
        if self.start == self.end:
            print('values are the same')
            print(self.start, self.end)

        return self.ve


#
# def alpha(self):
#    alpha = math.degrees(math.acos(self.abs[0]/self.long()))
#    return alpha
#
# def beta(self):
#    beta = math.degrees(math.acos(self.abs[1]/self.long()))
#    return beta
#
# def gama(self):
#    gama = math.degrees(math.acos(self.abs[2]/self.long()))
#    return gama
#
# def vector_ensamble(self):
#    ve = []
#    for i in self.nodos[0].ve__:
#        ve.append(i)
#    for j in self.nodos[1].ve__:
#        ve.append(j)
#    return ve
#


class Concreto(Elemento):
    """Propiedades específicas del concreto"""
    Elemento.countrefs += 1

    def __init__(self):
        Elemento.__init__(self)
        self.b = 0  # ancho de zapata
        self.h = 0  # altura de zapata
        self.b_prima = 0  # ancho de Contratrabe
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
            ((16 / 3) - (3.36 * ((self.b_prima / 2) / (self.h / 2)) * \
                         (1 - (self.b_prima / 2) ** 4 / (12 * (self.h / 2) ** 4))))
        return x


class Especial(Elemento):
    Elemento.countrefs += 1

    def __init__(self):
        Elemento.__init__(self)
        self.b = 0  # ancho de la sección
        self.h = 0  # altura de la sección
        self.izz_ = 0  # inercia del eje x
        self.iyy_ = 0  # inercia del eje y
        self.j_ = 0  # momento polar de inercia
        self.e = 0  # modulo de elasticidad
        self.p_mat = 0  # peso propio
        # self.a1 = self.b
        # self.a2 = self.h
        self.area_ = 0

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


class Acero(Elemento):
    def __init__(self):
        Elemento.__init__(self)
        self.e = 0
        self.p_mat = 7.849
        self.armadura = False


class Or(Acero):
    """Propiedades específicas del tipo OR"""
    Elemento.countrefs += 1

    def __init__(self):
        Acero.__init__(self)
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

    def __init__(self):
        Acero.__init__(self)
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

    def __init__(self):
        Acero.__init__(self)
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
