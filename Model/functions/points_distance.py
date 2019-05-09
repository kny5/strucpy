from math import sqrt


def dist_point_line(x1, y1, x2, y2, x3, y3):  # x3,y3 is the point
    px = x2 - x1
    py = y2 - y1
    sqr_point = px * px + py * py
    u = ((x3 - x1) * px + (y3 - y1) * py) / float(sqr_point)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    x = x1 + u * px
    y = y1 + u * py
    dx = x - x3
    dy = y - y3
    return sqrt(dx**2 + dy**2)

def dist_point_point(x, y, mouse_pos):  # x3,y3 is the point
    return abs(sqrt(((x - mouse_pos[0])**2) + ((y - mouse_pos[1])**2)))
