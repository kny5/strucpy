import pyglet
from pyglet.gl import *

win = pyglet.window.Window(400,280)


@win.event
def on_draw():
    # Clear buffers
    glClearColor(0.196, 0.196, 0.196, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glScalef(0.6, 0.6, 0.6)
    # Draw some stuff
    glBegin(GL_LINES)
    glVertex2i(50, 50)
    glVertex2i(600, 50)
    glVertex2i(50, 50)
    glVertex2i(50, 400)
    glVertex2i(50, 400)
    glVertex2i(600,400)
    glVertex2i(600,50)
    glVertex2i(600,400)
    glVertex2i(300,50)
    glVertex2i(300,400)
    glEnd()

    # Draw some stuff
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2i(50, 50)
    glVertex2i(100, 400)
    glVertex2i(100, 50)
    glVertex2i(600, 50)
    glVertex2i(50, 400)
    glVertex2i(600, 400)
    glVertex2i(300, 50)
    glVertex2i(300, 400)
    glEnd()



pyglet.app.run()