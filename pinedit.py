import tkinter as tk


class PinEdit(tk.Spinbox):
    @staticmethod
    def valid(value):
        return value == '' or value == '0' or value == '1'

    def __init__(self, parent, val):
        self.val = tk.IntVar()
        self.val.set(val)
        vc = (parent.register(self.valid), "%P")
        super().__init__(parent,
                         textvariable=self.val,
                         validate='all',
                         validatecommand=vc,
                         from_=0,
                         to=1,
                         width=4)
