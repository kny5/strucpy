from Model.classes.element_types import Section, Element
from Model.functions.read_dxf import read_dxf, save_dxf
import json


class BufferHandler:
    def __init__(self):
        # lists
        self.vectors = []
        self.sections = []
        self.materials = []
        self.elements = []
        self.db = {}
        self.filename = "c:/repos/strucpy/dev_files/dxf/test.dxf"

    def assemble_elements(self):
        for vector in self.vectors:
            pass


    # import section class

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
        self.sections = []

    def export_as_json(self):
        export = json.dumps(str(self.db))
        with open('c:/repos/strucpy/dev_files/db.json', 'w') as outfile:
            json.dump(export, outfile)
        print(export)


