from Model.functions.read_dxf import read_dxf, save_dxf
# import json
from Model.classes.MainProgram import Program
from Model.classes.geometry import Vector
from ui_views.vector_edit import Ui_vector_widget

class Controller:

    def __init__(self, parent):
        self.parent = parent
        self.filename = None
        self.program = Program(self)
        self.selection = set([])
        self.uis = self.parent.uis
        # self.views = None

    def open_file(self):
        try:
            self.parent.set_filename()
            self.program.vectors = set(read_dxf(self.filename))
            self.parent.graphicsys.show_vectors()
        except Exception:
            pass

    def save_file(self):
        try:
            save_dxf(self.program.vectors, self.filename)
        except Exception:
            pass

    def clear_selection(self):
        self.selection.clear()
        self.parent.graphicsys.show_vector_selection()

    def close_file(self):
        self.filename = None
        self.program = Program(self)
        self.selection = set([])
        self.parent.graphicsys.plot.setData([], [])
        self.clear_selection()
        Vector.matrix = []

    def add_vector(self):
        vector = Vector((0,0,0,), (1,1,1))
        ui = Ui_vector_widget(self, vector)
        self.uis.add(ui)

    def edit_vector(self):
        if self.selection.__len__() > 0:
            self.uis.clear()
            for vector in self.selection:
                ui = Ui_vector_widget(self, vector)
                self.uis.add(ui)
                ui.show()
            self.selection.clear()
        else:
            self.parent.notificator('Error', 'No hay vectores seleccionados' )

    def del_selection(self):
        for vector in self.selection:
            self.program.vectors.remove(vector)
        self.selection = set([])
        self.parent.graphicsys.plot.setData([], [])
        self.clear_selection()
        Vector.matrix = []
        self.parent.graphicsys.show_vectors()


    def set_vectors(self):
        pass

    def set_nodes(self):
        pass

    def edit_multi_element(self):
        pass

    def edit_node(self):
        pass

    def edit_type(self):
        pass

    # def multiple_views(self, view, selection):
    #     self.views = {}
    #     for obj in list(selection):
    #         self.views.add(view(obj))
    #     return self.views

    # def export_as_json(self):
    #     export = json.dumps(str(self.db))
    #     with open('c:/repos/strucpy/dev_files/db.json', 'w') as outfile:
    #         json.dump(export, outfile)
    #     print(export)
