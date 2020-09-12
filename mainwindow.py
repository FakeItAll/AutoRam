import tkinter as tk
import random


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

        self.schemas = {}

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

        in_id, out_id = {}, {}

        rect_center_x = rect_coords[0] + width // 2
        rect_center_y = rect_coords[1] + height // 2
        self.canvas.create_text(rect_center_x, rect_center_y,
                                text=schema.code, justify=self.consts['center'], font='Arial 14')

        shift = height // (in_count + 1)
        from_x = rect_coords[0] - self.consts['arrow_length']
        to_x = rect_coords[0]
        for i in range(in_count):
            cur_y = rect_coords[1] + shift * (i + 1)
            self.canvas.create_line(from_x, cur_y, to_x, cur_y, arrow=self.consts['last'])
            self.canvas.create_text(to_x + 4 * len(in_names[i]), cur_y,
                                    text=in_names[i], justify=self.consts['center'], font='Arial 8')
            in_id[in_names[i]] = [from_x, cur_y]

        shift = height // (out_count + 1)
        from_x = rect_coords[2]
        to_x = rect_coords[2] + self.consts['arrow_length']
        for i in range(out_count):
            cur_y = rect_coords[1] + shift * (i + 1)
            self.canvas.create_line(from_x, cur_y, to_x, cur_y, arrow=self.consts['last'])
            self.canvas.create_text(from_x - 4 * len(out_names[i]), cur_y,
                                    text=out_names[i], justify=self.consts['center'], font='Arial 8')
            out_id[out_names[i]] = [to_x, cur_y]

        self.schemas[schema.uid] = {'obj': schema, 'names': [in_id, out_id]}

        return schema.uid

    def draw_matrix(self, matrix, rect_coords=[]):
        in_names, out_names = matrix.io_settings['names']
        in_count, out_count = len(in_names), len(out_names)

        width = out_count * 18
        height = in_count * 18

        rect_coords.append(rect_coords[0] + width)
        rect_coords.append(rect_coords[1] + height)

        in_id, out_id = {}, {}

        shift = height // (in_count + 1)
        from_x = rect_coords[0] - self.consts['arrow_length']
        to_x = rect_coords[0]
        from_x2 = rect_coords[2] - width // (out_count + 1)
        for i in range(in_count):
            cur_y = rect_coords[1] + shift * (i + 1)
            self.canvas.create_line(from_x, cur_y, to_x, cur_y, arrow=self.consts['last'])
            self.canvas.create_line(from_x2, cur_y, to_x, cur_y)
            in_id[in_names[i]] = [from_x, cur_y]

        shift = width // (out_count + 1)
        from_y = rect_coords[3]
        to_y = rect_coords[3] + self.consts['arrow_length']
        to_y2 = rect_coords[1] + height // (in_count + 1)
        for i in range(out_count):
            cur_x = rect_coords[0] + shift * (i + 1)
            self.canvas.create_line(cur_x, from_y+1, cur_x, to_y, arrow=self.consts['last'])
            self.canvas.create_line(cur_x, from_y-1, cur_x, to_y2)
            out_id[out_names[i]] = [cur_x, to_y]

        self.schemas[matrix.uid] = {'obj': matrix, 'names': [in_id, out_id]}

        for key_y in matrix.matrix.keys():
            y_n = in_names.index(key_y) + 1
            y0 = rect_coords[1] + width // (out_count + 1) * y_n
            for key_x in matrix.matrix[key_y]:
                x_n = out_names.index(key_x) + 1
                x0 = rect_coords[0] + height // (in_count + 1) * x_n
                self.canvas.create_oval(x0-3, y0-3, x0+3, y0+3, fill='blue')

        return matrix.uid

    def draw_connections(self):
        for schema_i in self.schemas.values():
            schema = schema_i['obj']
            for schema_to_uid in schema.connector.schema_binds():
                schema_to_i = self.schemas[schema_to_uid]
                connections = schema.connector.raw(schema_to_uid)
                for c_out, c_in in connections.items():
                    pos_out = schema_i['names'][1][c_out]
                    pos_in = schema_to_i['names'][0][c_in]
                    diff = abs(pos_in[0] - pos_out[0]) * 0.1
                    pos_x = random.randint(min(pos_in[0], pos_out[0]) + diff, max((pos_in[0], pos_out[0])) - diff)
                    self.canvas.create_line(pos_out, pos_x, pos_out[1], fill='red')
                    self.canvas.create_line(pos_x, pos_out[1], pos_x, pos_in[1], fill='red')
                    self.canvas.create_line(pos_x, pos_in[1], pos_in, fill='red')

    def execute(self):
        self.root.mainloop()
