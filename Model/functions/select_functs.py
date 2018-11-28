def select_by_id(id, elements):
    return list(map(lambda x: x if x.e_id == id else None, elements))