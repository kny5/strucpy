def select_by_id(id, elements):
    return list(map(lambda x: x if x.e_id == id else None, elements))


def select_by_z(z_val, elements):
    __selected = []
    for element in elements:
        if element.nodeStart.position[2] == z_val:
            __selected.append(element)
    return __selected


def select_by_exact_angle(angle, elements):
    __selected = []
    for element in elements:
        if element.vector.lm == angle:
            __selected.append(element)
    return __selected


# def select_by_less_than_angle(angle, elements):
#     __selected = []
#     for element in elements:
#         if element.vector.lm < angle:
#             __selected.append(element)
#     return __selected


def select_by_range_angle(base, maximo, elements):
    __selected = []
    for element in elements:
        if maximo > element.vector.lm > base:
            __selected.append(element)
    return __selected
