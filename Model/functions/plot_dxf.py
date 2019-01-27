# from pyqtgraph.Qt import QtGui
from PyQt5 import QtGui
import pyqtgraph.opengl as gl
from read_dxf import read_dxf
import pyqtgraph as pg
# from PyQt5.QtWidgets import QFileDialog as qfd
from numpy import asarray
import numpy as np
import time
import math


start = time.time()
vectors = read_dxf('c:/repos/strucpy/dev_files/dxf/lienzo.dxf')
normal = vectors[0]


def projection(point, alpha=35, beta=45):
    calpha = math.cos(alpha)
    salpha = math.sin(alpha)
    cbeta = math.cos(beta)
    sbeta = math.sin(beta)

    _tranform_a = np.array([[1, 0, 0],
                           [0, calpha, salpha],
                           [0, -salpha, calpha]])

    _tranform_b = np.array([[cbeta, 0, -sbeta],
                            [0, 1, 0],
                            [sbeta, 0, cbeta]])

    _tranform_c = _tranform_a.dot(_tranform_b)

    _a = 3 ** 0.5
    _b = 2 ** 0.5
    _c = 1 / 6 ** 0.5

    _rotation_matrix = np.array([[_a, 0, -_a],
                                 [1, 2, 1],
                                 [_b, -_b, _b]]) * _c

    _x_y = np.array([[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]])

    _x_z = np.array([[1, 0, 0],
                     [0, 0, 0],
                     [0, 0, 1]])

    _y_z = np.array([[0, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])

    _translated_mtrix = _rotation_matrix.dot(point)
    _isometric = _translated_mtrix.dot(_x_y)
    _isoproject_a = _tranform_c.dot(point)
    _isoproject_b = _isoproject_a.dot(_x_y)
    _top = _x_y.dot(point)
    _right = _x_z.dot(point)
    _front = _y_z.dot(point)

    class point_plot:
        pass

    _points = point_plot()
    _points.isometric = (_isometric[0], _isometric[1])
    _points.isoproject = (_isoproject_b[0], _isoproject_b[1])
    _points.front = (_front[1], _front[2])
    _points.right = (_right[0], _right[2])
    _points.top = (_top[0], _top[1])
    # return (isometric[0], isometric[1]), (front[1], front[2]), (right[0], right[2]), (top[0], top[1])
    return _points


def projection_rotator(angle, points, beta=45):
    alpha = math.sinh(math.tan(angle))

    def rotator(point):
        plane = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        matrix_a = np.array([[1, 0, 0], [0, math.cos(alpha), math.sin(alpha)], [0, -math.sin(alpha), math.cos(alpha)]])
        matrix_b = np.array([[math.cos(beta), 0, -math.sin(beta)], [0, 1, 0], [math.sin(beta), 0, math.cos(beta)]])
        matrix_c = matrix_a.dot(matrix_b)
        matrix_d = matrix_c.dot(point)
        return matrix_d.dot(plane)

    return list(map(rotator, points))


points = asarray(list(map(projection, normal)))
isometric = asarray([point.isometric for point in points])
isoproject = asarray([point.isoproject for point in points])
top = asarray([point.top for point in points])
right = asarray([point.right for point in points])
front = asarray([point.front for point in points])
max_point = vectors[2]
min_point = vectors[3]
max_distance = max(max_point)
axis_long = max_distance / 2

app = QtGui.QApplication([])
pg.setConfigOption('leftButtonPan', True)
pg.setConfigOption('useOpenGL', True)

w = gl.GLViewWidget()
w.setBackgroundColor(0.15)
w.show()
w.setWindowTitle('Strucpy v0.1 [BETA]')

# read = qfd.getOpenFileName(w, "Open DXF", "c:\\", "dfx files (*.dxf)")
# vectors = read_dxf(read[0])
# w.showFullScreen()


w.opts['center'] = QtGui.QVector3D((max_point[0] - min_point[0]) / 2 + min_point[0],
                                   (max_point[1] - min_point[1]) / 2 + min_point[1],
                                   max_point[2])

w.setCameraPosition(distance=max_distance * 10, azimuth=180, elevation=90)

plt_isom = gl.GLLinePlotItem(pos=isometric,
                             mode='lines',
                             antialias=True,
                             color=[0.4, 0.2, 0.3, 0.9],
                             width=1)
# w.addItem(plt_isom)

plt_isopro = gl.GLLinePlotItem(pos=isoproject,
                             mode='lines',
                             antialias=True,
                             color=[0.4, 0.2, 0.3, 0.9],
                             width=1)
w.addItem(plt_isopro)
# print(isometric[1])
# plt_isom.rotate(45, 100, 100, 100)

plt_isom.viewTransform()
plt_isom.scale(10,10,10)

# plt_front = gl.GLLinePlotItem(pos=front,
#                               mode='lines',
#                               antialias=True,
#                               color=[0.4, 0.2, 0.3, 0.9],
#                               width=1)
# w.addItem(plt_front)
# plt_front.rotate(45, 100, 100, 0)

# plt_top = gl.GLLinePlotItem(pos=top,
#                             mode='lines',
#                             antialias=True,
#                             color=[0.4, 0.2, 0.3, 0.9],
#                             width=1)
# w.addItem(plt_top)

# plt_right = gl.GLLinePlotItem(pos=right,
#                               mode='lines',
#                               antialias=True,
#                               color=[0.4, 0.2, 0.3, 0.9],
#                               width=1)
# w.addItem(plt_right)

# plt = gl.GLLinePlotItem(pos=asarray(normal),
#                         mode='lines',
#                         antialias=True,
#                         color=[0.4, 0.2, 0.3, 0.9],
#                         width=1)
# w.addItem(plt)


axis = gl.GLAxisItem()
axis.setSize(x=-axis_long, y=axis_long, z=-axis_long)
w.addItem(axis)

# select = gl.GLLinePlotItem(pos=geometry.array[:1001],
#                            mode='lines',
#                            antialias=True,
#                            width=7,
#                            color=[0, 255, 0, 0.7])
# w.addItem(select)

print(time.time() - start)
app.exec_()
