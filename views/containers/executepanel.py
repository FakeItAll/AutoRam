from views.mixins.eventmixin import EventMixin
import tkinter as tk


class ExecutePanel(EventMixin, tk.LabelFrame):
    def __init__(self, parent, width, height):
        super().__init__(parent, text='ExecutePanel', width=width, height=height, padx=5, pady=10)
        self.run_button = tk.Button(self, text='Run', command=self.run)
        self.clear_button = tk.Button(self, text='Clear', command=self.clear)

        self.run_button.pack(side='left', padx=10, ipadx=20)
        self.clear_button.pack(side='left', padx=10, ipadx=20)
        self.parent = parent

    def run(self):
        self.emit('OnRun', None)

    def clear(self):
        self.emit('OnClear', None)

