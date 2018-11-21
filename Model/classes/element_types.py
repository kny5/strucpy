import math
from itertools import count as it_counts
from numpy import asarray
import numpy as np


class Value:
    value = None

    def __init__(self, default, _max=float('inf'), _min=0.0, text='empty', units='u'):

        self.__type = type(default)
        self.value = default

        self.__str = text
        self.__max = _max
        self.__min = _min
        self.__units = units

    # def __float__(self):
    #     if isinstance(self.value, float):
    #         return self.value
    #     else:
    #         raise TypeError

    def __str__(self):
        return self.__str

    def _set_value(self, value):
        if type(value) == self.__type:
            if not isinstance(self.value, str) or not isinstance(self.value, object) \
                    and self.__max is not None and self.__min is not None:
                if self.__min <= value <= self.__max:
                    self.value = value
                else:
                    print('fuera de rango')
                    raise ValueError
            else:
                self.value = value
        else:
            print('tipo de dato incorrecto')
            raise TypeError


class Geometry:
    gem_id_gen = it_counts(1)

    def __init__(self, vectors):
        magic = [0, 0, 0]
        array = []

        for vector in vectors:
            array.append(np.subtract(asarray(vector.start), magic))
            array.append(np.subtract(asarray(vector.end), magic))

        array_np = asarray(array)

        x_min = array_np[:, 0].min()
        y_min = array_np[:, 1].min()
        z_min = array_np[:, 2].min()

        x_max = array_np[:, 0].max()
        y_max = array_np[:, 1].max()

        magic = [(x_max + x_min) / 2, (y_max + y_min) / 2, z_min]

        translate = []

        for vector in vectors:
            translate.append(np.subtract(asarray(vector.start), magic))
            translate.append(np.subtract(asarray(vector.end), magic))

        np_translate = asarray(translate)
        # x axis
        x_min = np_translate[:, 0].min()
        x_max = np_translate[:, 0].max()
        # y axis
        y_min = np_translate[:, 1].min()
        y_max = np_translate[:, 1].max()
        # z axis
        z_min = np_translate[:, 2].min()
        z_max = np_translate[:, 2].max()

        self.centroid = [(x_max + x_min) / 2, (y_max + y_min) / 2, (z_max + z_min) / 2]

        self.array = np_translate

        self.point_max = [x_max, y_max, z_max]
        self.max = max(self.point_max)


class Vector:
    __v_id_gen = it_counts(1)

    def __init__(self, start, end):
        self.v_id = next(self.__v_id_gen)

        if start[2] < end[2]:
            self.start = start
            self.end = end
        else:
            self.start = end
            self.end = start

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

    def correct_z(self):
        if self.start[2] > self.end[2]:
            start = self.start
            end = self.end

            if start[2] < end[2]:
                self.start = start
                self.end = end
            else:
                self.start = end
                self.end = start


class Node:
    n_id_gen = it_counts(1)
    counter = 0
    # conf = {'dx': True, 'dy': True, 'dz': True, 'mx': True, 'my': True, 'mz': True}

    def __init__(self, position):
        self.n_id = str(next(self.n_id_gen))
        self.position = position
        self.n_ve = []
        self.n_springs = []
        self.n_vcn = []


class Element:
    """Propiedades aplicadas para todos los elementos"""
    _SCC = Value(default=20, _max=500, _min=5, text='Número de secciones')
    _poisson = Value(default=0.25, _max=0.3, text='Número de Poisson')

    _e_id_gen = it_counts(1)

    kv = Value(default=0.0, text='Reacción: Vertical')
    kh = Value(default=0.0, text='Reacción: Horizontal')
    wy = Value(default=0.0, text='Eje Y: Carga Uniforme', units='TON/m')
    wz = Value(default=0.0, text='Eje Z: Carga Uniforme')
    aw = Value(default=0.0, text='Carga: Ángulo')
    marco = Value(default='all', text='Marco')

    start_conf: dict = {'dx': True, 'dy': True, 'dz': True, 'mx': True, 'my': True, 'mz': True}
    end_conf: dict = {'dx': True, 'dy': True, 'dz': True, 'mx': True, 'my': True, 'mz': True}

    def __init__(self, vector):
        self.e_id = next(self._e_id_gen)
        # vector debe ser una instancia de la clase Vector, de lo contrario envía ValueError
        self.vector: object = vector

    def _set_type(self, of_type):

        if setattr(self, 'e_type', of_type()):
            self.__dict__.update(of_type.__dict__.keys())
            return False
        else:
            return True


class Concrete:
    """Propiedades específicas del concreto"""

    b = Value(default=0.0, _max=250.0, _min=40.0, text='Zapata: Ancho')
    h = Value(default=0.0, _min=40.0, text='Zapata: Alto')
    b_prima = Value(default=0.0, _min=10.0, text='Contratrabe: Ancho')
    e = Value(default=221.359, text='Elasticidad: Modulo')
    p_mat = Value(default=2.4, text='Material: Peso', units='TON/m')

    def _a1(self):
        return self.b

    def _a2(self):
        return self.h

    def _area(self):
        return self.b_prima.value * self.h.value

    def _izz(self):
        return (self.b_prima.value * self.h.value ** 3) / 12

    def _iyy(self):
        return (self.h.value * self.b_prima.value ** 3) / 12

    def _j(self):
        return ((self.h.value / 2) * (self.b_prima.value / 2) ** 3) * \
               ((16 / 3) - (3.36 * ((self.b_prima.value / 2) / (self.h.value / 2)) *
                            (1 - (self.b_prima.value / 2) ** 4 / (12 * (self.h.value / 2) ** 4))))


class Custom:
    """Tipo de elemento con propiedades personalizadas"""

    b = Value(default=0.0, _min=1.0, text='Sección: Ancho')
    h = Value(default=0.0, _min=1.0, text='Sección: Alto')
    izz = Value(default=0.0, text='Eje X: Inercia')
    iyy = Value(default=0.0, text='Eje Y: Inercia')
    j_ = Value(default=0.0, text='Inercia: Momento Polar')
    e = Value(default=0.0, text='Elasticidad: Modulo')
    p_mat = Value(default=0.0, text='Material: Peso')
    area_ = Value(default=0.0, text='Sección: Área')  # verificar dato

    def _a1(self):
        return self.b.value

    def _a2(self):
        return self.h.value

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

    d = Value(default=0.0, text='Sección: Altura')  # Verificar dato
    bf = Value(default=0.0, text='Sección: Ancho')
    tf = Value(default=0.0, text='Base: Espesor')
    tw = Value(default=0.0, text='Alma: Espesor')
    e = Value(default=0.0, text='Elasticidad: Modulo')
    p_mat = Value(default=7.849, text='Elemento: Peso')

    armour: bool = False    # Añadir opci´n en Value class

    def _a1(self):
        return self.bf.value

    def _a2(self):
        return self.d.value

    def _area(self):
        return (self.d.value * self.bf.value) - \
               ((self.d.value - 2 * self.tf.value) *
                (self.bf.value - 2 * self.tw.value))

    def _izz(self):
        return 2 * ((self.bf.value * self.tf.value ** 3) / 12) + \
               2 * ((self.tw.value * (self.d.value - 2 * self.tf.value) ** 3) / 12) + \
               2 * ((self.bf.value * self.tf.value) * ((self.d.value - self.tf.value) / 2) ** 2)

    def _iyy(self):
        return 2 * ((self.d.value * self.tw.value ** 3) / 12) + \
               2 * ((self.tf.value * (self.bf.value - 2 * self.tw.value) ** 3) / 12) + \
               2 * ((self.d.value * self.tw.value) * ((self.bf.value - self.tw.value) / 2) ** 2)

    def _j(self):
        return (2 * ((self.bf.value - self.tw.value) * (self.d.value - self.tf.value)) ** 2) / \
               (((self.bf.value - self.tw.value) / self.tf.value) + ((self.d.value - self.tf.value) / self.tw.value))


class Ir:
    """Propiedades específicas del tipo IR"""

    d = Value(default=0.0, text='Sección: Peralte')  # Verificar dato
    bf = Value(default=0.0, text='Patín: Ancho')
    tf = Value(default=0.0, text='Patín: Espesor')
    tw = Value(default=0.0, text='Alma: Espesor')
    e = Value(default=0.0, text='Elasticidad: Modulo')
    p_mat = Value(default=7.849, text='Elemento: Peso')

    armour: bool = False

    def _a1(self):
        return self.bf.value

    def _a2(self):
        return self.d.value

    def _area(self):
        return (2 * self.bf.value * self.tf.value) + ((self.d.value - 2 * self.tf.value) * self.tw.value)

    def _izz(self):
        return 2 * ((self.bf.value * (self.tf.value ** 3)) / 12) + \
               (self.tw.value * (self.d.value - (2 * self.tf.value)) ** 3 / 12) + \
               2 * ((self.bf.value * self.tf.value) * ((self.d.value - self.tf.value) / 2) ** 2)

    def _iyy(self):
        return 2 * ((self.tf.value * self.bf.value ** 3) / 12) + \
               (((self.d.value - 2 * self.tf.value) * self.tw.value ** 3) / 12)

    def _j(self):
        return ((2 * self.bf.value * self.tf.value ** 3) + ((self.d.value - self.tf.value) * self.tw.value ** 3)) / 3


class Oc:
    """Propiedades específicas del tipo OC"""
    d = Value(default=0.0, text='Sección: Diametro')
    t = Value(default=0.0, text='Sección: Espesor')
    e = Value(default=0.0, text='Elasticidad: Modulo')
    p_mat = Value(default=7.849, text='Elemento: Peso')

    armour: float = False

    def _a1(self):
        return self.d.value

    def _a2(self):
        return self.d.value

    def _area(self):
        return math.pi * ((self.d.value / 2) ** 2) - (math.pi * ((self.d.value - (2 * self.t.value)) / 2) ** 2)

    def _izz(self):
        return (0.25 * math.pi * (self.d.value / 2) ** 4) - \
               ((0.25 * math.pi) * ((self.d.value - 2 * self.t.value) / 2) ** 4)

    def _iyy(self):
        return self._izz()

    def _j(self):
        return ((math.pi * self.d.value ** 4) / 32) - ((math.pi * (self.d.value - 2 * self.t.value) ** 4) / 32)
