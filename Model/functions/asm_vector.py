def asm_v(nodes):
    freedom = 0
    for node in nodes:
        for _bool in node.conf.values():
            if _bool:
                freedom += 1
                node.n_ve.append(freedom)
            else:
                node.n_ve.append(0)
    return freedom
