import importlib


class Loader(object):
    def __init__(self, dir):
        self.dir = dir

    def load(self, name):
        path = self.dir + name
        module = importlib.import_module(path)
        return module.Schema()

