from baseschema import BaseSchema


class Schema(BaseSchema):
    def __init__(self):
        self.name = 'And'
        self.code = 'AND'
        self.io_settings = {
            'count': [2, 1]
        }
        super().__init__()

    def f(self):
        super().validate()
        self.outs[0] = int(self.ins[0] and self.ins[1])
