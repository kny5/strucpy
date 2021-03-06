import numpy as np
import math
from itertools import count as it_counts
from functools import reduce
from operator import add


class Projector:
    parent = None
    alpha = 35
    beta = 50.3
    project_plane_matrix = np.array([[1, 0, 0],
                                     [0, -1, 0],
                                     [0, 0, 0]])
    matrix = []
    last_iso_projection = []

    def set_parent(self, parent):
        self.parent = parent

    @classmethod
    def default_position(cls):
        cls.alpha = 35
        cls.beta = 45

    @classmethod
    def iso_projection(cls):
        _alpha = cls.alpha
        _beta = cls.beta
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

        # _tranform_b = np.array([[cbeta, sbeta, 0],
        #                         [-sbeta, cbeta, 0],
        #                         [0, 0, 1]])

        cls.last_iso_projection = _tranform_a.dot(_tranform_b)

    @classmethod
    def to_2d(cls, point):
        _isoproject_a = np.array(point).dot(cls.last_iso_projection)
        return _isoproject_a.dot(cls.project_plane_matrix)

    @classmethod
    def process_to_matrix(cls, vectors, selection=False):
        if not selection:
            if cls.matrix.__len__() == 0:
                cls.matrix = np.array(reduce(add, [[vector.start, vector.end] for vector in vectors]))
                projection = cls.matrix.dot(cls.last_iso_projection)
            else:
                projection = cls.matrix.dot(cls.last_iso_projection)
        else:
            matrix = np.array(reduce(add, [[vector.start, vector.end] for vector in vectors]))
            projection = matrix.dot(cls.last_iso_projection)
        return projection.dot(cls.project_plane_matrix)

    @property
    def start_2d(self):
        return self.to_2d(self.start)

    @property
    def end_2d(self):
        return self.to_2d(self.end)


class Vector(Projector):
    def __init__(self, start, end):
        super().__init__()
        self.start = start
        self.end = end
        self.reformat_byz()

    @property
    def pos(self):
        return self.start, self.end

    @property
    def long(self):
        return abs((((self.end[0] - self.start[0]) ** 2) + ((self.end[1] - self.start[1]) ** 2) +
             ((self.end[2] - self.start[2]) ** 2)) ** 0.5)

    @property
    def plane_xz(self):
        return (((self.end[0] - self.start[0]) ** 2) +
                    ((self.end[2] - self.start[2]) ** 2)) ** 0.5

    @property
    def nu(self):
        if self.plane_xz != 0:
            _nu_ = math.degrees(math.asin((self.end[2] - self.start[2]) / self.plane_xz))
            if self.end[0] - self.start[0] < 0:
                return 180 - _nu_
            else:
                return _nu_
        else:
            return 0

    @property
    def lm(self):
        return math.degrees(math.asin((self.end[1] - self.start[1]) / self.long))

    def reformat_byz(self):
        if self.start[1] > self.end[1]:
            start = self.start
            self.start = self.end
            self.end = start
        # elif self.start == (0,0,0):
        #     pass


class Node:
    n_id_gen = it_counts(1)

    def __init__(self, position):
        # self.assigned = False
        self.n_id = next(self.n_id_gen)
        self.pos = position
        self.n_ve = []
        self.conf = {'dx': {'spring': 0.0, 'load': 0.0, 'activated': True},
                     'dy': {'spring': 0.0, 'load': 0.0, 'activated': True},
                     'dz': {'spring': 0.0, 'load': 0.0, 'activated': True},
                     'mx': {'spring': 0.0, 'load': 0.0, 'activated': True},
                     'my': {'spring': 0.0, 'load': 0.0, 'activated': True},
                     'mz': {'spring': 0.0, 'load': 0.0, 'activated': True}}

        # self.conf_springs = {'dx': 0.0, 'dy': 0.0, 'dz': 0.0, 'mx': 0.0, 'my': 0.0, 'mz': 0.0}
        # self.conf_vcn = {'dx': 0.0, 'dy': 0.0, 'dz': 0.0, 'mx': 0.0, 'my': 0.0, 'mz': 0.0}
        # self.conf = {'dx': True, 'dy': True, 'dz': True, 'mx': True, 'my': True, 'mz': True}

    @property
    def n_springs(self):
        return [value['spring'] for value in self.conf.values()] # if value['activated'] is True]

    @property
    def n_vcn(self):
        return [value['load'] for value in self.conf.values() if value['activated'] == True]

