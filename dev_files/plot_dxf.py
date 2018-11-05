from pyqtgraph.Qt import QtGui
import pyqtgraph.opengl as gl
from Model.functions.read_dxf import read_dxf
import pyqtgraph as pg
from PyQt5.QtWidgets import QFileDialog as qfd
from Model.classes.element_types import Geometry

app = QtGui.QApplication([])
pg.setConfigOption('leftButtonPan', True)
pg.setConfigOption('useOpenGL', True)
w = gl.GLViewWidget()
w.setBackgroundColor(0.15)
w.show()

w.setWindowTitle('Strucpy v0.1 [BETA]')

# read = qfd.getOpenFileName(w, "Open DXF", "c:\\", "dfx files (*.dxf)")
# vectors = read_dxf(read[0])
vectors = read_dxf('lienzo.dxf')

geometry = Geometry(vectors)
w.opts['distance'] = geometry.max * 2.25
# w.opts['center'] = QtGui.QVector3D(geometry.centroid[0],
#                                   geometry.centroid[1],
#                                   geometry.centroid[2])

plt = gl.GLLinePlotItem(pos=geometry.array,
                        mode='lines',
                        antialias=True,
                        color=[0.4, 0.2, 2.3, 0.9],
                        width=1)
w.addItem(plt)

ground = gl.GLGridItem(antialias=True, glOptions='translucent', color=[255, 255, 255, 0.1])
ground.setSize(x=geometry.max * 2.1, y=geometry.max * 2.1)
ground.setSpacing(x=100, y=100)
# w.addItem(ground)

select = gl.GLLinePlotItem(pos=geometry.array[:1001],
                           mode='lines',
                           antialias=True,
                           width=7,
                           color=[0, 255, 0, 0.7])
w.addItem(select)

selct_area = w.itemsAt(region=[100, 100, 10, 10])

app.exec_()
