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
elemento1.h = 40
elemento1.b = 40
elemento1.nu = 0
elemento1.b_prima = 40
elemento1.lm = 90
elemento1.kv = 0
elemento1.kh = 0
elemento1.e = 221.359
elemento1.p_mat = 2.4
elemento1.ve = [1,2,3,4,5,6,7,8,9,10,11,12]
elemento1.apoyos = [2,5]


elemento2 = Concreto(node3,node4)
elemento2.h = 40
elemento2.b = 40
elemento2.nu = 0
elemento2.b_prima = 40
elemento2.lm = 0
elemento2.kv = 0
elemento2.kh = 0
elemento2.e = 221.359
elemento2.p_mat = 2.4
elemento2.ve = [7,8,9,10,11,12,13,14,15,16,17,18]
elemento2.apoyos = [0]

elemento3 = Concreto(node5,node6)
elemento3.h = 40
elemento3.b = 40
elemento3.nu = 0
elemento3.b_prima = 40
elemento3.lm = 0
elemento3.kv = 0
elemento3.kh = 0
elemento3.e = 221.359
elemento3.p_mat = 2.4
elemento3.ve = [13,14,15,16,17,18,19,20,21,22,23,24]
elemento3.apoyos = [0]

elemento4 = Concreto(node7,node8)
elemento4.h = 40
elemento4.b = 40
elemento4.nu = 0
elemento4.b_prima = 40
elemento4.lm = 90
elemento4.kv = 0
elemento4.kh = 0
elemento4.e = 221.359
elemento4.p_mat = 2.4
elemento4.ve = [25,26,27,28,29,30,19,20,21,22,23,24]
elemento4.apoyos = [2,5]

elementos = [elemento1, elemento2, elemento3, elemento4]

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

