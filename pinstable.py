import tkinter as tk
from pinedit import PinEdit


class PinsTable(tk.LabelFrame):
    def __init__(self, parent, width):
        super().__init__(parent, width=width, padx=34, pady=10)
        self.collect = []
        self.parent = parent

    def set(self, ins, outs, name):
        # if self.selected_schema and new_selected_schema.uid == self.selected_schema.uid:
        #    return

        if self.collect:
            self.clear()

        self.collect = [[], [], [], []]

        self.config(text=name)

        label = tk.Label(self, text='Inputs')
        self.collect[0].append(label)
        label.grid(column=0, row=1, columnspan=2)

        label = tk.Label(self, text='Outputs')
        self.collect[2].append(label)
        label.grid(column=2, row=1, columnspan=2)
        self.refresh(ins, outs)

    def refresh(self, ins, outs, name=''):
        i = 2
        for k, v in ins.items():
            label = tk.Label(self, text=k)
            label.grid(column=0, row=i)
            self.collect[0].append(label)

            edit = PinEdit(self, k, v)
            edit.grid(column=1, row=i)
            self.collect[1].append(edit)
            i += 1
        i = 2
        for k, v in outs.items():
            label = tk.Label(self, text=k)
            label.grid(column=2, row=i)
            self.collect[2].append(label)

            edit = PinEdit(self, k, v, False)
            edit.grid(column=3, row=i)
            self.collect[3].append(edit)
            i += 1

    def clear(self):
        for col in self.collect:
            for row in col:
                row.destroy()
        self.in_pin_vals = {}
        self.collect = []
