from Model.classes.element_types import Node


def set_nodes(self, Vector):
        #   check for other existent nodes
    for node in self.Nodes:
        if node.position == Vector.start:
            setattr(Vector, "nodeStart", node)
        elif node.position == Vector.end:
            setattr(Vector, "nodeEnd", node)
    #   creating new nodes
    try:
        if Vector.nodeStart:
            pass
    except AttributeError:
        Vector.nodeStart = Node(Vector.start)
        self.Nodes.append(Vector.nodeStart)
        for _bool in Vector.start_conf.values():
            if _bool:
                self.freedom += 1
                Vector.nodeStart.n_ve.append(self.freedom)
                try:
                    Vector.nodeStart.n_vcn.append(_bool[0])
                    Vector.nodeStart.n_springs.append(_bool[1])
                except TypeError:
                    Vector.nodeStart.n_vcn.append(0)
                    Vector.nodeStart.n_springs.append(0)
            else:
                Vector.nodeStart.n_ve.append(0)
    #   ...and repeat for nodeEnd
    try:
        if Vector.nodeEnd:
            pass
    except AttributeError:
        Vector.nodeEnd = Node(Vector.end)
        self.Nodes.append(Vector.nodeEnd)
        for _bool in Vector.end_conf.values():
            if _bool:
                self.freedom += 1
                Vector.nodeEnd.n_ve.append(self.freedom)
                try:
                    Vector.nodeEnd.n_vcn.append(_bool[0])
                    Vector.nodeEnd.n_springs.append(_bool[1])
                except TypeError:
                    Vector.nodeEnd.n_vcn.append(0)
                    Vector.nodeEnd.n_springs.append(0)
            else:
                Vector.nodeEnd.n_ve.append(0)

    Vector.ve = Vector.nodeStart.n_ve + Vector.nodeEnd.n_ve
    Vector.springs = Vector.nodeStart.n_springs + Vector.nodeEnd.n_springs
