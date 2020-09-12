class Schema(object):
    def __init__(self):
        super().__init__()
        self.name = 'Test'
        self.code = 'TEST'
        self.io_settings = {
            'names': [
                ['I1', 'I2'],
                ['RES']
            ]
        }
        # self.post_init()

    def f(self):
        self.outs['RES'] = int(self.ins['I1'] and self.ins['I2'])
