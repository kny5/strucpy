from Model.Classes import *
from gc import get_objects

SCC = 10
poisson = 0.25

elemento1 = Or()
elemento1.l = 800
elemento1.h = 40
elemento1.b = 40
elemento1.b_prima = 40
elemento1.kv = 0
elemento1.e = 221.359
elemento1.p_mat = 2.4
elemento1.ve = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
elemento1.wy = 0
elemento1.wz = 0
elemento1.aw = 0
elemento1.nu = 0
elemento1.lm = 90
elemento1.apoyos = [1,3,2,100,100,100,4,6,5,100,100,100]

elemento1.armadura = False

v_c_n = [20,0,-50,0,0,0,0,-10,0,0,0,0]

lista = []
#
for element in get_objects():
    if isinstance(element, Or):
        lista.append(element)
