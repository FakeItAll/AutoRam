import tkinter.ttk as ttk


class PinLabel(ttk.Label):
    def __init__(self, parent, text, base=False):
        super().__init__(parent, text=text)

        self.font_normal = 'Arial 10'
        self.font_bold = 'Arial 10 bold'
        self.set_base(base)

    def set_base(self, val=True):
        if not val:
            self.config(font=self.font_normal)
        else:
            self.config(font=self.font_bold)

