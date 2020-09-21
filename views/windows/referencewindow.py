import tkinter as tk
import tkinter.ttk as ttk
from views.frames.htmlviewer import HtmlViewer
from views.mixins.windowmixin import WindowMixin


class ReferenceWindow(WindowMixin, tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('References')
        self.init_width = 1000
        self.init_height = 800
        self.geometry([self.init_width, self.init_height, 100, 100])

        frame = HtmlViewer(self, self.init_width, self.init_height)
        frame.pack()
