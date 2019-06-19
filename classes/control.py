from functions.read_dxf import read_dxf, save_dxf
from classes.MainProgram import Program
from classes.geometry import Vector, Node
from classes.element_types import Element
from ui_views.vector_edit import VectorEditor
from ui_views.loads_edit import LoadsEditor
from ui_views.node_edit import NodeEditor
from ui_views.type_edit import TypeEditor
from ui_views.Results import Ui_Form as ResultsViewer
# from ui_views.Inpector import App as ResultsViewer
from functools import reduce
from operator import add

class Controller:

    def __init__(self, parent):
        self.parent = parent
        self.filename = None
        self.selection = set([])
        self.dict_nodes = {}

        self.uis_vector = dict()
        self.uis_element = dict()
        self.uis_node = dict()
        self.uis_type = dict()
        self.uis_results = dict()

        # self.views = None
        self.program = Program(self)

    def open_file(self):
        try:
            self.parent.set_filename()
            dxf = read_dxf(self.filename)
            self.program.vectors = dxf
            self.parent.graphicsys.show_vectors()
            self.set_nodes()
            self.set_vectors()
            self.parent.graphicsys.show_points()
            # print(self.program.vectors, self.program.elements, self.program.nodes)
        except Exception:
            pass

    def save_file(self):
        try:
            save_dxf(self.program.vectors, self.filename)
        except Exception:
            pass
    def save_as_new(self):
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
            for vector in self.selection:
                # # print("--" + str(self.uis_vector.get(str(vector.pos))))
                ui = VectorEditor(self, vector)
                self.uis_vector[str(vector.pos)] = ui
                #this ui set is buggy
                # if self.uis_vector.get(str(vector.pos)) is None:
                #     ui = VectorEditor(self, vector)
                #     self.uis_vector[str(vector.pos)] = ui
                # else:
                #     ui = self.uis_vector.get(str(vector.pos))
                ui.show()
            # self.selection.clear()
        else:
            self.parent.notificator('Error', 'No hay vectores seleccionados' )

    def del_selection(self):
        if self.selection.__len__() > 0:
            # add confirmation dialog
            for vector in self.selection:
                if vector in self.program.vectors:
                    self.program.vectors.discard(vector)
            self.selection.clear()
            self.parent.graphicsys.plot.setData([], [])
            Vector.matrix = []
            self.parent.graphicsys.show_vectors()
            self.parent.graphicsys.show_points()
            self.parent.graphicsys.show_vector_selection()
        else:
            self.parent.notificator('Error', 'No hay vectores seleccionados')

    def set_vectors(self):
        if self.program.vectors.__len__() > 0:
            self.program.elements = set(list(map(Element, [vector for vector in self.program.vectors if vector.parent is None])) )
            # # print(self.program.elements.__len__())
            # # print(str([vector.parent for vector in self.selection]))
        else:
            self.parent.notificator('Error', 'No hay vectores')

    def set_nodes(self):
        try:
            list_points = reduce(add, [[vector.start, vector.end] for vector in self.program.vectors if vector.parent is None])
            nodes = list(map(Node, list_points))
            # # print(nodes)
            dict_points = dict(zip(list_points, nodes))
            for key in dict_points.keys():
                if not key in self.dict_nodes:
                    self.dict_nodes[key] = dict_points[key]
            # # print(self.dict_nodes)
        except:
            # print('hi bug')
            pass

    def view_results_all(self):
        if self.selection.__len__() > 0:
            for vector in self.selection:
                if self.uis_results.get(str(vector.pos)) is None:
                    ui = ResultsViewer(vector.parent)
                    self.uis_results[str(vector.pos)] = ui
                else:
                    ui = self.uis_results[str(vector.pos)]
                ui.show()
        else:
            self.parent.notificator('Error', 'No hay vectores seleccionados')


    def edit_loads(self):
        if self.selection.__len__() > 0:
            for vector in self.selection:
                if self.uis_element.get(str(vector.pos)) is None:
                    ui = LoadsEditor(self, vector.parent)
                    self.uis_element[str(vector.pos)] = ui
                else:
                    ui = self.uis_element[str(vector.pos)]
                ui.show()
        else:
            self.parent.notificator('Error', 'No hay vectores seleccionados')

    def edit_node(self):
        if self.selection.__len__() > 0:
            self.uis_node.clear()
            for vector in self.selection:
                # print(self.uis_node.get(str(vector.start)))
                if self.uis_node.get(str(vector.start)) is None:
                    start = self.dict_nodes[vector.start]
                    u1 = NodeEditor(start)
                    self.uis_node[str(vector.start)] = u1
                else:
                    u1 = self.uis_node.get(str(vector.start))
                if self.uis_node.get(str(vector.end)) is None:
                    end = self.dict_nodes[vector.end]
                    u2 = NodeEditor(end)
                    self.uis_node[str(vector.end)] = u2
                else:
                    u2 = self.uis_node.get(str(vector.end))
                u1.show()
                u2.show()
            # self.selection.clear()
        else:
            self.parent.notificator('Error', 'No hay vectores seleccionados')

    #def edit_loads_invector(self):
    #    if self.selection.__len__() > 0:
    #        for vector in self.selection:
    #            if self.parent.uis_element.get(str(vector.pos)) is None:
    #                ui = LoadsEditor(self, vector.parent)
    #                self.parent.uis_element[str(vector.pos)] = ui
    #            else:
    #                ui = self.parent.uis_element[str(vector.pos)]
    #            ui.show()
    #    # elif self.selection.__len__() == 0 and self.program.vectors.__len__() > 0:
    #    #     for vector in self.program.vectors:
    #    #         if self.parent.uis_element.get(str(vector.pos)) is None:
    #    #             ui = LoadsEditor(self, vector.parent)
    #    #             self.parent.uis_element[str(vector.pos)] = ui
    #    #         else:
    #    #             ui = self.parent.uis_element[str(vector.pos)]
    #    #         ui.show()
    #    else:
    #        self.parent.notificator('Error', 'No hay vectores seleccionados')

    def edit_section_type(self):
        if self.selection.__len__() > 0:
            # for vector in self.selection:
            if self.uis_type.get('partial') is None:
                ui = TypeEditor([vector.parent for vector in self.selection])
                self.uis_type['partial'] = ui
            else:
                ui = self.uis_type['partial']
            ui.show()
        elif self.selection.__len__() == 0 and self.program.vectors.__len__() > 0:
            ui = TypeEditor([ vector.parent for vector in self.program.vectors])
            self.uis_type['all'] = ui
            ui.show()
        # else:
        #     self.parent.notificator('Error', 'No hay vectores seleccionados')

    def run(self):
        self.program.run()
