from abc import abstractmethod
from models.connector import Connector


class BaseSchema(object):
    uid_counter = 0

    @staticmethod
    def generate_uid():
        BaseSchema.uid_counter += 1
        prefix = 'schuid-'
        hash = BaseSchema.uid_counter
        postfix = ''
        return '{}{}{}'.format(prefix, hash, postfix)

    def __init__(self):
        self.name = 'default'
        self.code = 'DEFAULT'
        self._ins = {}
        self._outs = {}

        self.io_settings = {
            'count': [],
            'names': []
        }

        self.connector = Connector()
        self.uid = self.generate_uid()

    def set_default_values(self):
        if self.io_settings.get('names'):
            keys = self.io_settings['names'][0]
            self._ins = {k: 0 for k in keys}
            keys = self.io_settings['names'][1]
            self._outs = {k: 0 for k in keys}
        else:
            self._ins = {i: 0 for i in range(self.io_settings['count'][0])}
            self._outs = {i: 0 for i in range(self.io_settings['count'][1])}

    @property
    def ins(self):
        return self._ins

    @ins.setter
    def ins(self, vals):
        for k, v in vals.items():
            self._ins[k] = v

    @property
    def outs(self):
        return self._outs

    @abstractmethod
    def f(self):
        pass
