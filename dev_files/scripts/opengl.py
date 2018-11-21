import pyglet
from pyglet.gl import *
from pyglet import clock, window
import sys
'''
    http://www.learnersdictionary.com/search/aspect
    a dictionary site

    http://www.opengl.org/sdk/docs/man2/
    opengl api reference

'''

def vector(type, *args):
    '''
        return a ctype array
        GLfloat
        GLuint
        ...
    '''
    return (type*len(args))(*args)



class model:
    def __init__(self, vertices, colorMatrix, indice):
        self.vertices = vector(GLfloat, *vertices)
        self.colorMatrix = vector(GLfloat, *colorMatrix)
        self.indice = vector(GLuint, *indice)
        self.angle = 0

    def update(self):
        self.angle += 0.1
        self.angle %= 360

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glRotatef(self.angle, 1, 1, 0)


        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)

        glColorPointer(3, GL_FLOAT, 0, self.colorMatrix)
        glVertexPointer(3, GL_FLOAT, 0, self.vertices)
        glDrawElements(GL_QUADS, len(self.indice), GL_UNSIGNED_INT, self.indice)


        glDisableClientState(GL_COLOR_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)



class world:
    def __init__(self):
        self.element = []

    def update(self, dt):
        for obj in self.element:
            obj.update()

    def addModel(self, model):
        self.element.append(model)

    def draw(self):
        for obj in self.element:
            obj.draw()


def setup():
    # look for GL_DEPTH_BUFFER_BIT
    glEnable(GL_DEPTH_TEST)







win = window.Window(fullscreen=False, vsync=True, resizable=False, height=600, width=600)
mWorld = world()

cube = (
    20, 5, 20, #0
    -20, 5, 20, #1
    -20, -20, 20, #2
    20, -20, 20, #3
    20, 5, -20, #4
    -20, 5, -20, #5
    -20, -20, -20, #6
    20, -20, -20 #7
)


color = (
    1, 0, 0,
    1, 0, 0,
    1, 0, 0,
    1, 0, 0,
    0, 1, 0,
    0, 1, 0,
    0, 0, 1,
    0, 0, 1
)

indice = (
    0, 1, 2, 3, # front face
    0, 4, 5, 1, # top face
    4, 0, 3, 7, # right face
    1, 5, 6, 2, # left face
    3, 2, 6, 7, # bottom face
    4, 7, 6, 5  #back face
)

obj = model(cube, color, indice)
mWorld.addModel(obj)


@win.event
def on_resize(width, height):
    glViewport(-100, 100, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-50, 50, -50, 50, -50, 50)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

@win.event
def on_draw():
    glClearColor(0.2, 0.2, 0.2, 0.4)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mWorld.draw()


pyglet.clock.schedule(mWorld.update)
clock.set_fps_limit(10)
setup()
pyglet.app.run()