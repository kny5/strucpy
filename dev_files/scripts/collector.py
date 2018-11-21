#from Classes import Concreto
import jsonpickle
import sys
try:
    print(str(sys.argv[1]))
    with open(str(sys.argv[1]), 'r') as inputFile:
        read_input = jsonpickle.loads(inputFile.read())

except IndexError:
    with open('input.json', 'r') as inputFile:
        read_input = jsonpickle.loads(inputFile.read())

try:
    read_input.set_nodes
    read_input.calculations()

#except AttributeError:
    #read_input.id = 1
except TypeError:
    print(read_input)
print(read_input.ve)
