import tkinter as tk


class MainWindow(object):
    def __init__(self):
        root = tk.Tk()
        root.title('AutoRAM')
        root.geometry('1000x400+100+100')
        # root.state('zoomed')
        self.root = root

        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()

        canvas_width = width // 2
        canvas_height = height - 10
        canvas = tk.Canvas(self.root,
                           width=canvas_width, height=canvas_height, bg='lightgrey')
        canvas.pack(side='left')
        self.canvas = canvas

        self.consts = {'center': tk.CENTER, 'first': tk.FIRST, 'last': tk.LAST, 'arrow_length': 20}

    def draw_schema(self, schema, rect_coords=[]):
        if schema.io_settings.get('names'):
            in_names, out_names = schema.io_settings['names']
            in_count, out_count = len(in_names), len(out_names)
        else:
            in_count, out_count = schema.io_settings['count']

        width = max(in_count, out_count) * 25
        height = 60

        rect_coords.append(rect_coords[0] + width)
        rect_coords.append(rect_coords[1] + height)

        self.canvas.create_rectangle(*rect_coords)

        rect_center_x = min(rect_coords[0], rect_coords[2]) + width // 2
        rect_center_y = min(rect_coords[1], rect_coords[3]) + height // 2
        self.canvas.create_text(rect_center_x, rect_center_y,
                                text=schema.code, justify=self.consts['center'], font='Arial 14')

        shift = width // (in_count + 1)
        for i in range(in_count):
            cur_x = rect_coords[0] + shift * (i + 1)
            from_y = rect_coords[3]
            to_y = rect_coords[3] + self.consts['arrow_length']
            self.canvas.create_line(cur_x, from_y, cur_x, to_y, arrow=self.consts['first'])
            self.canvas.create_text(cur_x, from_y - 8,
                                    text=in_names[i], justify=self.consts['center'], font='Arial 8')

        shift = width // (out_count + 1)
        for i in range(out_count):
            cur_x = rect_coords[0] + shift * (i + 1)
            from_y = rect_coords[1]
            to_y = rect_coords[1] - self.consts['arrow_length']
            self.canvas.create_line(cur_x, from_y, cur_x, to_y, arrow=self.consts['last'])
            self.canvas.create_text(cur_x, from_y + 8,
                                    text=out_names[i], justify=self.consts['center'], font='Arial 8')

        return schema.uid

    def execute(self):
        self.root.mainloop()
