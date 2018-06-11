""" archivo para pruebas """
from Model.dataClasses import *
from Model.k_p import calculations as calc
from pandas import DataFrame as df
from Model.kest import *

workspace = workspace(100, 100, 100)

node1 = Nodo(20,30,14, workspace)
node2 = Nodo(67,56,34, workspace)

node3 = Nodo(60,70,54, workspace)
node4 = Nodo(89,12,44, workspace)

node5 = Nodo(45,23,4, workspace)
node6 = Nodo(6,5,4, workspace)

node7 = Nodo(46,42,23, workspace)
node8 = Nodo(89,87,78, workspace)


elemento1 = Concreto(node1,node2)
elemento1.l = 500
elemento1.h = 40
elemento1.b = 40
elemento1.nu = 0
elemento1.b_prima = 40
elemento1.lm = 90
elemento1.kv = 0
elemento1.kh = 0
elemento1.e = 221.359
elemento1.p_mat = 2.4
elemento1.ve = [0,0,0,0,0,0,1,2,3,4,5,6]
elemento1.apoyos = [0,0]


elemento2 = Concreto(node3,node4)
elemento2.l = 500
elemento2.h = 40
elemento2.b = 40
elemento2.nu = 0
elemento2.b_prima = 40
elemento2.lm = 90
elemento2.kv = 0
elemento2.kh = 0
elemento2.e = 221.359
elemento2.p_mat = 2.4
elemento2.ve = [0,0,0,0,0,0,7,8,9,10,11,12]
elemento2.apoyos = [0]

elemento3 = Concreto(node5,node6)
elemento3.l = 500
elemento3.h = 40
elemento3.b = 40
elemento3.nu = 0
elemento3.b_prima = 40
elemento3.lm = 90
elemento3.kv = 0
elemento3.kh = 0
elemento3.e = 221.359
elemento3.p_mat = 2.4
elemento3.ve = [0,0,0,0,0,0,13,14,15,16,17,18]
elemento3.apoyos = [0]

elemento4 = Concreto(node7,node8)
elemento4.l = 500
elemento4.h = 40
elemento4.b = 40
elemento4.nu = 0
elemento4.b_prima = 40
elemento4.lm = 90
elemento4.kv = 0
elemento4.kh = 0
elemento4.e = 221.359
elemento4.p_mat = 2.4
elemento4.ve = [0,0,0,0,0,0,19,20,21,22,23,24]
elemento4.apoyos = [0]

elemento5 = Concreto(node7,node8)
elemento5.l = 900
elemento5.h = 40
elemento5.b = 40
elemento5.nu = 0
elemento5.b_prima = 40
elemento5.lm = 0
elemento5.kv = 0
elemento5.kh = 0
elemento5.e = 221.359
elemento5.p_mat = 2.4
elemento5.ve = [1,2,3,4,5,6,7,8,9,10,11,12]
elemento5.apoyos = [0]

elemento6 = Concreto(node7,node8)
elemento6.l = 900
elemento6.h = 40
elemento6.b = 40
elemento6.nu = 0
elemento6.b_prima = 40
elemento6.lm = 0
elemento6.kv = 0
elemento6.kh = 0
elemento6.e = 221.359
elemento6.p_mat = 2.4
elemento6.ve = [13,14,15,16,17,18,19,20,21,22,23,24]
elemento6.apoyos = [0]

elemento7 = Concreto(node7,node8)
elemento7.l = 300
elemento7.h = 40
elemento7.b = 40
elemento7.nu = 90
elemento7.b_prima = 40
elemento7.lm = 0
elemento7.kv = 0
elemento7.kh = 0
elemento7.e = 221.359
elemento7.p_mat = 2.4
elemento7.ve = [13,14,15,16,17,18,1,2,3,4,5,6]
elemento7.apoyos = [0]

elemento8 = Concreto(node7,node8)
elemento8.l = 300
elemento8.h = 40
elemento8.b = 40
elemento8.nu = 90
elemento8.b_prima = 40
elemento8.lm = 0
elemento8.kv = 0
elemento8.kh = 0
elemento8.e = 221.359
elemento8.p_mat = 2.4
elemento8.ve = [19,20,21,22,23,24,7,8,9,10,11,12]
elemento8.apoyos = [0]

elementos = [elemento1, elemento2, elemento3, elemento4, elemento5, elemento6, elemento7, elemento8]

#i = 0
for array in elementos:
    #with open(str(i) + '_data.txt', 'w') as outfile:
    #    json.dump(array.__dict__, outfile)
    x = calc(array, 20, 0.25)
    #x = calc(array, 20, 0.25)
    #print(df(x))
    #x.to_csv(str(i) + "_output.csv")
    #i += 1



est_init = est_init(elementos)

kest = kest_maker(elementos, est_init["kest"])
pcur = pcur_maker(elementos, est_init["pcur"])

print("done.")

df(kest).to_csv("kest.csv")
df(pcur).to_csv("pcur.csv")

