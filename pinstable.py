import tkinter as tk
from pinedit import PinEdit


class PinsTable(tk.LabelFrame):
    def __init__(self, parent, width):
        super().__init__(parent, width=width)
        self.selected_schema = None
        self.collect = []
        self.in_pin_vals = {}
        self.parent = parent

    def set(self, new_selected_schema):
        # if self.selected_schema and new_selected_schema.uid == self.selected_schema.uid:
        #    return

        if self.collect:
            self.clear()

        self.collect = [[], [], [], []]
        self.selected_schema = new_selected_schema
        name = self.selected_schema.name
        ins, outs = self.selected_schema.ins, self.selected_schema.outs

        # label = tk.Label(self, text=name)
        # self.collect[0].append(label)
        # label.grid(column=0, row=0, columnspan=4)
        self.config(text=name)

        label = tk.Label(self, text='Inputs')
        self.collect[0].append(label)
        label.grid(column=0, row=1, columnspan=2)
        self.refresh()

    def refresh(self):
        i = 2
        ins, outs = self.selected_schema.ins, self.selected_schema.outs
        for k, v in ins.items():
            label = tk.Label(self, text=k)
            label.grid(column=0, row=i)
            self.collect[0].append(label)

            edit = PinEdit(self, k, v)
            edit.grid(column=1, row=i)
            self.collect[1].append(edit)
            self.in_pin_vals.update({k: edit})
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

    def get_in(self, pin):
        return self.in_pin_vals.get(pin)

    def clear(self):
        for col in self.collect:
            for row in col:
                row.destroy()
        self.in_pin_vals = {}
        self.collect = []
