""" archivo para pruebas """
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Strucpy') + '[MDF]\t[v0.1]\t[2018]' + '\n')
print('importing modules')
from dev_files.kest import vdgen
print('Creando elementos')

vdgen()

print("\n[Programa finalizado]\n")

