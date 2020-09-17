import tkinter as tk
from pinedit import PinEdit


class PinsTable(tk.Frame):
    def __init__(self, parent, width):
        super().__init__(parent, width=width)
        self.pack(side='left', fill=tk.Y)
        self.collect = []

    def set(self, name, ins, outs):
        if self.collect:
            self.clear()
        self.collect = [[], [], [], []]

        label = tk.Label(self, text=name)
        self.collect[0].append(label)
        label.grid(column=0, row=0, columnspan=4)

        label = tk.Label(self, text='Inputs')
        self.collect[0].append(label)
        label.grid(column=0, row=1, columnspan=2)
        i = 2
        for k, v in ins.items():
            label = tk.Label(self, text=k)
            label.grid(column=0, row=i)
            self.collect[0].append(label)

            edit = PinEdit(self, v)
            edit.grid(column=1, row=i)
            self.collect[1].append(edit)
            i += 1

        label = tk.Label(self, text='Outputs')
        self.collect[2].append(label)
        label.grid(column=2, row=1, columnspan=2)
        i = 2
        for k, v in outs.items():
            label = tk.Label(self, text=k)
            label.grid(column=2, row=i)
            self.collect[2].append(label)

            edit = PinEdit(self, v)
            edit.grid(column=3, row=i)
            self.collect[3].append(edit)
            i += 1

    def clear(self):
        for col in self.collect:
            for row in col:
                row.destroy()
        self.collect = []
