import importlib.util as imp_util


class Loader(object):
    uid_counter = 0

    @staticmethod
    def generate_uid():
        Loader.uid_counter += 1
        prexif = 'schid-'
        uhash = Loader.uid_counter
        postfix = ''
        return '{}{}{}'.format(prexif, uhash, postfix)

    def __init__(self, dir=''):
        self.dir = dir

    def load_schema(self, name):
        if self.dir:
            path = self.dir + name
            module_spec = imp_util.spec_from_file_location(name, path)  # not tested!
        else:
            module_spec = imp_util.find_spec(name)

        if not module_spec:
            print('Module {} not found!'.format(name))
            return None

        module = imp_util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)

        schema = module.Schema()
        schema.uid = self.generate_uid()
        return schema

