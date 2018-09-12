from Model.Classes import Concreto
from gc import get_objects

SCC = 20
poisson = 0.25

elemento1 = Concreto()
#elemento1.l = 800
elemento1.h = 5
elemento1.b = 2
elemento1.b_prima = 2
elemento1.kv = 0
elemento1.e = 2000
elemento1.p_mat = 7.849
#elemento1.ve = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
elemento1.wy = 0
elemento1.wz = 0
elemento1.aw = 0
elemento1.nu = 0
elemento1.lm = 0
elemento1.apoyos = [0,0,0,0,0,0,0,0,0,0,0,0]

elemento2 = Concreto()
#elemento1.l = 800
elemento2.h = 5
elemento2.b = 2
elemento2.b_prima = 2
elemento2.kv = 0
elemento2.e = 2000
elemento2.p_mat = 7.849
#elemento1.ve = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
elemento2.wy = 0
elemento2.wz = 0
elemento2.aw = 0
elemento2.nu = 0
elemento2.lm = 0
elemento2.apoyos = [0,0,0,0,0,0,0,0,0,0,0,0]

elemento3 = Concreto()
#elemento1.l = 800
elemento3.h = 5
elemento3.b = 2
elemento3.b_prima = 2
elemento3.kv = 0
elemento3.e = 2000
elemento3.p_mat = 7.849
#elemento1.ve = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
elemento3.wy = 0
elemento3.wz = 0
elemento3.aw = 0
elemento3.nu = 0
elemento3.lm = 90
elemento3.apoyos = [0,0,0,0,0,0,0,0,0,0,0,0]

elemento4 = Concreto()
#elemento1.l = 800
elemento4.h = 5
elemento4.b = 2
elemento4.b_prima = 2
elemento4.kv = 0
elemento4.e = 2000
elemento4.p_mat = 7.849
#elemento1.ve = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
elemento4.wy = 0
elemento4.wz = 0
elemento4.aw = 0
elemento4.nu = 0
elemento4.lm = 39.8
elemento4.apoyos = [0,0,0,0,0,0,0,0,0,0,0,0]

elemento5 = Concreto()
#elemento1.l = 800
elemento5.h = 5
elemento5.b = 2
elemento5.b_prima = 2
elemento5.kv = 0
elemento5.e = 2000
elemento5.p_mat = 7.849
#elemento1.ve = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
elemento5.wy = 0
elemento5.wz = 0
elemento5.aw = 0
elemento5.nu = 180
elemento5.lm = 39.8
elemento5.apoyos = [0,0,0,0,0,0,0,0,0,0,0,0]


elemento1.start_conf['dx'] = False
elemento1.start_conf['dy'] = False
elemento1.start_conf['dz'] = False
elemento1.start_conf['mx'] = False
elemento1.start_conf['my'] = False
elemento1.start_conf['mz'] = False

elemento1.end_conf['my'] = False
elemento1.end_conf['mx'] = False
elemento1.end_conf['mz'] = False

elemento2.end_conf['dy'] = False
elemento2.end_conf['dz'] = False
elemento2.end_conf['mx'] = False
elemento2.end_conf['my'] = False
elemento2.end_conf['mz'] = False

elemento3.end_conf['mx'] = False
elemento3.end_conf['my'] = False
elemento3.end_conf['mz'] = False

elemento1.armadura = True
elemento2.armadura = True
elemento3.armadura = True
elemento4.armadura = True
elemento5.armadura = True

elemento1.start = (0,0,0)
elemento1.end = (300,0,0)
elemento2.start = (300,0,0)
elemento2.end = (600,0,0)
elemento3.start = (300,0,0)
elemento3.end = (300,250,0)
elemento4.start = (0,0,0)
elemento4.end = (300,250,0)
elemento5.start = (600,0,0)
elemento5.end = (300,250,0)

v_c_n = [0,0,0,0,-4,-6.9282,0]

lista = []
#
for element in get_objects():
    if isinstance(element, Concreto):
        element.set_nodes()
        lista.append(element)
