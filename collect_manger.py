class CollectManager(object):
    def __init__(self):
        self.collect = []
        self.connects = {
            0: [{0: 0}],
            1: [{0: 0}, {1: 1}]
        }
        self.pointer = 0

    def add(self, schema):
        self.collect.append(schema)

    def connect(self, pairs, level):
        if self.connects.get(level):
            self.connects[level].append(pairs)
        else:
            self.connects = {level: pairs}

    def execute(self, ins):
        while self.pointer < len(self.collect):
            schema = self.collect[self.pointer]
            self.pointer += 1
