from abc import abstractmethod


class BaseSchema(object):
    uid_counter = 0

    @staticmethod
    def generate_uid():
        BaseSchema.uid_counter += 1
        prexif = 'schuid-'
        uhash = BaseSchema.uid_counter
        postfix = ''
        return '{}{}{}'.format(prexif, uhash, postfix)

    def __init__(self):
        self.uid = self.generate_uid()
        self.name = self.name or 'default'
        self.code = self.code or 'DEFAULT'
        self.ins = {}
        self.outs = {}

        self.io_settings = self.io_settings or {}
        self.io_settings['count'] = self.io_settings.get('count') or [0, 0]  # required
        self.io_settings['digital'] = self.io_settings.get('digital') or [True, True]
        self.io_settings['pins'] = self.io_settings.get('pins') or {}

        if self.io_settings['pins'].get('in_names'):
            keys = self.io_settings['pins']['in_names']
            self.ins = {k: 0 for k in keys}
        else:
            self.ins = {i: 0 for i in range(self.io_settings['count'][0])}

        if self.io_settings['pins'].get('out_names'):
            keys = self.io_settings['pins']['out_names']
            self.outs = {k: 0 for k in keys}
        else:
            self.outs = {i: 0 for i in range(self.io_settings['count'][1])}

    @abstractmethod
    def f(self):
        pass
