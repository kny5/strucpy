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
elemento3.l = 400
elemento3.h = 40
elemento3.b = 40
elemento3.nu = 0
elemento3.b_prima = 40
elemento3.lm = 90
elemento3.kv = 0
elemento3.kh = 0
elemento3.e = 221.359
elemento3.p_mat = 2.4
elemento3.ve = [0, 0, 0, 0, 0, 0, 13, 14, 15, 16, 17, 18]
elemento3.apoyos = [0]

elemento4 = Concreto()
elemento4.l = 400
elemento4.h = 40
elemento4.b = 40
elemento4.b_prima = 40
elemento4.kv = 0
elemento4.e = 221.359
elemento4.p_mat = 2.4
elemento4.ve = [0, 0, 0, 0, 0, 0, 19, 20, 21, 22, 23, 24]
elemento4.wy = 0
elemento4.aw = 0
elemento4.nu = 0
elemento4.lm = 90

elemento5 = Concreto()
elemento5.l = 600
elemento5.h = 40
elemento5.b = 40
elemento5.b_prima = 40
elemento5.kv = 0
elemento5.e = 221.359
elemento5.p_mat = 2.4
elemento5.ve = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
elemento5.wy = 0
elemento5.aw = 0
elemento5.nu = 0
elemento5.lm = 0

elemento6 = Concreto()
elemento6.l = 600
elemento6.h = 40
elemento6.b = 40
elemento6.b_prima = 40
elemento6.kv = 0
elemento6.e = 221.359
elemento6.p_mat = 2.4
elemento6.ve = [13,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
elemento6.wy = 0
elemento6.aw = 0
elemento6.nu = 0
elemento6.lm = 0

elemento7 = Concreto()
elemento7.l = 300
elemento7.h = 40
elemento7.b = 40
elemento7.b_prima = 40
elemento7.kv = 0
elemento7.e = 221.359
elemento7.p_mat = 2.4
elemento7.ve = [13,14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6]
elemento7.wy = 0
elemento7.aw = 0
elemento7.nu = 90
elemento7.lm = 0

elemento8 = Concreto()
elemento8.l = 300
elemento8.h = 40
elemento8.b = 40
elemento8.b_prima = 40
elemento8.kv = 0
elemento8.e = 221.359
elemento8.p_mat = 2.4
elemento8.ve = [19,20, 21, 22, 23, 24, 7, 8, 9, 10, 11, 12]
elemento8.wy = 0
elemento8.aw = 0
elemento8.nu = 90
elemento8.lm = 0

elemento9 = Concreto()
elemento9.l = 781.02
elemento9.h = 40
elemento9.b = 40
elemento9.b_prima = 40
elemento9.kv = 0
elemento9.e = 221.359
elemento9.p_mat = 2.4
elemento9.ve = [0,0, 0, 0, 0, 0, 19, 20, 21, 22, 23, 24]
elemento9.wy = 8
elemento9.aw = 30.8
elemento9.nu = -26.565
elemento9.lm = 30.8

v_c_n = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

lista = []
#
for element in get_objects():
    if isinstance(element, Concreto):
        lista.append(element)
