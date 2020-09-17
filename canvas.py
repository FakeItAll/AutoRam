import tkinter as tk
from canvasmixin import CanvasMixin
from eventmixin import EventMixin
from schemaui import SchemaUI


class Canvas(CanvasMixin, EventMixin, tk.Canvas):
    def __init__(self, parent, width, bg_color):
        super().__init__(parent, width=width, bg=bg_color)
        self.click_listen(self.click_handler)
        self.select_flag = False
        self.parent = parent

        self.listen('OnSelect', self.schemas_listner)
        self.schemas_ui = {}

    def schemas_listner(self, data):
        self.select_flag = True
        self.unselect(data)

    def click_handler(self, e):
        if not self.select_flag:
            self.unselect()
            self.emit('OnUnSelect', None)
        else:
            self.select_flag = False

    def unselect(self, key_selected=''):
        for key, obj in self.schemas_ui.items():
            if key != key_selected:
                obj.unselect()

    def schema(self, schema, coords):
        new_schema_ui = SchemaUI(self, schema, coords)
        self.schemas_ui.update({schema.uid: new_schema_ui})
