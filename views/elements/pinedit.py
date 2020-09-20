import tkinter as tk
from views.mixins.eventmixin import EventMixin


class PinEdit(EventMixin, tk.Spinbox):
    def __init__(self, parent, pin, val, is_active=True):
        self.parent = parent
        self.pin = pin
        self.val = tk.StringVar()

        self.font_normal = 'Arial 10'
        self.font_bold = 'Arial 10 bold'
        self.not_user_flag = False

        vc = (parent.register(self.valid), "%P")

        super().__init__(parent,
                         textvariable=self.val,
                         from_=0,
                         to=1,
                         width=5,
                         state=tk.NORMAL if is_active else tk.DISABLED,
                         disabledforeground='#000')
        self.set(val, False)
        self.config(validate='all', validatecommand=vc)

    def valid(self, value):
        if value == '' or value == '0' or value == '1':
            if value == '0' or value == '1':
                value = int(value)

                if self.not_user_flag:
                    self.not_user_flag = False
                elif value != self.get():
                    self.emit('OnChange', [self.pin, value])

                if value == 0:
                    self.set_font()
                else:
                    self.set_font(False)
            return True
        return False

    def set(self, val, user=True):
        if not user and val != self.get():
            self.not_user_flag = True
            self.val.set(val)
        if val == 0:
            self.set_font()
        elif val == 1:
            self.set_font(False)

    def get(self):
        return int(self.val.get())

    def set_font(self, normal=True):
        if normal:
            self.config(font=self.font_normal)
        else:
            self.config(font=self.font_bold)
