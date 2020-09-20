import tkinter as tk
import tkinter.ttk as ttk
from views.mixins.windowmixin import WindowMixin


class ReferenceWindow(WindowMixin, tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('References')
        self.geometry([600, 400, 100, 100])
