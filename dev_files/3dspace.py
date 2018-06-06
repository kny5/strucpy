import pyglet
# import all of opengl functions
from pyglet.gl import *

win = pyglet.window.Window()


def cube(dim, orig):
    lis = [orig, orig, orig]
    glVertex3f(orig,dim,orig)
    glVertex3f(dim,orig,dim)
    for i in range(len(lis)):
        lis[i] = dim
        glVertex3f(lis[0], lis[1], lis[2])
        print(lis)
    for j in range(len(lis)):
        lis[j] = orig
        glVertex3f(lis[0], lis[1], lis[2])
        print(lis)
    return True


@win.event
def on_draw():
    # create a line context

    glPushMatrix()
    glRotatef(45, 0, 0, 0)
    glPointSize(10)
    #gluLookAt(-10, -200, 5, 100, 100, 100, 0, 1, 0)
    glScalef(0.9, 0.9, 0.9)
    glBegin(GL_POINTS)
    # create a line, x,y,z


    cube(300, 100)

    glEnd()


pyglet.app.run()