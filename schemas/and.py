from schemas.baseschema import BaseSchema


class Schema(BaseSchema):
    def __init__(self):
        super().__init__()
        self.name = 'And'
        self.code = 'AND'
        self.io_settings = {
            'names': [
                ['X1', 'X2'],
                ['Y']
            ]
        }
        self.set_default_values()

    def f(self):
        self.outs['Y'] = int(self.ins['X1'] and self.ins['X2'])
