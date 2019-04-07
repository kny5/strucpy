from Model.classes.element_types import Element
# from Model.classes.geometry import Vector
from Model.functions.read_dxf import read_dxf, save_dxf
import json


class Controller:
    def __init__(self):
        self.vectors = []
        self.elements = []
        self.filename = "c:/repos/strucpy/dev_files/dxf/test.dxf"

    def get_filename(self):
        pass

    def assemble_elements(self):
        self.elements = list(map(Element, self.vectors))

    def add_element(self):
        pass

    def open_dxf(self):
        try:
            self.vectors = read_dxf(self.filename)
        except:
            return

    def save_dxf(self):
        try:
            save_dxf(self.vectors, self.filename)
        except:
            return

    def clear_all(self):
        self.vectors = []
        self.elements = []

    def export_as_json(self):
        export = json.dumps(str(self.db))
        with open('c:/repos/strucpy/dev_files/db.json', 'w') as outfile:
            json.dump(export, outfile)
        print(export)
