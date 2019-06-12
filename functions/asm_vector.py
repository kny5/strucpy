def asm_v(nodes):
    # print("asm_v")
    freedom = 0
    for node in nodes:
        n_ve = []
        for _bool in node.conf.values():
            if _bool:
                freedom += 1
                n_ve.append(freedom)
            else:
                n_ve.append(0)
        node.n_ve = n_ve
    # print(freedom)
    return freedom
