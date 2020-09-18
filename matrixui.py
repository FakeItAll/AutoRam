from schemaui import SchemaUI


class MatrixUI(SchemaUI):
    def __init__(self, parent, matrix, coords, direction):
        super().__init__(parent, matrix, coords, direction)
        self.matrix = matrix

        self.holes_color = '#00F'

        self.out_direction = (direction + 1) % 4

    def draw(self):
        rect_coords = self.rect_coords
        in_names, out_names = self.matrix.io_settings['names']
        in_count, out_count = len(in_names), len(out_names)

        width = out_count * self.pins_spacing
        height = in_count * self.pins_spacing

        rect_coords.append(rect_coords[0] + width)
        rect_coords.append(rect_coords[1] + height)

        self.parent.rect([rect_coords], self.default_color)

        in_id, out_id = {}, {}

        shift = height // (in_count + 1)
        from_x = rect_coords[0] - self.arrow_length
        to_x = rect_coords[0]
        from_x2 = rect_coords[2] - width // (out_count + 1)
        foo = 3
        for i in range(in_count):
            cur_y = rect_coords[1] + shift * (i + 1)
            self.parent.arrow([from_x, cur_y, to_x, cur_y])
            self.parent.line([from_x2 - foo, cur_y, to_x, cur_y])

            in_id[in_names[i]] = [from_x, cur_y]

        shift = width // (out_count + 1)
        from_y = rect_coords[3]
        to_y = rect_coords[3] + self.arrow_length
        to_y2 = rect_coords[1] + height // (in_count + 1)
        for i in range(out_count):
            cur_x = rect_coords[0] + shift * (i + 1)
            self.parent.arrow([cur_x, from_y + 1, cur_x, to_y])
            self.parent.line([cur_x, from_y - 1, cur_x, to_y2])
            out_id[out_names[i]] = [cur_x, to_y]

        self.in_coords = in_id
        self.out_coords = out_id

        for key_y in self.matrix.matrix.keys():
            y_n = in_names.index(key_y) + 1
            y0 = rect_coords[1] + width // (out_count + 1) * y_n
            for key_x in self.matrix.matrix[key_y]:
                x_n = out_names.index(key_x) + 1
                x0 = rect_coords[0] + height // (in_count + 1) * x_n
                self.parent.oval([x0 - 3, y0 - 3, x0 + 3, y0 + 3], self.holes_color)

        self.cuids = self.parent.cuids_dump()
        self.bind()

        return self.matrix.uid