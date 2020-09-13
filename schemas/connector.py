class Connector(object):
    def __init__(self):
        self.schemas_to = {  # example
            'schuid-1': {'OUT1': 'IN1', 'OUT2': 'IN2'},
            'schuid-2': {'OUT3': 'IN1', 'OUT4': 'IN2'},
        }
        self.schemas_to = {}

    def add(self, schema_to, connections):
        if self.schemas_to.get(schema_to.uid):
            self.schemas_to[schema_to.uid].update(connections)
        else:
            self.schemas_to.update({schema_to.uid: connections})

    def remove(self, schema_to):
        self.schemas_to.pop(schema_to.uid, None)

    def empty(self):
        return not self.schemas_to

    def schema_binds(self):
        return list(self.schemas_to.keys())

    def pins_from(self, schema_to_uid):
        return list(self.schemas_to[schema_to_uid].keys())

    def pins_to(self, schema_to_uid):
        return list(self.schemas_to[schema_to_uid].values())

    def raw(self, schema_to_uid):
        return self.schemas_to.get(schema_to_uid)
