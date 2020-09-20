import importlib.util as imp_util


class Loader(object):
    def __init__(self, dir=''):
        self.dir = dir
        self.modules = {}

    def load_schema(self, module_name):
        if self.modules.get(module_name):
            module = self.modules[module_name]
        else:
            if self.dir:
                path = self.dir + module_name + '.py'
                module_spec = imp_util.spec_from_file_location(module_name, path)
            else:
                path = module_name
                module_spec = imp_util.find_spec(module_name)

            try:
                module = imp_util.module_from_spec(module_spec)
                module_spec.loader.exec_module(module)
            except Exception:
                raise ImportError('Модуль {} не найден'.format(path))
                return None
            self.modules.update({module_name: module})

        schema = module.Schema()
        return schema

    def clear_cache(self):
        self.modules.clear()

