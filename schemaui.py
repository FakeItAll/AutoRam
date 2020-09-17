from eventmixin import EventMixin


class SchemaUI(EventMixin):
    def __init__(self, parent, schema, coords):
        self.parent = parent
        self.schema = schema
        self.uid = schema.uid
        self.selected = False

        self.arrow_length = 15
        self.schema_length = 90
        self.pins_spacing = 15

        self.default_color = '#DDD'
        self.active_color = '#F00'

        cuids = self.draw(coords)
        self.rect_cuid = cuids[0]
        for cuid in cuids:
            self.click_listen_tag(cuid, self.click_handler)

    def draw(self, rect_coords):
        cuids = []
        if self.schema.io_settings.get('names'):
            in_names, out_names = self.schema.io_settings['names']
            in_count, out_count = len(in_names), len(out_names)
        else:
            in_count, out_count = self.schema.io_settings['count']

        width = self.schema_length
        height = max(in_count, out_count) * self.pins_spacing

        rect_coords.append(rect_coords[0] + width)
        rect_coords.append(rect_coords[1] + height)

        cuids.append(self.parent.rect(rect_coords, self.default_color))

        in_id, out_id = {}, {}

        rect_center_x = rect_coords[0] + width // 2
        rect_center_y = rect_coords[1] + height // 2
        self.parent.text_lg([rect_center_x, rect_center_y], self.schema.code)

        shift = height // (in_count + 1)
        from_x = rect_coords[0] - self.arrow_length
        to_x = rect_coords[0]
        for i in range(in_count):
            cur_y = rect_coords[1] + shift * (i + 1)
            self.parent.arrow([from_x, cur_y, to_x, cur_y])
            self.parent.text_sm([to_x + 4 * len(in_names[i]), cur_y], in_names[i])
            in_id[in_names[i]] = [from_x, cur_y]

        shift = height // (out_count + 1)
        from_x = rect_coords[2]
        to_x = rect_coords[2] + self.arrow_length
        for i in range(out_count):
            cur_y = rect_coords[1] + shift * (i + 1)
            self.parent.arrow([from_x, cur_y, to_x, cur_y])
            self.parent.text_sm([from_x - 4 * len(out_names[i]), cur_y], out_names[i])

            out_id[out_names[i]] = [to_x, cur_y]

        # self.schemas[self.schema.uid] = {'obj': self.schema, 'names': [in_id, out_id]}

        return self.parent.cuids_dump()

    def click_handler(self, e):
        self.select()
        self.emit('OnSelect', self.uid)

    def select(self):
        if not self.selected:
            print('select ' + str(self.uid))
            self.parent.change_color(self.rect_cuid, self.active_color)
            self.selected = True

    def unselect(self):
        if self.selected:
            print('unselect ' + str(self.uid))
            self.parent.change_color(self.rect_cuid, self.default_color)
            self.selected = False
