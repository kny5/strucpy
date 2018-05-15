#import json
#import pyqt5
import math
from kebg import kebg
"""
Catalogo de clases
"""
SCC = 20
POISSON = 0.25
SIGMA_SUELO = 0

class Elemento:
    """Propiedades generales de elemento"""
    def __init__(self):
        self.long = 0   #longitud del elemento
        self.v_ens = [0,0,0,0,0,0,0,0,0,0,0,0]  #vector de ensamble
        self.nu = 0     #ángulo plano xz
        self.lamb = 0   #ángulo plano xy
        self.kv = 0     #módulo de reacción vertical
        self.kh = 0     #módulo de reacción horizontal

    def dx(self):
        x = self.long / SCC
        return x

    def mzz(self):
        x = (self.e * self.izz()) / self.dx() ** 2
        return x

    def myy(self):
        x = (self.e * self.iyy()) / self.dx() ** 2
        return x

    def vzz(self):
        x = (self.e * self.izz()) / (2 * self.dx() ** 3)
        return x

    def vyy(self):
        x = (self.e * self.iyy()) / (2 * self.dx() ** 3)
        return x

    #def A(self):
    #    x = (self.kv *  self.a1() * self.dx() ** 4) / (1000 * self.e * self.izz())
    #    return x

    #def B(self):
    #    x = (self.kh * self.a2() * self.dx() ** 4) / (1000 * self.e * self.iyy())
    #    return x

    def G(self):
        x = self.e / (2 * (1 + POISSON))
        return x

    def torsion(self):
        x = (self.G() * self.j()) / self.long
        return x

    def axial(self):
        x = (self.e * self.area()) / self.long
        return x

    def KEBG(self):
        x = kebg(self.A(), self.B(), SCC, self.dx(), POISSON, self.nu, self.lamb, \
            self.mzz(), self.myy(), self.vzz(), self.vyy(), self.axial(), self.torsion())
        return x


class Concreto(Elemento):
    """Propiedades específicas del concreto"""
    def __init__(self):
        Elemento.__init__(self)
        self.b = 0              #ancho de zapata
        self.h = 0              #altura de zapata
        self.b_prima = 0        #ancho de Contratrabe
        self.e = 0              #modulo de elasticidad
        self.p_mat = 2.4       #ton/m3

    def A(self):
        x = (self.kv * self.b * self.dx() ** 4) / (1000 * self.e * self.izz())
        return x

    def B(self):
        x = (self.kh * self.h * self.dx() ** 4) / (1000 * self.e * self.iyy())
        return x

    #def a1(self):
    #    return self.b

    #def a2(self):
    #    return self.h

    def area(self):
        x = self.b_prima * self.h
        return x

    def peso_p(self):
        x = (self.area * self.p_conc / 10000) * (self.long / SCC)
        return x

    def izz(self):
        x = (self.b_prima * self.h ** 3) / 12
        return x

    def iyy(self):
        x = (self.h * self.b_prima ** 3) / 12
        return x

    def j(self):
        x = ((self.h / 2) * (self.b_prima / 2) ** 3) * \
            ((16/3) - (3.36 * ((self.b_prima / 2) / (self.h / 2)) * \
            (1 - (self.b_prima / 2) ** 4 / (12 * (self.h / 2) ** 4))))
        return x

class Especial(Elemento):
    def __init__(self):
        Elemento.__init__(self)
        self.b = 0      #ancho de la sección
        self.h = 0      #altura de la sección
        self.ixx = 0    #inercia del eje x
        self.iyy = 0    #inercia del eje y
        self.j = 0     #momento polar de inercia
        self.e = 0      #modulo de elasticidad
        self.peso_p = 0     #peso propio
        self.a1 =  self.b
        self.a2 = self.h
        self.area = 0

class Acero(Elemento):
    def __init__(self):
        Elemento.__init__(self)
        self.e = 0
        self.p_mat = 7.849

    def peso_p(self):
        x = self.area() * (self.p_acero / 10000) * (self.long / SCC)
        return x

class Or(Acero):
    """Propiedades específicas del tipo OR"""
    def __init__(self):
        Acero.__init__(self)
        self.d = 0
        self.bf = 0
        self.tf = 0
        self.tw = 0
        self.a1 = self.bf
        self.a2 = self.d

    def area(self):
        x = (self.d * self.bf) - ((self.d - 2 * self.tf) * (self.bf -2 * self.tw))
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
        x = (2 * ((self.bf - self.tw) * (self.d -self.tf)) ** 2) / \
            (((self.bf - self.tw) / self.tf) + ((self.d -self.tf) / self.tw))
        return x

class Ir(Acero):
    """Propiedades específicas del tipo IR"""
    def __init__(self):
        Acero.__init__(self)
        self.d = 0
        self.bf = 0
        self.tf = 0
        self.tw = 0
        self.a1 = self.bf
        self.a2 = self.d

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
    def __init__(self):
        Acero.__init__(self)
        self.d = 0
        self.t = 0
        self.a1 = self.d
        self.a2 = self.d

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