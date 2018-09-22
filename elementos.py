from Model.Classes import Concreto

#import jsonpickle

elemento1 = Concreto()
elemento1.h = 5
elemento1.b = 2
elemento1.b_prima = 2
elemento1.kv = 0
elemento1.e = 2000
elemento1.p_mat = 7.849
elemento1.wy = 0
elemento1.wz = 0
elemento1.aw = 0

elemento2 = Concreto()
elemento2.h = 5
elemento2.b = 2
elemento2.b_prima = 2
elemento2.kv = 0
elemento2.e = 2000
elemento2.p_mat = 7.849
elemento2.wy = 0
elemento2.wz = 0
elemento2.aw = 0

elemento3 = Concreto()
elemento3.h = 5
elemento3.b = 2
elemento3.b_prima = 2
elemento3.kv = 0
elemento3.e = 2000
elemento3.p_mat = 7.849
elemento3.wy = 0
elemento3.wz = 0
elemento3.aw = 0

elemento4 = Concreto()
elemento4.h = 5
elemento4.b = 2
elemento4.b_prima = 2
elemento4.kv = 0
elemento4.e = 2000
elemento4.p_mat = 7.849
elemento4.wy = 0
elemento4.wz = 0
elemento4.aw = 0

elemento5 = Concreto()
elemento5.h = 5
elemento5.b = 2
elemento5.b_prima = 2
elemento5.kv = 0
elemento5.e = 2000
elemento5.p_mat = 7.849
elemento5.wy = 0
elemento5.wz = 0
elemento5.aw = 0

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
elemento3.end_conf['mz'] = (1,2)

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

#json_object = jsonpickle.encode(elemento1)

#print(json_object)

#with open("_input.json", 'w') as f:
#    f.write(str(json_object))