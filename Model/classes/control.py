from Model.classes.element_types import Element
# from Model.classes.geometry import Vector
from Model.functions.read_dxf import read_dxf, save_dxf
import json
from PyQt5.QtWidgets import QFileDialog as qfd


class Controller:
    def __init__(self, parent):
        self.parent = parent
        self.vectors = []
        self.elements = []
        self.filename = None

    def set_filename(self):
        file = qfd.getOpenFileName(self.parent, "Open DXF", "c:\\", "dfx files (*.dxf)")
        self.filename = file[0]

    def get_filename(self):
        return self.filename

    def assemble_elements(self):
        self.elements = list(map(Element, self.vectors))

    def add_element(self):
        pass

    def opening_dxf(self):
        try:
            self.set_filename()
            self.vectors = read_dxf(self.filename)
        except:
            return

    def saving_dxf(self):
        try:
            save_dxf(self.vectors, self.filename)
        except:
            return

    def deleting_all(self):
        self.vectors = []
        self.elements = []

    def export_as_json(self):
        export = json.dumps(str(self.db))
        with open('c:/repos/strucpy/dev_files/db.json', 'w') as outfile:
            json.dump(export, outfile)
        print(export)
