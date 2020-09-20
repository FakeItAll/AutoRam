import tkinter as tk
from canvas import Canvas
from pinstable import PinsTable
from executepanel import ExecutePanel
from eventmixin import EventMixin
import json


class MainWindow(EventMixin, tk.Tk):
    def __init__(self, collect_manager=None):
        super().__init__()
        self.title('AutoRAM')

        self.init_width = 1000
        self.init_height = 600
        self.geometry([self.init_width, self.init_height, 100, 100])

        canvas_width = self.init_width * 3 // 4
        canvas_height = self.init_height - 10

        self.canvas = Canvas(self, canvas_width, canvas_height)
        self.canvas.pack(side='left', fill=tk.Y)

        execute_panel_width = self.init_width - canvas_width
        execute_panel_height = 100

        self.execute_panel = ExecutePanel(self, execute_panel_width, execute_panel_height)
        self.execute_panel.pack(side='top', anchor='nw', padx=5, pady=5)

        pins_table_width = self.init_width - canvas_width
        pins_table_height = 0
        self.pins_table = PinsTable(self, pins_table_width, pins_table_height)

        self.collect_manager = collect_manager
        self.selected_uid = ''

        self.listen('OnSelect', self.select_handler)
        self.listen('OnUnSelect', self.unselect_handler)
        self.listen('OnRun', self.run_handler)
        self.listen('OnClear', self.clear_handler)
        self.listen('OnChange', self.change_handler)

        self.logs = True

    def get_selected_data(self):
        schema = self.collect_manager.get(self.selected_uid)
        ins = self.collect_manager.get_ins(schema)
        outs = self.collect_manager.get_outs(schema)
        base_ins = self.collect_manager.get_base_ins(schema)
        return [ins, outs, base_ins, schema.name]

    def select_handler(self, uid):
        self.selected_uid = uid
        self.pins_table.pack(side='top', anchor='nw', padx=5, pady=5)
        self.pins_table.select(*self.get_selected_data())

    def unselect_handler(self, e):
        self.pins_table.pack_forget()
        self.pins_table.unselect()
        self.selected_uid = ''

    def run_handler(self, e):
        self.collect_manager.execute(self.logs)
        if self.selected_uid:
            self.pins_table.refresh(*self.get_selected_data())

    def clear_handler(self, e):
        self.collect_manager.clear()
        if self.selected_uid:
            self.pins_table.clear()
            self.pins_table.refresh(*self.get_selected_data())

    def change_handler(self, e):
        pin_val = self.serialize(e)
        schema = self.collect_manager.get(self.selected_uid)
        pin, val = pin_val
        self.pins_table.set_base_pin(pin)
        self.collect_manager.set_base_ins(schema, {pin: val})

    def geometry(self, params):
        super().geometry('{}x{}+{}+{}'.format(*params))

    def serialize(self, str):
        return json.loads(str.replace("'", "\""))

    def execute(self):
        self.mainloop()
