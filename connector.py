class Connector(object):
    def __init__(self, schema_from):
        self.schema_from = schema_from
        self.schemas_to = {}

    def add(self, schema_to, connections):
        connections = connections or {'OUT1': 'IN1', 'OUT2': 'IN2'}  # example
        if self.schemas_to.get(schema_to.uid):
            self.schemas_to[schema_to.uid].update(connections)
        else:
            self.schemas_to.update({schema_to.uid: connections})

    def remove(self, schema_to):
        self.schemas_to.pop(schema_to.uid, None)
