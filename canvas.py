import tkinter as tk
from canvasmixin import CanvasMixin
from eventmixin import EventMixin
from schemaui import SchemaUI
from matrixui import MatrixUI
from connectorui import ConnectorUI


class Canvas(CanvasMixin, EventMixin, tk.Canvas):
    def __init__(self, parent, width, bg_color):
        super().__init__(parent, width=width, bg=bg_color)
        self.click_listen(self.click_handler)
        self.select_flag = False
        self.parent = parent

        self.listen('OnSelect', self.schemas_listner)
        self.collect = {}

    def add(self, schema, schema_ui):
        self.collect.update({schema.uid: {'schema': schema, 'schema_ui': schema_ui}})

    def schemas_listner(self, uid):
        self.select_flag = True
        self.unselect(uid)

    def click_handler(self, e):
        if not self.select_flag:
            self.unselect()
            self.emit('OnUnSelect', None)
        else:
            self.select_flag = False

    def unselect(self, uid_selected=''):
        for uid, elem in self.collect.items():
            if uid != uid_selected:
                elem['schema_ui'].unselect()

    def schema(self, schema, coords):
        new_schema_ui = SchemaUI(self, schema, coords, 0)
        self.add(schema, new_schema_ui)
        return new_schema_ui

    def matrix(self, matrix, coords):
        new_matrix_ui = MatrixUI(self, matrix, coords, 0)
        self.add(matrix, new_matrix_ui)
        return new_matrix_ui

    def connections(self):
        connectors_ui = []
        for uid, elem in self.collect.items():
            schema = elem['schema']
            schema_from_ui = elem['schema_ui']
            for schema_to_uid in schema.connector.schema_binds():
                schema_to_ui = self.collect[schema_to_uid]['schema_ui']
                connections = schema.connector.raw(schema_to_uid)
                connectors_ui.append(ConnectorUI(self, schema_from_ui, schema_to_ui, connections))
        return connectors_ui
