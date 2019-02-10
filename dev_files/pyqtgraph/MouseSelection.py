# -*- coding: utf-8 -*-
"""
Demonstrates selecting plot curves by mouse click
"""
# import initExample ## Add path to library (just for examples; you do not need this)
import dxfgrabber as dxfg
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


def read_dxf(file):
    convention_switch_array = []
    # vector_objects = []
    array_dxf = [[line.start, line.end] for line in dxfg.readfile(file).entities._entities if isinstance(line, dxfg.dxfentities.Line)]
    for line in array_dxf:
        start = (line[0][0], line[0][2], -line[0][1])
        end = (line[1][0], line[1][2], -line[1][1])
        convention_switch_array += [start, end]
        # vector_objects.append(Vector(start, end))

    max_point_convention = max(convention_switch_array)
    min_point_convention = min(convention_switch_array)

    return convention_switch_array, max_point_convention, min_point_convention


vectors = read_dxf('c:/repos/strucpy/dev_files/all_vectors/irregular.all_vectors')
normal = vectors[0]


def orthogonal_projection(point):
    convert_matrix = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 1]])
    ort = convert_matrix.dot(point)
    return ort[0], ort[2]


# list_pro = list(map(orthogonal_projection, normal))

# list_pairs = [[list_pro[n], list_pro[n+1]] for n, x in enumerate(list_pro) if n % 2 == 0 or n == 0]
# list_x = [[list_pro[n][0], list_pro[n+1][0]] for n, x in enumerate(list_pro) if n % 2 == 0 or n == 0]
# list_x = [x[0] for x in list_pro]
# list_y = [[list_pro[n][1], list_pro[n+1][1]] for n, x in enumerate(list_pro) if n % 2 == 0 or n == 0]
# list_y = [y[1] for y in list_pro]
# pair_lists_end = list(zip(list_x, list_y))
# print(list_pairs)

win = pg.plot()
win.setWindowTitle('pyqtgraph example: Plot data selection')
# curves = []

# for n, line in enumerate(list_pairs):
#     if n % 2 == 0 or n == 0:
#         curves.append(pg.PlotCurveItem(x=np.asarray([list_pairs[n][0], list_pairs[n+1][0]]),
#                                        y=np.asarray([list_pairs[n][1], list_pairs[n+1][1]]),
#                                        pen='r',
#                                        clickable=True))

# win.setAspectLocked(True)
# win.addItem(pg.PlotCurveItem(x=np.asarray(list_x), y=np.asarray(list_y), clickable=True, pen='r'))


curves = [
    pg.PlotCurveItem(y=np.sin(np.linspace(0, 20, 1000)), pen='r', clickable=True),
    pg.PlotCurveItem(y=np.sin(np.linspace(1, 21, 1000)), pen='g', clickable=True),
    pg.PlotCurveItem(y=np.sin(np.linspace(2, 22, 1000)), pen='b', clickable=True),
    ]


def plotClicked(curve):
    global curves
    for c in curves:
        if c is curve:
            c.setPen('g', width=5)
        else:
            c.setPen('r', width=1)


for c in curves:
    win.addItem(c)
    c.sigClicked.connect(plotClicked)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
