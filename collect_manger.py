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

        self.in_connects = {  # example
            'uid-2': ['uid-1', 'uid-3'],
            'uid-3': ['uid-2'],
        }
        self.ins = {}
        self.in_connects = {}

    def add(self, schema):
        self.collect.update({schema.uid: schema})
        self.visited.update({schema.uid: False})
        self.in_connects.update({schema.uid: []})
        return schema.uid

    def set_ins(self, schema, ins, soft=False):
        if self.ins.get(schema.uid):
            if not soft:
                self.ins[schema.uid].update(ins)
            else:
                for pin, v in ins.items():
                    if not self.ins[schema.uid].get(pin):
                        self.ins[pin] = v
        else:
            self.ins.update({schema.uid: ins})

    def remove(self, schema):
        self.collect.pop(schema.uid, None)
        self.visited.pop(schema.uid, None)
        self.in_connects.pop(schema.uid, None)
        return schema.uid

    def step(self, schema_cur, logs=False, back=False):
        if not self.collect.get(schema_cur.uid):
            return

        for schema_from_uid in self.in_connects[schema_cur.uid]:
            if not self.visited[schema_from_uid]:
                self.step(self.collect[schema_from_uid], logs, True)

        self.visited[schema_cur.uid] = True
        schema_cur.ins = self.ins[schema_cur.uid]
        schema_cur.f()
        outs = schema_cur.outs

        if logs:
            self.log(1, schema_cur.code, schema_cur.uid, schema_cur.ins, outs)

        if schema_cur.connector.empty():
            return

        connector = schema_cur.connector
        for schema_to_uid in connector.schema_binds():
            if self.collect.get(schema_to_uid):
                new_ins = {}
                out_pins = connector.pins_from(schema_to_uid)
                in_pins = connector.pins_to(schema_to_uid)
                for i in range(len(out_pins)):
                    new_ins.update({in_pins[i]: outs[out_pins[i]]})
                self.set_ins(self.collect[schema_to_uid], new_ins)
                if logs:
                    self.log(2, schema_cur.uid, schema_to_uid, connector.raw(schema_to_uid))
                if not back:
                    self.step(self.collect[schema_to_uid], logs, False)

    def init(self):
        self.visited = {uid: False for uid in self.visited.keys()}
        # set in_collects
        for uid in self.in_connects.keys():
            self.in_connects[uid] = []
        for schema_from in self.collect.values():
            for schema_to_uid in schema_from.connector.schema_binds():
                self.in_connects[schema_to_uid].append(schema_from.uid)

    def execute(self, start_schema, logs=False, back=False):
        self.init()
        self.step(start_schema, logs, back)
