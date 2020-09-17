import tkinter as tk


class CanvasMixin(object):
    consts = {
        'center': tk.CENTER,
        'first': tk.FIRST,
        'last': tk.LAST,
        'font_lg': 'Arial 14',
        'font_sm': 'Arial 8',
    }

    cuid_collect = []

    def cuids_dump(self):
        collect = list(self.cuid_collect)
        self.cuid_collect.clear()
        return collect

    def change_color(self, cuid, new_color):
        return self.itemconfig(cuid, fill=new_color)

    def rect(self, geometry, color='#EEE'):
        cuid = self.create_rectangle(geometry, fill=color)
        self.cuid_collect.append(cuid)
        return cuid

    def line(self, geometry, color='#000'):
        cuid = self.create_line(*geometry,
                                       fill=color)
        self.cuid_collect.append(cuid)
        return cuid

    def arrow(self, geometry, color='#000'):
        cuid = self.create_line(*geometry,
                                       fill=color,
                                       arrow=self.consts['last'])
        self.cuid_collect.append(cuid)
        return cuid

    def arrow_f(self, geometry, color='#000'):
        cuid = self.create_line(*geometry,
                                       fill=color,
                                       arrow=self.consts['first'])
        self.cuid_collect.append(cuid)
        return cuid

    def text_sm(self, geometry, text):
        cuid = self.create_text(*geometry,
                                       text=text,
                                       justify=self.consts['center'],
                                       font=self.consts['font_sm'])
        self.cuid_collect.append(cuid)
        return cuid

    def text_lg(self, geometry, text):
        cuid = self.create_text(*geometry,
                                       text=text,
                                       justify=self.consts['center'],
                                       font=self.consts['font_lg'])
        self.cuid_collect.append(cuid)
        return cuid

    def oval(self, geometry, color='blue'):
        cuid = self.create_oval(*geometry, fill=color)
        self.cuid_collect.append(cuid)
        return cuid