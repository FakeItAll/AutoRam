from baseschema import BaseSchema


class Schema(BaseSchema):
    def __init__(self):
        super().__init__()
        self.name = 'And'
        self.code = 'AND'
        self.io_settings = {
            'names': [
                ['I1', 'I2'],
                ['RES']
            ]
        }
        self.post_init()

    def f(self):
        self.outs['RES'] = int(self.ins['I1'] and self.ins['I2'])
