from Model.Classes import *
from gc import get_objects

SCC = 20
poisson = 0.25

elemento1 = Concreto()
elemento1.l = 400
elemento1.h = 40
elemento1.b = 40
elemento1.b_prima = 40
elemento1.kv = 0
elemento1.e = 221.359
elemento1.p_mat = 2.4
elemento1.ve = [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6]
elemento1.wy = 0
elemento1.aw = 0
elemento1.nu = 0
elemento1.lm = 90

elemento2 = Concreto()
elemento2.l = 400
elemento2.h = 40
elemento2.b = 40
elemento2.nu = 0
elemento2.b_prima = 40
elemento2.lm = 90
elemento2.kv = 0
elemento2.kh = 0
elemento2.e = 221.359
elemento2.p_mat = 2.4
elemento2.ve = [0, 0, 0, 0, 0, 0, 7, 8, 9, 10, 11, 12]
elemento2.apoyos = [0]

elemento3 = Concreto()
elemento3.l = 300
elemento3.h = 40
elemento3.b = 40
elemento3.nu = 90
elemento3.b_prima = 40
elemento3.lm = 0
elemento3.kv = 0
elemento3.kh = 0
elemento3.e = 221.359
elemento3.p_mat = 2.4
elemento3.ve = [7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6]
elemento3.apoyos = [0]

elemento4 = Concreto()
elemento4.l = 781.02
elemento4.h = 40
elemento4.b = 40
elemento4.b_prima = 40
elemento4.kv = 0
elemento4.e = 221.359
elemento4.p_mat = 2.4
elemento4.ve = [0, 0, 0, 0, 0, 0, 7, 8, 9, 10, 11, 12]
elemento4.wy = 8
elemento4.aw = 30.80
elemento4.nu = -26.565
elemento4.lm = 30.8

v_c_n = [0,0,0,0,0,0,0,0,0,0,0,0]

lista = []
#
for element in get_objects():
    if isinstance(element, Concreto):
        lista.append(element)
