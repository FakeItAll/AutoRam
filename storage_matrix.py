from baseschema import BaseSchema


class Schema(BaseSchema):
    def __init__(self):
        super().__init__()
        self.name = 'Storage Matrix'
        self.code = ''
        self.io_settings = {
            'names': [
                ['Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7'],
                ['X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7'],
            ]
        }
        self.matrix = {
            'Y0': ['X0', 'X1'],
            'Y1': ['X7'],
            'Y6': ['X4', 'X5', 'X6'],
            'Y7': ['X1', 'X2', 'X3'],
        }
        self.post_init()

    def f(self):
        for row, cols in self.matrix.items():
            for col in cols:
                self.outs[col] |= self.ins[row]
