class CollectManager(object):
    @staticmethod
    def log(*log_data):
        print('{} ({}): {} => {}'.format(*log_data))

    def __init__(self):
        self.collect = {  # example
            'uid-1': object,
            'uid-2': object,
        }
        self.collect = {}

        self.visited = {  # example
            'uid-1': False,
            'uid-2': False,
        }
        self.visited = {}

        self.connects = {  # example
            'uid-1': {0: ['uid-2', 0]},
            'uid-2': {0: ['uid-3', 0], 1: ['uid-3', 1]}
        }
        self.connects = {}

    def add(self, schema):
        self.collect.update({schema.uid: schema})
        self.visited.update({schema.uid: False})
        return schema.uid

    def connect(self, all_connects):
        for schema_out_uid, schema_out_connects in all_connects.items():
            if self.connects.get(schema_out_uid):
                self.connects[schema_out_uid].update(schema_out_connects)
            else:
                self.connects.update({schema_out_uid: schema_out_connects})

    def step(self, uid, ins, logs):
        self.visited[uid] = True
        schema = self.collect[uid]
        schema.ins = ins
        schema.f()
        outs = schema.outs
        if logs:
            self.log(schema.code, schema.uid, ins, outs)

        if not self.connects.get(uid):
            return

        item_connects = self.connects[uid]
        schema_ins = []

        new_ins = {uid: {} for uid in schema_ins}
        for out_pin, schema_input in item_connects.items():
            input_uid = schema_input[0]
            if not self.visited[input_uid] and input_uid not in schema_ins:
                schema_ins.append(input_uid)
            in_pin = schema_input[1]
            if new_ins.get(input_uid):
                new_ins[input_uid].update({in_pin: outs[out_pin]})
            else:
                new_ins.update({input_uid: {in_pin: outs[out_pin]}})

        if not schema_ins:
            return

        for uid, ins in new_ins.items():
            self.step(uid, ins, logs)

    def clean(self):
        self.visited = {uid: False for uid in self.visited.keys()}

    def execute(self, start_uid, ins, logs=False):
        self.clean()
        self.step(start_uid, ins, logs)
