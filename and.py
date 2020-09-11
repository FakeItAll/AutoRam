from baseschema import BaseSchema


class Schema(BaseSchema):
    def __init__(self):
        self.name = 'And'
        self.code = 'AND'
        self.io_settings = {
            'count': [2, 1],
            'pins': {
                'in_names': ['I1', 'I2'],
                'out_names': ['RES'],
            }
        }
        super().__init__()

    def f(self):
        super().validate()
        self.outs['RES'] = int(self.ins['I1'] and self.ins['I2'])
