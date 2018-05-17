""" archivo para pruebas """
from pandas import DataFrame as df
from dataClasses import *
x = Concreto()
x.l = 1200
x.b_prima = 40
x.b = 100
x.h = 80
x.nu = 30
x.lm = 70
x.kv = 2
x.kh = 5
x.wy = 8
x.aw = 70
x.wz = 5
x.e = 221.359

print(df(x.KEBG()))
