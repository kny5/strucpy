from Model.classes.geometry import Vector


class controller:
    def __init__(self):
        self.all_vectors = []
        self.vector_set = set([])

    def open_dxf(self):
        try:
            file = qfd.getOpenFileName(self, "Open DXF", "c:\\", "dfx files (*.dxf)")
            self.all_vectors = read_dxf(file[0])
            self.matrix_plot = np.array(reduce(add, [[vector.start, vector.end] for vector in self.all_vectors]))
            Vector.iso_projection()
            self.plot()
        except:
            return

    def save_dxf(self):
        try:
            file = qfd.getSaveFileName(self, "Save DXF", "c:\\", "dxf files (*.dxf)")
            save_dxf(self.all_vectors, file[0])
        except:
            return

    def clear_all(self):
        self.all_vectors = []
        self.vector_set = {}
        Vector.alpha = 35
        Vector.beta = 50.3
        Vector.iso_projection()
        self.plot()
        self.plot_select()
        return

    def xy_vectors_toplot(self, vectors):
        # # return np.array(reduce(add, [[vector.start_2d, vector.end_2d] for vector in vectors]))
        if vectors != self.all_vectors:
            matrix = np.array(reduce(add, [[vector.start, vector.end] for vector in vectors]))
            # print(matrix.shape)
            projection = matrix.dot(Vector.last_iso_projection)
            return projection.dot(Vector.project_plane_matrix)
        else:
            # matrix = Vector.last_iso_projection.dot(self.matrix_plot)
            matrix = self.matrix_plot.dot(Vector.last_iso_projection)
            return matrix.dot(Vector.project_plane_matrix)

    def plot(self):
        if self.vector_set.__len__() < self.all_vectors.__len__() != 0:
            not_selected = self.xy_vectors_toplot(self.all_vectors)
            self.plot_dxf.updateData(
                not_selected[:, 0],
                not_selected[:, 1],
                connect="pairs")
        else:
            self.plot_dxf.setData([], [])
        return

    def plot_select(self):
        # selection = xy_vectors_toplot([vector for vector in self.all_vectors if vector.selected is True])
        if self.vector_set.__len__() > 0:
            selection = self.xy_vectors_toplot(list(self.vector_set))
            self.plot_selected.updateData(
                selection[:, 0],
                selection[:, 1],
                pen=pg.mkPen(color=QtGui.QColor(255, 255, 0, 200), width=5),
                connect="pairs")
        else:
            self.plot_selected.setData([], [])

    def check_point(self, cursor):
        if cursor.button() == 1:
            try:
                _maped_pos = self.plot_dxf.mapFromScene(cursor.pos())
                _x_ = _maped_pos.x()
                _y_ = _maped_pos.y()
                pixelsize = self.viewbox.viewPixelSize()
            except AttributeError:
                return

            for vector in self.all_vectors:
                start = vector.start_2d
                end = vector.end_2d
                point_toline_mindist = dist(start[0], start[1], end[0], end[1], _x_, _y_)

                if point_toline_mindist < pixelsize[0] * 15:
                    vector.clicked()
                    if vector.selected:
                        self.vector_set.add(vector)
                    else:
                        self.vector_set.remove(vector)

                    self.plot()
                    self.plot_select()
                    return
                else:
                    pass
        else:
            print("right click")

    def atm_rot(self, direction):

        if direction == QtCore.Qt.Key_Up:
            Vector.alpha += 0.1
        elif direction == QtCore.Qt.Key_Down:
            Vector.alpha -= 0.1
        elif direction == QtCore.Qt.Key_Left:
            Vector.beta -= 0.1
        elif direction == QtCore.Qt.Key_Right:
            Vector.beta += 0.1

        Vector.iso_projection()
        self.plot()
        self.plot_select()
        # self.graphics.enableAutoRange(True)

    def _cursor(self, cursor):
        maped_pos = self.plot_dxf.mapFromScene(cursor)
        x_ = maped_pos.x()
        y_ = maped_pos.y()
        self.vLine.setPos(x_)
        self.hLine.setPos(y_)
        return
