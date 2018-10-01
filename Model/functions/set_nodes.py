from Model.classes.element_types import Node
import math


def set_nodes(self, element):
        #   check for other existent nodes
    for node in self.Nodes:
        if node.position == element.start:
            setattr(element, "nodeStart", node)
        elif node.position == element.end:
            setattr(element, "nodeEnd", node)
    #   creating new nodes
    try:
        if element.nodeStart:
            pass
    except AttributeError:
        element.nodeStart = Node(element.start)
        self.Nodes.append(element.nodeStart)
        for _bool in element.start_conf.values():
            if _bool:
                self.freedom += 1
                element.nodeStart.n_ve.append(self.freedom)
                try:
                    element.nodeStart.n_vcn.append(_bool[0])
                    element.nodeStart.n_springs.append(_bool[1])
                except TypeError:
                    element.nodeStart.n_vcn.append(0)
                    element.nodeStart.n_springs.append(0)
            else:
                element.nodeStart.n_ve.append(0)
    #   ...and repeat for nodeEnd
    try:
        if element.nodeEnd:
            pass
    except AttributeError:
        element.nodeEnd = Node(element.end)
        self.Nodes.append(element.nodeEnd)
        for _bool in element.end_conf.values():
            if _bool:
                self.freedom += 1
                element.nodeEnd.n_ve.append(self.freedom)
                try:
                    element.nodeEnd.n_vcn.append(_bool[0])
                    element.nodeEnd.n_springs.append(_bool[1])
                except TypeError:
                    element.nodeEnd.n_vcn.append(0)
                    element.nodeEnd.n_springs.append(0)
            else:
                element.nodeEnd.n_ve.append(0)

    element.ve = element.nodeStart.n_ve + element.nodeEnd.n_ve
    element.springs = element.nodeStart.n_springs + element.nodeEnd.n_springs

    element.long = abs((((element.end[0] - element.start[0]) ** 2) +
                     ((element.end[1] - element.start[1]) ** 2) +
                     ((element.end[2] - element.start[2]) ** 2)) ** 0.5)

    plane_xz = (((element.nodeEnd.x - element.nodeStart.x) ** 2) +
                ((element.nodeEnd.z - element.nodeStart.z) ** 2)) ** 0.5

    if plane_xz != 0:
        _nu_ = math.degrees(math.asin((element.nodeEnd.z - element.nodeStart.z) / plane_xz))
        if element.nodeEnd.x - element.nodeStart.x < 0:
            element.nu = 180 - _nu_
        else:
            element.nu = _nu_
    else:
        element.nu = 0

    element.lm = math.degrees(math.asin((element.nodeEnd.y - element.nodeStart.y) / element.long))


