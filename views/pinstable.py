import tkinter as tk
from views.components.pinlabel import PinLabel
from views.components.pinedit import PinEdit


class PinsTable(tk.LabelFrame):
    def __init__(self, parent, width, height):
        super().__init__(parent, width=width, height=height, padx=30, pady=10)
        self.collect_header = {'ins': None, 'outs': None}
        self.collect_labels = {'ins': {}, 'outs': {}}
        self.collect_pins = {'ins': {}, 'outs': {}}
        self.base_pins = []
        self.parent = parent

    def select(self, ins, outs, base_ins, name):
        if self.collect_header['ins'] or self.collect_header['outs']:
            self.unselect()

        self.config(text=name)
        if base_ins:
            self.base_pins = list(base_ins.keys())

        label = tk.Label(self, text='Inputs')
        self.collect_header['ins'] = label
        label.grid(column=0, row=0, columnspan=2)

        label = tk.Label(self, text='Outputs')
        self.collect_header['outs'] = label
        label.grid(column=2, row=0, columnspan=2)
        self.create(ins, outs)

    def create(self, ins, outs):
        row = 1
        for pin, val in ins.items():
            label = PinLabel(self, pin, pin in self.base_pins)
            label.grid(column=0, row=row)
            self.collect_labels['ins'][pin] = label

            edit = PinEdit(self, pin, val)
            edit.grid(column=1, row=row)
            self.collect_pins['ins'][pin] = edit
            row += 1
        row = 1
        for pin, val in outs.items():
            label = PinLabel(self, pin)
            label.grid(column=2, row=row)
            self.collect_labels['outs'][pin] = label

            edit = PinEdit(self, pin, val, False)
            edit.grid(column=3, row=row)
            self.collect_pins['outs'][pin] = edit
            row += 1

    def refresh(self, ins, outs, base_ins, name=''):
        if base_ins:
            self.base_pins = list(base_ins.keys())
        for pin, val in ins.items():
            self.collect_labels['ins'][pin].set_base(pin in self.base_pins)

            self.collect_pins['ins'][pin].set(val, False)

        for pin, val in outs.items():
            self.collect_pins['outs'][pin].set(val, False)

    def unselect(self):
        if self.collect_header['ins'] or self.collect_header['outs']:
            self.collect_header['ins'].destroy()
            self.collect_header['outs'].destroy()

        for pin in self.collect_labels['ins'].keys():
            self.collect_labels['ins'][pin].destroy()
            self.collect_pins['ins'][pin].destroy()

        for pin in self.collect_labels['outs'].keys():
            self.collect_labels['outs'][pin].destroy()
            self.collect_pins['outs'][pin].destroy()

        self.collect_header = {'ins': None, 'outs': None}
        self.collect_labels = {'ins': {}, 'outs': {}}
        self.collect_pins = {'ins': {}, 'outs': {}}
        self.base_pins = []

    def clear(self):
        self.base_pins = []

    def set_base_pin(self, pin):
        if self.collect_labels['ins'].get(pin):
            self.base_pins.append(pin)
            self.collect_labels['ins'][pin].set_base()
