from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np


app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 40
w.show()
w.setWindowTitle('3d wire crankshaft')


i=0
crankshaft=np.array(([0,0,0],[2,0,0],[2,np.cos(i),np.sin(i)],[2.5,np.cos(i),np.sin(i)],[2.5,-np.cos(i),-np.sin(i)],[3,-np.cos(i),-np.sin(i)],[3,0,0],[6,0,0]))

plt=gl.GLLinePlotItem(pos=crankshaft)

w.addItem(plt)

conrod1=np.array(([2.25,np.cos(i),np.sin(i)],[2.25,np.cos(i)+2.5,0]))
plt1=gl.GLLinePlotItem(pos=conrod1)
w.addItem(plt1)

conrod2=np.array(([3.25,-np.cos(i),-np.sin(i)],[3.25,-np.cos(i)-2.5,0]))
plt2=gl.GLLinePlotItem(pos=conrod2)
w.addItem(plt2)

def crankshaft():
  global i
  crankshaft=np.array(([0,0,0],[2,0,0],[2,np.cos(i),np.sin(i)],[2.5,np.cos(i),np.sin(i)],[2.5,-np.cos(i),-np.sin(i)],[3,-np.cos(i),-np.sin(i)],[3,0,0],[6,0,0]))
  conrod1=np.array(([2.25,np.cos(i),np.sin(i)],[2.25,np.cos(i)+2.5,0]))
  conrod2=np.array(([2.75,-np.cos(i),-np.sin(i)],[2.75,-np.cos(i)-2.5,0]))
  plt.setData(pos=crankshaft)
  plt1.setData(pos=conrod1)
  plt2.setData(pos=conrod2)
  i+=0.05

time=QtCore.QTimer()
time.timeout.connect(crankshaft)
time.start(0.5)
app.exec_()