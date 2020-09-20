class CollectManager(object):
    @staticmethod
    def log(log_id, *log_data):
        if log_id == 1:
            print('{} ({}): {} => {}'.format(*log_data))
        elif log_id == 2:
            print('{} => {}: {}'.format(*log_data))
        print()

    def __init__(self, base_schema=None):
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
        self.in_connects = {}

        self.base_ins = {}
        self.base_schema = base_schema
        if base_schema:
            self.add(base_schema)

        self.iter_step_counter = 0
        self.iter_next_step = {}

    def items(self):
        return self.collect.items()

    def get(self, uid):
        return self.collect.get(uid)

    def add(self, schema):
        self.collect.update({schema.uid: schema})
        self.visited.update({schema.uid: False})
        self.in_connects.update({schema.uid: []})
        return schema.uid

    def set_base_ins(self, schema, ins, soft=False):
        if self.base_ins.get(schema.uid):
            if not soft:
                for pin, v in ins.items():
                    self.base_ins[schema.uid][pin] = v
            else:
                for pin, v in ins.items():
                    if not self.base_ins[schema.uid].get(pin):
                        self.base_ins[schema.uid][pin] = v
        else:
            self.base_ins.update({schema.uid: ins})

    def get_base_ins(self, schema):
        return self.base_ins[schema.uid]

    def get_ins(self, schema):
        res_ins = {}
        for pin, val in schema.ins.items():
            if self.base_ins.get(schema.uid):
                base_val = self.base_ins[schema.uid].get(pin)
                res_ins.update({pin: base_val or val})
            else:
                res_ins.update({pin: val})
        return res_ins

    def get_outs(self, schema):
        return schema.outs

    def clear_base_ins(self, schema):
        self.base_ins.pop(schema.uid, None)

    def remove(self, schema):
        self.collect.pop(schema.uid, None)
        self.visited.pop(schema.uid, None)
        self.in_connects.pop(schema.uid, None)
        return schema.uid

    def set_base_schema(self, schema):
        if not self.collect.get(schema.uid):
            self.add(schema)
        self.base_schema = schema

    def init(self):
        self.iter_step_counter = 0
        self.visited = {uid: False for uid in self.visited.keys()}
        # set in_collects
        for uid in self.in_connects.keys():
            self.in_connects[uid] = []
        for schema_from in self.collect.values():
            for schema_to_uid in schema_from.connector.schema_binds():
                self.in_connects[schema_to_uid].append(schema_from.uid)
        for schema in self.collect.values():
            schema.set_default_values()

    def iter(self, schema_cur, back=False, logs=False):
        if not self.collect.get(schema_cur.uid):
            return

        for schema_from_uid in self.in_connects[schema_cur.uid]:
            if not self.visited[schema_from_uid]:
                self.iter(self.collect[schema_from_uid], True, logs)

        self.visited[schema_cur.uid] = True
        schema_cur.ins = self.base_ins.get(schema_cur.uid) or schema_cur.ins
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

                self.collect[schema_to_uid].ins = new_ins

                if logs:
                    self.log(2, schema_cur.uid, schema_to_uid, connector.raw(schema_to_uid))
                if not back:
                    self.iter(self.collect[schema_to_uid], False, logs)

    def clear(self):
        for schema in self.collect.values():
            self.clear_base_ins(schema)
            schema.set_default_values()

    def execute(self, logs=False):
        self.init()
        self.iter(self.base_schema, False, logs)
