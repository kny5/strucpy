from math import sqrt


def dist_point_line(start, end, cursor):  # x3,y3 is the point
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]
    x3 = cursor[0]
    y3 = cursor[1]
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

def dist_point_point(point, mouse_pos):
    return abs(sqrt(((point[0] - mouse_pos[0])**2) + ((point[1] - mouse_pos[1])**2)))
