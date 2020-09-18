import tkinter as tk
from eventmixin import EventMixin


class PinEdit(EventMixin, tk.Spinbox):
    def valid(self, value):
        if value == '' or value == '0' or value == '1':
            if value == '0' or value == '1':
                print('valid ' + str(value))
                self.emit('OnChange', [self.pin, value])
            return True
        return False

    def __init__(self, parent, pin, val, is_active=True):
        self.parent = parent
        self.pin = pin
        self.val = tk.StringVar()
        self.set(val)
        vc = (parent.register(self.valid), "%P")
        super().__init__(parent,
                         textvariable=self.val,
                         from_=0,
                         to=1,
                         width=5,
                         state=tk.NORMAL if is_active else tk.DISABLED,
                         disabledforeground='#000')
        self.config(validate='all', validatecommand=vc)

    def set(self, val):
        self.val.set(val)

    def get(self):
        return self.val.get()
