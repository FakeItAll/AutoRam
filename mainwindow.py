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

        self.init_width = 1100
        self.init_height = 600
        self.geometry([self.init_width, self.init_height, 100, 100])

        canvas_width = self.init_width * 2 // 3
        canvas_color = '#DBF'
        self.canvas = Canvas(self, canvas_width, canvas_color)
        self.canvas.pack(side='left', fill=tk.Y)

        self.execute_panel = ExecutePanel(self, self.init_width - canvas_width, 100)
        self.execute_panel.pack(side='top', pady=5)

        self.pinstable = PinsTable(self, self.init_width - canvas_width)

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
        return [ins, outs, schema.name]

    def select_handler(self, uid):
        self.selected_uid = uid
        self.pinstable.pack(side='top', pady=5)
        self.pinstable.set(*self.get_selected_data())

    def unselect_handler(self, e):
        self.pinstable.pack_forget()
        self.pinstable.clear()
        self.selected_uid = ''

    def run_handler(self, e):
        self.collect_manager.execute(self.logs)
        if self.selected_uid:
            self.pinstable.refresh(*self.get_selected_data())

    def clear_handler(self, e):
        self.collect_manager.clear()
        if self.selected_uid:
            self.pinstable.refresh(*self.get_selected_data())

    def change_handler(self, e):
        pin_val = self.serialize(e)
        schema = self.collect_manager.get(self.selected_uid)
        pin, val = pin_val
        self.collect_manager.set_base_ins(schema, {pin: val})

    def geometry(self, params):
        super().geometry('{}x{}+{}+{}'.format(*params))

    def serialize(self, str):
        return json.loads(str.replace("'", "\""))

    def execute(self):
        self.mainloop()
