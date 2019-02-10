import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from Model.functions.read_dxf import read_dxf


verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
    )

vectors = read_dxf('test.all_vectors')


def cube():
    glBegin(GL_LINES)
    for vector in vectors:
        glVertex3fv(vector.start, vector.end)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(100, 0.5, 0, 1.0)

    help(gluPerspective)


    glTranslatef(0.0, 20.0, -40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()
        glRotatef(1, 0, 1, 0)
        pygame.display.flip()
        pygame.time.wait(10)


main()