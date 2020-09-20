from views.mixins.eventmixin import EventMixin
import tkinter.ttk as ttk


class ExecutePanel(EventMixin, ttk.LabelFrame):
    def __init__(self, parent, width, height):
        super().__init__(parent, text='ExecutePanel', width=width, height=height, padding='10')
        self.run_button = ttk.Button(self, text='Run', width=5, command=self.run)
        self.clear_button = ttk.Button(self, text='Clear', width=5, command=self.clear)

        self.run_button.pack(side='left', padx=10, ipadx=20)
        self.clear_button.pack(side='left', padx=10, ipadx=20)
        self.parent = parent

    def run(self):
        self.emit('OnRun', None)

    def clear(self):
        self.emit('OnClear', None)

