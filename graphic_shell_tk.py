import tkinter as tk


class GraphicShellTk(object):
    def __init__(self):
        self._window = tk.Tk()
        self.root = self._window
        self._canvas = None
        self.consts = {
            'center': tk.CENTER,
            'first': tk.FIRST,
            'last': tk.LAST,
            'font_lg': 'Arial 14',
            'font_sm': 'Arial 8',
        }

    def execute(self):
        self.window.mainloop()

    @property
    def window(self):
        return self._window

    @window.setter
    def window(self, val):
        self.window.title(val['title'])
        geometry = val['geometry']
        x, y, width, height = geometry[0], geometry[1], geometry[2], geometry[3]
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    @property
    def canvas(self):
        return self._canvas

    @canvas.setter
    def canvas(self, val):
        geometry = val['geometry']
        x, y, width, height = geometry[0], geometry[1], geometry[2], geometry[3]  # x, y todo
        frame = tk.Frame(master=self.window, width=width)
        frame.pack(side='left', fill=tk.Y)
        self._canvas = tk.Canvas(frame,
                                 width=width,
                                 height=height,
                                 bg=val['bg_color'])
        self._canvas.place(x=0, y=0)

    def rect(self, geometry, color='black'):
        return self.canvas.create_rectangle(*geometry)

    def line(self, geometry, color='black'):
        return self.canvas.create_line(*geometry,
                                       fill=color)

    def arrow(self, geometry, color='black'):
        return self.canvas.create_line(*geometry,
                                       fill=color,
                                       arrow=self.consts['last'])

    def arrow_f(self, geometry, color='black'):
        return self.canvas.create_line(*geometry,
                                       fill=color,
                                       arrow=self.consts['first'])

    def text_sm(self, geometry, text):
        return self.canvas.create_text(*geometry,
                                       text=text,
                                       justify=self.consts['center'],
                                       font=self.consts['font_sm'])

    def text_lg(self, geometry, text):
        return self.canvas.create_text(*geometry,
                                       text=text,
                                       justify=self.consts['center'],
                                       font=self.consts['font_lg'])

    def oval(self, geometry, color='blue'):
        return self.canvas.create_oval(*geometry, fill=color)

    def input_sm(self, geometry):
        entry = tk.Entry(self.window, width=2)
        entry.place(x=geometry[0], y=geometry[1], anchor=self.consts['center'])
