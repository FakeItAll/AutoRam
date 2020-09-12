import tkinter as tk


class MainWindow(object):
    def __init__(self):
        root = tk.Tk()
        root.title('AutoRAM')
        root.geometry('1200x400+100+100')
        # root.state('zoomed')
        self.root = root

        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()

        canvas_width = width - width // 3
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

        width = 90
        height = max(in_count, out_count) * 18

        rect_coords.append(rect_coords[0] + width)
        rect_coords.append(rect_coords[1] + height)

        self.canvas.create_rectangle(*rect_coords)

        rect_center_x = rect_coords[0] + width // 2
        rect_center_y = rect_coords[1] + height // 2
        self.canvas.create_text(rect_center_x, rect_center_y,
                                text=schema.code, justify=self.consts['center'], font='Arial 14')

        shift = height // (in_count + 1)
        for i in range(in_count):
            cur_y = rect_coords[1] + shift * (i + 1)
            from_x = rect_coords[0] - self.consts['arrow_length']
            to_x = rect_coords[0]
            self.canvas.create_line(from_x, cur_y, to_x, cur_y, arrow=self.consts['last'])
            self.canvas.create_text(to_x + 4 * len(in_names[i]), cur_y,
                                    text=in_names[i], justify=self.consts['center'], font='Arial 8')

        shift = height // (out_count + 1)
        for i in range(out_count):
            cur_y = rect_coords[1] + shift * (i + 1)
            from_x = rect_coords[2]
            to_x = rect_coords[2] + self.consts['arrow_length']
            self.canvas.create_line(from_x, cur_y, to_x, cur_y, arrow=self.consts['last'])
            self.canvas.create_text(from_x - 4 * len(out_names[i]), cur_y,
                                    text=out_names[i], justify=self.consts['center'], font='Arial 8')

        return schema.uid

    def draw_matrix(self, matrix, rect_coords=[]):
        if matrix.io_settings.get('names'):
            in_names, out_names = matrix.io_settings['names']
            in_count, out_count = len(in_names), len(out_names)
        else:
            in_count, out_count = matrix.io_settings['count']

        width = out_count * 18
        height = in_count * 18

        rect_coords.append(rect_coords[0] + width)
        rect_coords.append(rect_coords[1] + height)

        self.canvas.create_rectangle(*rect_coords)

        shift = height // (in_count + 1)
        from_x = rect_coords[0] - self.consts['arrow_length']
        to_x = rect_coords[0]
        from_x2 = rect_coords[2] - width // (out_count + 1)
        for i in range(in_count):
            cur_y = rect_coords[1] + shift * (i + 1)
            self.canvas.create_line(from_x, cur_y, to_x, cur_y, arrow=self.consts['last'])
            self.canvas.create_line(from_x2, cur_y, to_x, cur_y)

        shift = width // (out_count + 1)
        from_y = rect_coords[3]
        to_y = rect_coords[3] + self.consts['arrow_length']
        to_y2 = rect_coords[1] + height // (in_count + 1)
        for i in range(out_count):
            cur_x = rect_coords[0] + shift * (i + 1)
            self.canvas.create_line(cur_x, from_y, cur_x, to_y, arrow=self.consts['last'])
            self.canvas.create_line(cur_x, from_y, cur_x, to_y2)

        x0 = rect_coords[0] + height // (in_count + 1)*2
        y0 = rect_coords[1] + width // (out_count + 1)*2
        self.canvas.create_oval(x0-3, y0-3, x0+3, y0+3, fill='blue')

    def execute(self):
        self.root.mainloop()
