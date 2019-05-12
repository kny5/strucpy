# from Model.classes.element_types import Element
# from Model.classes.geometry import Vector, Node
from Model.functions.read_dxf import read_dxf, save_dxf
# import json
from Model.classes.MainProgram import Program
# from Model.classes.MainUI import GraphicSystem
from Model.classes.geometry import Vector

class Controller:
    def __init__(self, parent):
        self.parent = parent
        self.filename = None
        self.program = Program(self)
        self.selection = set([])
        # self.views = None

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

    def clear_selection(self):
        self.selection.clear()
        self.parent.graphicsys.show_vector_selection()

    # def close_file(self):
    #     self.filename = None
    #     self.selection.clear()
    #     self.program = Program(self)
        # self.parent.graphicsys = GraphicSystem(self)

#     def multiple_views(self, view, selection):
#         self.views = {}
#         for obj in list(selection):
#             self.views.add(view(obj))
#         # return self.views

    def close_file(self):
        self.filename = None
        self.program.vectors = []
        self.program.elements = []
        self.parent.graphicsys.plot.setData([], [])
        Vector.matrix = []

    # def export_as_json(self):
    #     export = json.dumps(str(self.db))
    #     with open('c:/repos/strucpy/dev_files/db.json', 'w') as outfile:
    #         json.dump(export, outfile)
    #     print(export)
