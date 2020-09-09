from baseschema import BaseSchema


class Schema(BaseSchema):
    def __init__(self):
        self.name = 'Decryptor'
        self.outs = [0]
        self.io_params = {
            'count': [3, 8]
        }
        super().__init__()

    def f(self):
        self.outs[0] = not self.ins[0] and not self.ins[1] and not self.ins[2]
        self.outs[1] = not self.ins[0] and not self.ins[1] and self.ins[2]
        self.outs[2] = not self.ins[0] and self.ins[1] and not self.ins[2]
        self.outs[3] = not self.ins[0] and self.ins[1] and self.ins[2]
        self.outs[4] = self.ins[0] and not self.ins[1] and not self.ins[2]
        self.outs[5] = self.ins[0] and not self.ins[1] and self.ins[2]
        self.outs[6] = self.ins[0] and self.ins[1] and not self.ins[2]
        self.outs[7] = self.ins[0] and self.ins[1] and self.ins[2]