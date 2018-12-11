from pyqtgraph.Qt import QtGui
import pyqtgraph.opengl as gl
from read_dxf import read_dxf
import pyqtgraph as pg
# from PyQt5.QtWidgets import QFileDialog as qfd
# from Model.classes.element_types import Geometry
from numpy import asarray

app = QtGui.QApplication([])
pg.setConfigOption('leftButtonPan', True)
pg.setConfigOption('useOpenGL', True)
w = gl.GLViewWidget()
w.setBackgroundColor(0.15)
w.show()

w.setWindowTitle('Strucpy v0.1 [BETA]')

# read = qfd.getOpenFileName(w, "Open DXF", "c:\\", "dfx files (*.dxf)")
# vectors = read_dxf(read[0])
vectors = read_dxf('c:/repos/strucpy/dev_files/dxf/irregular.dxf')
# geometry = Geometry(vectors)
w.opts['distance'] = vectors[3] * 3
# w.opts['center'] = QtGui.QVector3D(geometry.centroid[0],
#                                    geometry.centroid[1],
#                                    geometry.centroid[2])
# w.opts['viewport'] = (200, 300)
# w.pan(0,0,0)
# w.setCameraPosition(pos=(10000,10,1000), distance=1000, elevation=10, azimuth=100)
plt = gl.GLLinePlotItem(pos=asarray(vectors[0]),
                        mode='lines',
                        antialias=True,
                        color=[0.4, 0.2, 0.3, 0.9],
                        width=1)
w.addItem(plt)

plt2 = gl.GLLinePlotItem(pos=asarray(vectors[2]),
                        mode='lines',
                        antialias=True,
                        color=[0.4, 0.2, 2.3, 0.9],
                        width=1)
w.addItem(plt2)

ground = gl.GLGridItem(antialias=True, glOptions='translucent', color=[255, 255, 255, 0.1])
ground.setSize(x=10000, y=10000)
ground.setSpacing(x=1000, y=1000)
# w.addItem(ground)

axis_long = vectors[3] / 10
axis_x = gl.GLLinePlotItem(
    pos=asarray([(0, 0, 0), (axis_long, 0, 0)]),
    mode='lines',
    antialias=True,
    color=[1.0, 0.0, 0.0, 0.7])
w.addItem(axis_x)

axis_y = gl.GLLinePlotItem(
    pos=asarray([(0, 0, 0), (0, axis_long, 0)]),
    mode='lines',
    antialias=True,
    color=[0.0, 1.0, 0.0, 0.7])
w.addItem(axis_y)

axis_z = gl.GLLinePlotItem(
    pos=asarray([(0, 0, 0), (0, 0, axis_long)]),
    mode='lines',
    antialias=True,
    color=[0.0, 0.0, 1.0, 0.7])
w.addItem(axis_z)

axis_nx = gl.GLLinePlotItem(
    pos=asarray([(0, 0, 0), (-axis_long, 0, 0)]),
    mode='lines',
    antialias=True,
    color=[1.0, 0.2, 0.6, 0.7])
w.addItem(axis_nx)

axis_ny = gl.GLLinePlotItem(
    pos=asarray([(0, 0, 0), (0, -axis_long, 0)]),
    mode='lines',
    antialias=True,
    color=[1.0, 1.0, 0.0, 0.7])
w.addItem(axis_ny)

axis_nz = gl.GLLinePlotItem(
    pos=asarray([(0, 0, 0), (0, 0, -axis_long)]),
    mode='lines',
    antialias=True,
    color=[0.2, 1.0, 1.0, 0.7])
w.addItem(axis_nz)

centre = gl.GLVolumeItem(data=[(0,0,0),(0,0,1)])

# select = gl.GLLinePlotItem(pos=geometry.array[:1001],
#                            mode='lines',
#                            antialias=True,
#                            width=7,
#                            color=[0, 255, 0, 0.7])
# w.addItem(select)

app.exec_()
