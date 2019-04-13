# from Model.classes.element_types import Element
# from Model.classes.geometry import Vector
from Model.functions.read_dxf import read_dxf, save_dxf
# import json
from Model.classes.analysisprograms import Program


class Controller:
    def __init__(self, parent):
        self.parent = parent
        self.filename = None
        self.select_vectors = True
        self.selected_elements = set([])
        self.program = Program(self)

    def open_file(self):
        try:
            self.parent.set_filename()
            self.program.vectors = read_dxf(self.filename)
            self.parent.graphicsys.show_vectors()
        except:
            pass

    def save_file(self):
        try:
            save_dxf(self.program.vectors, self.filename)
        except:
            pass

    def close_file(self):
        self.program.vectors = []
        self.program.elements = []
        self.parent.graphicsys.plot.setData([], [])

    # def export_as_json(self):
    #     export = json.dumps(str(self.db))
    #     with open('c:/repos/strucpy/dev_files/db.json', 'w') as outfile:
    #         json.dump(export, outfile)
    #     print(export)
