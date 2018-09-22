import itertools

class Node:

    n_id_gen = itertools.count(1)
    counter = 0

    def __init__(self, position, **kwargs):
        self.n_id = str(next(self.n_id_gen))
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.position = position
        self.ve_parcial = []
        self.n_vcn = []
        self.n_apoyo = []

        for value in list(kwargs.values()):
            if value:
                try:
                    self.n_vcn.append(value[0])
                    self.n_apoyo.append(value[1])
                except TypeError:
                    self.n_vcn.append(0)
                    self.n_apoyo.append(0)
                self.ac_nodo += 1
                ve_parcial.append(ac_nodo)
                Max_val.append(ac_nodo)
            else:
                self.ve_parcial.append(0)
                self.n_apoyo.append(0)

        Nodos.append(self)

        self.v_c_n += self.n_vcn
