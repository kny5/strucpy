from Model.functions.read_dxf import read_dxf, save_dxf
# import json
from Model.classes.MainProgram import Program
from Model.classes.geometry import Vector, Node
from Model.classes.element_types import Element
from ui_views.vector_edit import VectorEditor
from ui_views.element_edit import ElementEditor
from ui_views.node_edit import NodeEditor
from functools import reduce
from operator import add

class Controller:

    def __init__(self, parent):
        self.parent = parent
        self.filename = None
        self.program = Program(self)
        self.selection = set([])
        self.dict_nodes = {}
        # self.views = None

    def open_file(self):
        try:
            self.parent.set_filename()
            dxf = read_dxf(self.filename)
            self.program.vectors = dxf
            # self.program.vectors = dxf[0]
            # self.program.nodes = dxf[1]
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

    def select_all(self):
        self.selection = self.program.vectors

    def close_file(self):
        self.filename = None
        self.program = Program(self)
        self.selection = set([])
        self.parent.graphicsys.plot.setData([], [])
        self.clear_selection()
        Vector.matrix = []

    def add_vector(self):
        vector = Vector((0,0,0), (1,1,1))
        self.selection.add(vector)
        self.edit_vector()


    def edit_vector(self):
        if self.selection.__len__() > 0:
            # self.parent.uis_vector.clear()
            for vector in self.selection:
                if self.parent.uis_vector.get(str(vector.pos)) is None:
                    ui = VectorEditor(self, vector)
                    self.parent.uis_vector[str(vector.pos)] = ui
                else:
                    ui = self.parent.uis_vector.get(str(vector.pos))
                ui.show()
            self.selection.clear()
        else:
            self.parent.notificator('Error', 'No hay vectores seleccionados' )

    def del_selection(self):
        if self.selection.__len__() > 0:
            for vector in self.selection:
                print(vector)
                if vector in self.program.vectors:
                    self.program.vectors.discard(vector)
                else:
                    pass
            self.selection.clear()
            self.parent.graphicsys.plot.setData([], [])
            Vector.matrix = []
            # self.parent.graphicsys.show_vectors()
        else:
            self.parent.notificator('Error', 'No hay vectores seleccionados')

    def set_vectors(self):
        if self.program.vectors.__len__() > 0:
            self.program.elements = set(list(map(Element, [vector for vector in self.program.vectors if vector.parent is None])) )
            print(self.program.elements.__len__())
            print(str([vector.parent for vector in self.selection]))
        else:
            self.parent.notificator('Error', 'No hay vectores')

    def set_nodes(self):
        try:
            list_points = reduce(add, [[vector.start, vector.end] for vector in self.program.vectors if vector.parent is None])
            nodes = list(map(Node, list_points))
            dict_points = dict(zip(list_points, nodes))
            for key in dict_points.keys():
                if not key in self.dict_nodes:
                    self.dict_nodes[key] = dict_points[key]
            print(self.dict_nodes)
        except:
            pass

    def edit_element(self):
        if self.selection.__len__() > 0:
            for vector in self.selection:
                if self.parent.uis_element.get(str(vector.pos)) is None:
                    ui = ElementEditor(self, vector.parent)
                    self.parent.uis_element[str(vector.pos)] = ui
                else:
                    ui = self.parent.uis_element[str(vector.pos)]
                ui.show()
            self.selection.clear()
        else:
            self.parent.notificator('Error', 'No hay vectores seleccionados')

    def edit_node(self):
        if self.selection.__len__() > 0:
            self.parent.uis_node.clear()
            for vector in self.selection:
                if self.parent.uis_node.get(str(vector.start)) is None:
                    start = self.dict_nodes[vector.start]
                    u1 = NodeEditor(start)
                    self.parent.uis_node[str(vector.start)] = u1
                else:
                    u1 = self.parent.uis_node.get(str(vector.start))
                if self.parent.uis_node.get(str(vector.end)) is None:
                    end = self.dict_nodes[vector.end]
                    u2 = NodeEditor(end)
                    self.parent.uis_node[str(vector.end)] = u2
                else:
                    u2 = self.parent.uis_node.get(str(vector.end))
                u1.show()
                u2.show()
            self.selection.clear()

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
