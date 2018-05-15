""" Calculo de izz para tipo OR"""
def izz(self):
    x = 2 * ((self.bf * self.tf ** 3) / 12) + \
        2 * ((self.tw * (self.d - 2 * self.tf) ** 3) / 12) + \
        2 * ((self.bf * self.tf) * ((self.d - self.tf) / 2) ** 2)
    return x

def iyy(self):
    x = 2 * ((self.d * self.tw ** 3) / 12) + \
        2 * ((self.tf * (self.bf - 2 * self.tw) ** 3) / 12) + \
        2 * ((self.d * self.tw) * ((self.bf - self.tw) / 2) ** 2)
    return x

def j(self):
    x = (2 * ((self.bf - self.tw) * (self.d -self.tf)) ** 2) / \
        (((self.bf - self.tw) / self.tf) + ((self.d -self.tf) / self.tw))
    return x


#IR

def izz(self):
    x = 2 * ((self.bf * self.tf ** 3) / 12) + \
        2 * ((self.tw * (self.d - 2 * self.tf) ** 3) / 12) + \
        2 * ((self.bf * self.tf) * ((self.d - self.tf) / 2) ** 2)
    return x

def iyy(self):
    x = 2 * ((self.tf * self.bf ** 3) / 12) + \
        (((self.d - 2 * self.tf) * self.tw ** 3) / 12)
    return x

def j(self):
    x = ((2 * self.bf * self.tf ** 3) + ((self.d - self.tf) * self.tw ** 3) / 3
    return x

#OC

def izz(self):
    x = (0.25 * math.pi * (self.d / 2) ** 4) - ((0.25 * math.pi) * ((self.d - 2 * self.t) / 2) ** 4)
    return x

def iyy(self):
    x = self.izz()
    return x

def j(self):
    x = ((math.pi * self.d ** 4) / 32) - ((math.pi * (self.d - 2 * self.t) ** 4) / 32)
    return x
