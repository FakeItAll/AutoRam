from baseschema import BaseSchema


class Schema(BaseSchema):
    def __init__(self):
        super().__init__()
        self.name = 'Or'
        self.code = 'OR'
        self.io_settings = {
            'names': [
                ['I1', 'I2'],
                ['RES']
            ]
        }
        self.post_init()

    def f(self):
        self._outs['RES'] = int(self._ins['I1'] or self._ins['I2'])
