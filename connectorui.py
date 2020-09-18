import random


class ConnectorUI(object):
    def __init__(self, parent, schema_from_ui, schema_to_ui, connections):
        self.parent = parent
        self.schema_from_ui = schema_from_ui
        self.schema_to_ui = schema_to_ui
        self.connections = connections

        self.color = '#F00'

    def draw(self):
        for c_out, c_in in self.connections.items():
            pos_out = self.schema_from_ui.out_coords[c_out]
            pos_in = self.schema_to_ui.in_coords[c_in]
            dir_in = self.schema_from_ui.out_direction
            dir_out = self.schema_to_ui.in_direction

            if dir_in == dir_out:
                diff = round(abs(pos_in[0] - pos_out[0]) * 0.1)
                pos_x = random.randint(min(pos_in[0], pos_out[0]) + diff, max((pos_in[0], pos_out[0])) - diff)

                self.parent.line([pos_out, pos_x, pos_out[1]], self.color)
                self.parent.line([pos_x, pos_out[1], pos_x, pos_in[1]], self.color)
                self.parent.line([pos_x, pos_in[1], pos_in], self.color)
            elif abs(dir_in - dir_out) == 1:
                self.parent.line([pos_out, pos_out[0], pos_in[1]], self.color)
                self.parent.line([pos_out[0], pos_in[1], pos_in], self.color)
