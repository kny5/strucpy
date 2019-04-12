from Model.classes.element_types import Element
# from Model.classes.geometry import Vector
from Model.functions.read_dxf import read_dxf, save_dxf
import json
from PyQt5.QtWidgets import QFileDialog as qfd
from Model.classes.analysisprograms import AnalysisPrograms


class Controller:
    def __init__(self, parent):
        self.parent = parent
        self.vectors = []
        self.elements = []
        self.filename = None
        self.select_vectors = True
        self.selected_elements = set([])
        self.a_programs = AnalysisPrograms(self)

    def set_filename(self):
        try:
            file = qfd.getOpenFileName(self.parent, "Open DXF", "c:\\", "dfx files (*.dxf)")
            self.filename = file[0]
        except:
            return

    def get_filename(self):
        return self.filename

    def assemble_elements(self):
        self.select_vectors = False
        self.elements = list(map(Element, self.vectors))
        print(self.elements)

    def add_element(self):
        if self.elements.__len__() > 0:
            pass
        else:
            pass

    def opening_dxf(self):
        try:
            self.set_filename()
            self.vectors = read_dxf(self.filename)
            self.parent.graphicsys.show_vectors()
        except:
            pass

    def saving_dxf(self):
        try:
            save_dxf(self.vectors, self.filename)
        except:
            pass

    def deleting_all(self):
        self.vectors = []
        self.elements = []
        self.parent.graphicsys.plot.setData([], [])

    def export_as_json(self):
        export = json.dumps(str(self.db))
        with open('c:/repos/strucpy/dev_files/db.json', 'w') as outfile:
            json.dump(export, outfile)
        print(export)

