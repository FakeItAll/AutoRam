class CollectManager(object):
    @staticmethod
    def log(log_id, *log_data):
        if log_id == 1:
            print('{} ({}): {} => {}'.format(*log_data))
        elif log_id == 2:
            print('{} => {}: {}'.format(*log_data))
        print()

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

    def remove(self, schema):
        self.collect.pop(schema.uid, None)
        self.visited.pop(schema.uid, None)
        return schema.uid

    def step(self, schema_cur, ins, logs):
        if not self.collect.get(schema_cur.uid):
            return

        self.visited[schema_cur.uid] = True
        schema_cur.ins = ins
        schema_cur.f()
        outs = schema_cur.outs

        if logs:
            self.log(1, schema_cur.code, schema_cur.uid, ins, outs)

        if schema_cur.connector.empty():
            return

        connector = schema_cur.connector
        for schema_to_uid in connector.schema_binds():
            new_ins = {}
            out_pins = connector.pins_from(schema_to_uid)
            in_pins = connector.pins_to(schema_to_uid)
            for i in range(len(out_pins)):
                new_ins.update({in_pins[i]: outs[out_pins[i]]})
            if self.collect.get(schema_to_uid):
                if logs:
                    self.log(2, schema_cur.uid, schema_to_uid, connector.raw(schema_to_uid))
                self.step(self.collect[schema_to_uid], new_ins, logs)

    def clean(self):
        self.visited = {uid: False for uid in self.visited.keys()}

    def execute(self, start_schema, ins, logs=False):
        self.clean()
        self.step(start_schema, ins, logs)
