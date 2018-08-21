from Model.Classes import *
from gc import get_objects

elemento1 = Concreto()
elemento1.l = 900
elemento1.h = 120
elemento1.b = 150
elemento1.b_prima = 40
elemento1.kv = 2
elemento1.e = 221.359
elemento1.p_mat = 2.4
elemento1.ve = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

elemento2 = Concreto()
elemento2.l = 900
elemento2.h = 120
elemento2.b = 150
elemento2.nu = 0
elemento2.b_prima = 40
elemento2.lm = 0
elemento2.kv = 2
elemento2.kh = 0
elemento2.e = 221.359
elemento2.p_mat = 2.4
elemento2.ve = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
elemento2.apoyos = [0]

elemento3 = Concreto()
elemento3.l = 300
elemento3.h = 120
elemento3.b = 150
elemento3.nu = 90
elemento3.b_prima = 40
elemento3.lm = 0
elemento3.kv = 2
elemento3.kh = 0
elemento3.e = 221.359
elemento3.p_mat = 2.4
elemento3.ve = [13, 14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6]
elemento3.apoyos = [0]

elemento4 = Concreto()
elemento4.l = 300
elemento4.h = 120
elemento4.b = 150
elemento4.nu = 90
elemento4.b_prima = 40
elemento4.lm = 0
elemento4.kv = 2
elemento4.kh = 0
elemento4.e = 221.359
elemento4.p_mat = 2.4
elemento4.ve = [19, 20, 21, 22, 23, 24, 7, 8, 9, 10, 11, 12]
elemento4.apoyos = [0]

elemento5 = Concreto()
elemento5.l = 500
elemento5.h = 40
elemento5.b = 40
elemento5.nu = 0
elemento5.b_prima = 40
elemento5.lm = 90
elemento5.kv = 0
elemento5.kh = 0
elemento5.e = 221.359
elemento5.p_mat = 2.4
elemento5.ve = [1, 2, 3, 4, 5, 6, 37, 38, 39, 40, 41, 42]
elemento5.apoyos = [0]

elemento6 = Concreto()
elemento6.l = 500
elemento6.h = 40
elemento6.b = 40
elemento6.nu = 0
elemento6.b_prima = 40
elemento6.lm = 90
elemento6.kv = 0
elemento6.kh = 0
elemento6.e = 221.359
elemento6.p_mat = 2.4
elemento6.ve = [7, 8, 9, 10, 11, 12, 43, 44, 45, 46, 47, 48]
elemento6.apoyos = [0]

elemento7 = Concreto()
elemento7.l = 500
elemento7.h = 40
elemento7.b = 40
elemento7.nu = 0
elemento7.b_prima = 40
elemento7.lm = 90
elemento7.kv = 0
elemento7.kh = 0
elemento7.e = 221.359
elemento7.p_mat = 2.4
elemento7.ve = [13, 14, 15, 16, 17, 18, 25, 26, 27, 28, 29, 30]
elemento7.apoyos = [0]

elemento8 = Concreto()
elemento8.l = 500
elemento8.h = 40
elemento8.b = 40
elemento8.nu = 0
elemento8.b_prima = 40
elemento8.lm = 90
elemento8.kv = 0
elemento8.kh = 0
elemento8.e = 221.359
elemento8.p_mat = 2.4
elemento8.ve = [19, 20, 21, 22, 23, 24, 31, 32, 33, 34, 35, 36]
elemento8.apoyos = [0]

elemento9 = Concreto()
elemento9.l = 900
elemento9.h = 40
elemento9.b = 40
elemento9.nu = 0
elemento9.b_prima = 40
elemento9.lm = 0
elemento9.kv = 0
elemento9.kh = 0
elemento9.e = 221.359
elemento9.p_mat = 2.4
elemento9.ve = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
elemento9.apoyos = [0]

elemento10 = Concreto()
elemento10.l = 900
elemento10.h = 40
elemento10.b = 40
elemento10.nu = 0
elemento10.b_prima = 40
elemento10.lm = 0
elemento10.kv = 0
elemento10.kh = 0
elemento10.e = 221.359
elemento10.p_mat = 2.4
elemento10.ve = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
elemento10.apoyos = [0]

elemento11 = Concreto()
elemento11.l = 300
elemento11.h = 40
elemento11.b = 40
elemento11.nu = 90
elemento11.b_prima = 40
elemento11.lm = 0
elemento11.kv = 0
elemento11.kh = 0
elemento11.e = 221.359
elemento11.p_mat = 2.4
elemento11.ve = [25, 26, 27, 28, 29, 30, 37, 38, 39, 40, 41, 42]
elemento11.apoyos = [0]

elemento12 = Concreto()
elemento12.l = 300
elemento12.h = 40
elemento12.b = 40
elemento12.nu = 90
elemento12.b_prima = 40
elemento12.lm = 0
elemento12.kv = 0
elemento12.kh = 0
elemento12.e = 221.359
elemento12.p_mat = 2.4
elemento12.ve = [31, 32, 33, 34, 35, 36, 43, 44, 45, 46, 47, 48]
elemento12.apoyos = [0]

lista = []
#
for element in get_objects():
    if isinstance(element, Concreto):
        lista.append(element)