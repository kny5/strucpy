#materials
#1.- concrete
#2.- steel type OR
#3.- steel type IR

if material == 1:
    PP = ((BP * HZ) / 10000) * 2.4
elif material == 2:
    BF = 0
    D = 0
    TW = 0
    TF = 0
    PV_STEEL = 0.0007849
    PP = ((BF * D) - (BF - 2 * TW) * (D - 2 * TF)) * PV_STEEL
elif material == 3:
