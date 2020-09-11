from baseschema import BaseSchema


class Schema(BaseSchema):
    def __init__(self):
        self.name = 'Decryptor'
        self.code = 'DC'
        self.io_settings = {
            'count': [3, 8],
            'pins': {
                'in_names': ['A', 'B', 'C'],
                'out_names': ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7'],
            }
        }
        super().__init__()

    def f(self):
        super().validate()
        self.outs['D0'] = int(not self.ins['A'] and not self.ins['B'] and not self.ins['C'])
        self.outs['D1'] = int(not self.ins['A'] and not self.ins['B'] and self.ins['C'])
        self.outs['D2'] = int(not self.ins['A'] and self.ins['B'] and not self.ins['C'])
        self.outs['D3'] = int(not self.ins['A'] and self.ins['B'] and self.ins['C'])
        self.outs['D4'] = int(self.ins['A'] and not self.ins['B'] and not self.ins['C'])
        self.outs['D5'] = int(self.ins['A'] and not self.ins['B'] and self.ins['C'])
        self.outs['D6'] = int(self.ins['A'] and self.ins['B'] and not self.ins['C'])
        self.outs['D7'] = int(self.ins['A'] and self.ins['B'] and self.ins['C'])
