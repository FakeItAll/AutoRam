from schemas.baseschema import BaseSchema


class Schema(BaseSchema):
    def __init__(self):
        super().__init__()
        self.name = 'Decryptor'
        self.code = 'DC'
        self.io_settings = {
            'names': [
                ['A0', 'A1', 'A2'],
                ['Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7'],
            ]
        }
        self.post_init()

    def f(self):
        self.outs['Y0'] = int(not self.ins['A0'] and not self.ins['A1'] and not self.ins['A2'])
        self.outs['Y1'] = int(not self.ins['A0'] and not self.ins['A1'] and self.ins['A2'])
        self.outs['Y2'] = int(not self.ins['A0'] and self.ins['A1'] and not self.ins['A2'])
        self.outs['Y3'] = int(not self.ins['A0'] and self.ins['A1'] and self.ins['A2'])
        self.outs['Y4'] = int(self.ins['A0'] and not self.ins['A1'] and not self.ins['A2'])
        self.outs['Y5'] = int(self.ins['A0'] and not self.ins['A1'] and self.ins['A2'])
        self.outs['Y6'] = int(self.ins['A0'] and self.ins['A1'] and not self.ins['A2'])
        self.outs['Y7'] = int(self.ins['A0'] and self.ins['A1'] and self.ins['A2'])
