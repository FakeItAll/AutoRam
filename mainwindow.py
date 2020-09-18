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

        self.init_width = 1200
        self.init_height = 600
        self.geometry([self.init_width, self.init_height, 100, 100])

        canvas_width = self.init_width * 2 // 3
        canvas_color = '#DBF'
        self.canvas = Canvas(self, canvas_width, canvas_color)
        self.canvas.pack(side='left', fill=tk.Y)

        self.execute_panel = ExecutePanel(self, self.init_width - canvas_width, 100)
        self.execute_panel.pack(side='top', ipadx=5, ipady=10, pady=5)

        self.pinstable = PinsTable(self, self.init_width - canvas_width)

        self.collect_manager = collect_manager

        self.listen('OnSelect', self.select_handler)
        self.listen('OnUnSelect', self.unselect_handler)
        self.listen('OnRun', self.run_handler)
        self.listen('OnClear', self.clear_handler)
        self.listen('OnChange', self.change_handler)

    def select_handler(self, uid):
        schema = self.collect_manager.get(uid)
        self.pinstable.pack(side='top', ipadx=5, ipady=10, pady=5)
        self.pinstable.set(schema)

    def unselect_handler(self, e):
        self.pinstable.pack_forget()
        self.pinstable.clear()

    def run_handler(self, e):
        self.collect_manager.execute()
        self.pinstable.refresh()

    def clear_handler(self, e):
        self.collect_manager.clear()
        self.pinstable.refresh()

    def change_handler(self, e):
        print('change')
        e = self.serialize(e)
        print(e)
        schema = self.pinstable.selected_schema
        pin, val = e
        self.collect_manager.set_base_ins(schema, {pin: val})

    def geometry(self, params):
        super().geometry('{}x{}+{}+{}'.format(*params))

    def serialize(self, str):
        return json.loads(str.replace("'", "\""))

    def execute(self):
        self.mainloop()
