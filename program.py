""" archivo para pruebas """
from pandas import DataFrame as df
from dataClasses import *
from matrix_generator import kebg_pcur
import copy as cp
import numpy as np

def builder(cls, cantidad):
    y = {}
    z = cls
    for x in range(cantidad):
        y[x] = cp.deepcopy(z)
    return y

def maths(dict):
    x = {}
    for key in dict:
        x[key] = kebg_pcur(dict[key])
        dict[key].KEBG = x[key]['KEBG']
        dict[key].PCUR = x[key]['PCUR']
    return

elementos = builder(Concreto(), 2)

elementos[0].__dict__ = {\
'l': 700,\
'h': 100,\
'b': 200,\
'nu': 0,\
'b_prima': 40,\
'lm': 0,\
'kv': 5,\
'kh': 0,\
'wy': 8,\
'aw': 0,\
'wz': 0,\
'e': 221.359,\
'p_mat': 2.4,\
've': np.matrix('0 2 300 23 5 8 0 9 12 7 0 4')
}

elementos[1].__dict__ = {\
'l': 700,\
'h': 100,\
'b': 200,\
'nu': 0,\
'b_prima': 40,\
'lm': 0,\
'kv': 5,\
'kh': 0,\
'wy': 8,\
'aw': 0,\
'wz': 0,\
'e': 221.359,\
'p_mat': 2.4,\
}

maths(elementos)




