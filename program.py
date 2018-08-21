""" archivo para pruebas """
from Model.k_p import calculations as calc
from Model.kest import vdgen
import pandas as pd
from openpyxl import load_workbook
import os
import datetime
import elementos
from shutil import copyfile
import sys
from pandas import DataFrame as df

elementos = elementos.lista
#
calc(elementos)
#
print('k_p.py done')
#

#
print("done.")

if not os.path.exists("proyectos"):
    os.mkdir("proyectos")

#if not sys.argv[1]:
#    print("\n" + "Proyectos existentes:" + "\n")
#    print(os.listdir("proyectos"))
#    print("\n## Puede escribir cualquiera de los nombres listados o crear uno nuevo.")

#    proyecto = input("\n" + "! " + "Nombre del proyecto: ")
#else:

proyecto = sys.argv[1]

path_pro = "proyectos/" + str(proyecto) + "/"

if not os.path.exists(path_pro):
    os.mkdir(path_pro)

#if not sys.argv[2]:
#    version = path_pro + str(datetime.datetime.now())
#else:
version = path_pro + sys.argv[2]

os.mkdir(version)

vdgen(elementos)
#
print("\nCreando archivos de excel:")

for k, elemento in enumerate(elementos, 1):

    print(("#"*k) + " " + str(k))

    w_name = str(k) + "_elemento.xlsx"
    completeName = os.path.join(version, w_name)

    w_elem = pd.ExcelWriter(completeName)
    for att, value in elemento.__dict__.items():
        if type(value) != float and type(value) != list and type(value) != int and type(value) != str:
            x_ = value.tolist()
            df(x_).to_excel(w_elem, str(att))
    w_elem.save()

    data_ = load_workbook(completeName)
    wb3 = data_.create_sheet('datos', 0)
    count_e = 1
    for att, value in elemento.__dict__.items():
        if type(value) == float or type(value) == int or type(value) == str or type(value) == list:

          wb3.cell(count_e, 1, value=str(att))
          wb3.cell(count_e, 2, value=str(value))
          count_e += 1

    data_.save(completeName)
    percent = round(100 / len(elementos), 0)

copyfile("elementos.py", os.path.join(version, "elementos.py"))
print("Programa finalizado.")
