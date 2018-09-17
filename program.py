""" archivo para pruebas """
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Strucpy') + '[MDF]\t[v0.1]\t[2018]' + '\n')
print('importing modules')
from Model.kest import vdgen
print('Creando elementos')

import elementos

vdgen()

print("\n[Programa finalizado]\n")

