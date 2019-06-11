import matplotlib.pyplot as plt
from numpy import arange


class plotter:
    def __init__(self, element):
        self.results = element.results
        self.plot()

    def plot(self):
        _dict = self.results.__dict__
        fig = plt.figure(1)
        pos = 211
        for c, key in enumerate(_dict, 0):
            if key not in ['dry', 'drz', 'desp_imp_antes_y']:
                len = _dict[str(key)].__len__()
                fig.add_subplot()
                plt.plot(arange(0, len, 1), _dict[key])
        plt.show()



