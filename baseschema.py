class BaseSchema(object):
    def __init__(self):
        self.name = 'default'
        self.ins = []
        self.outs = []

        self.io_params = self.io_params or {}
        self.io_params['count'] = self.io_params.get('count') or [0, 0]  # required!
        self.io_params['digital'] = self.io_params.get('digital') or [True, True]

        self.ins = [0 for i in range(self.io_params['count'][0])]
        self.outs = [0 for i in range(self.io_params['count'][1])]

    def f(self, _in):
        pass