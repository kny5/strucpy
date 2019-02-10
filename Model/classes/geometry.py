import numpy as np
import math
from itertools import count as it_counts
# from functools import reduce
# from operator import add


class Vector:
    # last_iso_projection = None
    alpha = 35
    beta = 50.3
    project_plane_matrix = np.array([[1, 0, 0],
                                     [0, -1, 0],
                                     [0, 0, 0]])

    points = {}

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.reformat_byz()
        self.selected = False
    # def process(self):
        self.long = abs((((self.end[0] - self.start[0]) ** 2) +
                         ((self.end[1] - self.start[1]) ** 2) +
                         ((self.end[2] - self.start[2]) ** 2)) ** 0.5)

        plane_xz = (((self.end[0] - self.start[0]) ** 2) +
                    ((self.end[2] - self.start[2]) ** 2)) ** 0.5

        if plane_xz != 0:
            _nu_ = math.degrees(math.asin((self.end[2] - self.start[2]) / plane_xz))
            if self.end[0] - self.start[0] < 0:
                self.nu = 180 - _nu_
            else:
                self.nu = _nu_
        else:
            self.nu = 0

        self.lm = math.degrees(math.asin((self.end[1] - self.start[1]) / self.long))

    def reformat_byz(self):
        if self.start[1] > self.end[1]:
            start = self.start
            self.start = self.end
            self.end = start
            # return True
        # else:
            # return False

    @classmethod
    def iso_projection(cls):
        _alpha = Vector.alpha
        _beta = Vector.beta
        calpha = math.cos(_alpha)
        salpha = math.sin(_alpha)
        cbeta = math.cos(_beta)
        sbeta = math.sin(_beta)

        _tranform_a = np.array([[1, 0, 0],
                                [0, calpha, salpha],
                                [0, -salpha, calpha]])

        _tranform_b = np.array([[cbeta, 0, -sbeta],
                                [0, 1, 0],
                                [sbeta, 0, cbeta]])

        cls.last_iso_projection = _tranform_a.dot(_tranform_b)

    @classmethod
    def to_2d(cls, point):
        _isoproject_a = np.array(point).dot(cls.last_iso_projection)
        # _isoproject_a = cls.last_iso_projection.dot(point)
        return _isoproject_a.dot(cls.project_plane_matrix)
        # return result[0], result[1]

    @property
    def start_2d(self):
        return Vector.to_2d(self.start)

    @property
    def end_2d(self):
        return Vector.to_2d(self.end)

    def clicked(self):
        if self.selected is False:
            self.selected = True
        else:
            self.selected = False
        return self.selected


class Node:
    n_id_gen = it_counts(1)

    def __init__(self, position):
        self.n_id = next(self.n_id_gen)
        self.position = position
        self.n_ve = []
        self.conf_springs = {'dx': 0.0, 'dy': 0.0, 'dz': 0.0, 'mx': 0.0, 'my': 0.0, 'mz': 0.0}
        self.conf_vcn = {'dx': 0.0, 'dy': 0.0, 'dz': 0.0, 'mx': 0.0, 'my': 0.0, 'mz': 0.0}
        self.conf = {'dx': True, 'dy': True, 'dz': True, 'mx': True, 'my': True, 'mz': True}
        self.n_springs = list(self.conf_springs.values())
        self.n_vcn = list(self.conf_vcn.values())
