import importlib.util as imp_util


class Loader(object):
    def __init__(self, dir=''):
        self.dir = dir
        self.modules = {}

    def load_schema(self, name):
        if self.modules.get(name):
            return self.modules[name].Schema()

        if self.dir:
            path = self.dir + name + '.py'
            module_spec = imp_util.spec_from_file_location(name, path)
        else:
            module_spec = imp_util.find_spec(name)

        if not module_spec:
            print('Module {} not found!'.format(name))
            return None

        module = imp_util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)

        self.modules.update({name: module})
        schema = module.Schema()
        return schema

    def clear_cache(self):
        self.modules.clear()

