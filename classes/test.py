from datetime import datetime
from importlib import import_module
from Model.classes.buffer import Buffer


class Analysis:
    Buff = Buffer

    def __init__(self, name):
        self.name = str(name)
        self.buffers = set()
        self.datetime = str(datetime.now())
        self.method = None

    def create_solo_buffer(self, buffer_id):

        try:
            _name = "id_" + str(buffer_id)
            setattr(self, _name, self.Buff(buffer_id))
            self.buffers.add(getattr(self, _name))
            return True

        except AttributeError:
            return False

        except TypeError:
            return False

    def read_dxf(self, file):

        # for line in file:
        # get_data(line)
        pass

    def read_json(self, file):
        pass

    def read_python(self, file):
        try:
            import_module(file)
            return True
        except FileNotFoundError:
            print('archivo no encontrado')
            return False

    def run(self):
        pass
