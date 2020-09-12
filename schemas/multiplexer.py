from schemas.baseschema import BaseSchema


class Schema(BaseSchema):
    def __init__(self):
        super().__init__()
        self.name = 'Multiplexer'
        self.code = 'MS'
        self.io_settings = {
            'names': [
                ['A1', 'A2', 'A3', 'X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7'],
                ['Y'],
            ]
        }
        self.post_init()

    def f(self):
        self.outs['Y'] = int(not self.ins['A1'] and not self.ins['A2'] and not self.ins['A3'] and self.ins['X0'] \
            or not self.ins['A1'] and not self.ins['A2'] and self.ins['A3'] and self.ins['X1'] \
            or not self.ins['A1'] and self.ins['A2'] and not self.ins['A3'] and self.ins['X2'] \
            or not self.ins['A1'] and self.ins['A2'] and self.ins['A3'] and self.ins['X3'] \
            or self.ins['A1'] and not self.ins['A2'] and not self.ins['A3'] and self.ins['X4'] \
            or self.ins['A1'] and not self.ins['A2'] and self.ins['A3'] and self.ins['X5'] \
            or self.ins['A1'] and self.ins['A2'] and not self.ins['A3'] and self.ins['X6'] \
            or self.ins['A1'] and self.ins['A2'] and self.ins['A3'] and self.ins['X7'])
