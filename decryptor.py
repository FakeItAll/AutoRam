from baseschema import BaseSchema


class Schema(BaseSchema):
    def __init__(self):
        self.name = 'Decryptor'
        self.code = 'DC'
        self.io_settings = {
            'count': [3, 8]
        }
        super().__init__()

    def f(self):
        super().validate()
        self.outs[0] = int(not self.ins[0] and not self.ins[1] and not self.ins[2])
        self.outs[1] = int(not self.ins[0] and not self.ins[1] and self.ins[2])
        self.outs[2] = int(not self.ins[0] and self.ins[1] and not self.ins[2])
        self.outs[3] = int(not self.ins[0] and self.ins[1] and self.ins[2])
        self.outs[4] = int(self.ins[0] and not self.ins[1] and not self.ins[2])
        self.outs[5] = int(self.ins[0] and not self.ins[1] and self.ins[2])
        self.outs[6] = int(self.ins[0] and self.ins[1] and not self.ins[2])
        self.outs[7] = int(self.ins[0] and self.ins[1] and self.ins[2])
