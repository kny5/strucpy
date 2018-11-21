from numpy import matlib


def k_mtx(element):
    f_a = (element.kv * element.a1() * (element.long / element.SCC) ** 4) / (1000 * element.e * element.izz())
    f_b = (element.kh * element.a2() * (element.long / element.SCC) ** 4) / (1000 * element.e * element.iyy())

    def k__(c):
        k = matlib.zeros(shape=((element.SCC + 1), (element.SCC + 1)))
        k[0, 0] = k[-1, -1] = 3
        k[1, 1] = k[-2, -2] = 7 + c
        k[1, 0] = k[1, 2] = k[-2, -1] = k[-2, -3] = -4
        k[1, 3] = k[-2, -4] = 1
        for _i in range(2, element.SCC - 1):
            k[_i, _i] = 6 + c
            k[_i, _i - 2] = k[_i, _i + 2] = 1
            k[_i, _i - 1] = k[_i, _i + 1] = -4
        return k

    element.kzz = k__(f_a)
    element.kyy = k__(f_b)
3