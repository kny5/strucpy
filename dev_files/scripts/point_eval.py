import math
import pyqtgraph as pg


def point_eval(point, vectors):
    x = point.x
    y = point.y
    pos = (x, y)
    for vector in vectors:
        start = vector[0]
        end = vector[1]
        d_x = end[0] - start[0]
        d_y = end[1] - start[1]
        ang_a = math.radians(math.tan(d_x/d_y))  # revisar
        p_x = x - start[0]
        p_y = y - start[1]
        ang_p = math.radians(math.tan(p_x/p_y))
        if start[0] <= x <= end[0] and start[1] <= y <= end[1] and start != end and ang_a == ang_p:
            return vector


def point_hover(plot):
    vectors = []
    d = lambda cursor: point_eval(cursor, vectors)
    return pg.SignalProxy(plot.scene().sigMouseMoved, rateLimit=60, slot=d)


point_hover(pg.plot())

