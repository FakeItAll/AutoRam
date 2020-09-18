from schemas.baseschema import BaseSchema


class Schema(BaseSchema):
    def __init__(self):
        super().__init__()
        self.name = 'Multiplexer'
        self.code = 'MS'
        self.io_settings = {
            'names': [
                ['X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'A0', 'A1', 'A2'],
                ['Y'],
            ]
        }
        self.set_default_values()

    def f(self):
        self.outs['Y'] = int(not self.ins['A0'] and not self.ins['A1'] and not self.ins['A2'] and self.ins['X0'] \
            or self.ins['A0'] and not self.ins['A1'] and not self.ins['A2'] and self.ins['X1'] \
            or not self.ins['A0'] and self.ins['A1'] and not self.ins['A2'] and self.ins['X2'] \
            or self.ins['A0'] and self.ins['A1'] and not self.ins['A2'] and self.ins['X3'] \
            or not self.ins['A0'] and not self.ins['A1'] and self.ins['A2'] and self.ins['X4'] \
            or self.ins['A0'] and not self.ins['A1'] and self.ins['A2'] and self.ins['X5'] \
            or not self.ins['A0'] and self.ins['A1'] and self.ins['A2'] and self.ins['X6'] \
            or self.ins['A0'] and self.ins['A1'] and self.ins['A2'] and self.ins['X7'])
