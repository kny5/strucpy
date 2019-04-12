"""NOT IN USE"""

from numpy import matlib


def k__(c, sections):
    matrix = matlib.zeros(shape=((sections + 1), (sections + 1)))
    matrix[0, 0] = matrix[-1, -1] = 3
    matrix[1, 1] = matrix[-2, -2] = 7 + c
    matrix[1, 0] = matrix[1, 2] = matrix[-2, -1] = matrix[-2, -3] = -4
    matrix[1, 3] = matrix[-2, -4] = 1
    for _i in range(2, sections - 1):
        matrix[_i, _i] = 6 + c
        matrix[_i, _i - 2] = matrix[_i, _i + 2] = 1
        matrix[_i, _i - 1] = matrix[_i, _i + 1] = -4
    return matrix


def k_mtx(element):

    # f_a = (element.section.kv * element.material.a1() * (element.vector.long / element.sections) ** 4) / \
    #       (1000 * element.material.e * element.material.izz())
    # f_b = (element.section.kh * element.material.a2() * (element.vector.long / element.sections) ** 4) / \
    #       (1000 * element.material.e * element.material.iyy())

    element.kzz = k__(element.f_a, element.sections)
    element.kyy = k__(element.f_b, element.sections)
