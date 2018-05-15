""" archivo para pruebas """
from pandas import DataFrame as df
from dataClasses import *
x = Concreto()
x.long = 500
x.b_prima = 50
x.b = 120
x.h = 80
x.kv = 1.2
x.e = 221.359

print(df(x.KEBG()))
