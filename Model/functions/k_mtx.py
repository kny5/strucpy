from numpy import matlib


def k_mtx(section):
    f_a = (section.kv * section.a1() * (section.long / section.SCC) ** 4) / (1000 * section.e * section.izz())
    f_b = (section.kh * section.a2() * (section.long / section.SCC) ** 4) / (1000 * section.e * section.iyy())

    def k__(c):
        k = matlib.zeros(shape=((section.SCC + 1), (section.SCC + 1)))
        k[0, 0] = k[-1, -1] = 3
        k[1, 1] = k[-2, -2] = 7 + c
        k[1, 0] = k[1, 2] = k[-2, -1] = k[-2, -3] = -4
        k[1, 3] = k[-2, -4] = 1
        for _i in range(2, section.SCC - 1):
            k[_i, _i] = 6 + c
            k[_i, _i - 2] = k[_i, _i + 2] = 1
            k[_i, _i - 1] = k[_i, _i + 1] = -4
        return k

    section.kzz = k__(f_a)
    section.kyy = k__(f_b)