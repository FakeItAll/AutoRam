from loader import Loader
from collect_manger import CollectManager
import tkinter as tk


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=200, height=200, bg='white')
        self.canvas.pack()
        self.arrow_first, self.arrow_last = tk.FIRST, tk.LAST
        self.arrow_length = 20
        self.text_center = tk.CENTER

    def gen_coords(self):
        return [20, 50, 180, 100]

    def draw_schema(self, schema):
        rect_coords = self.gen_coords()
        width = abs(rect_coords[0] - rect_coords[2])
        height = abs(rect_coords[1] - rect_coords[3])

        if schema.io_settings.get('count'):
            in_count, out_count = schema.io_settings['count']
        else:
            in_count, out_count = 3, 7

        self.canvas.create_rectangle(*rect_coords)

        rect_center_x = min(rect_coords[0], rect_coords[2]) + width // 2
        rect_center_y = min(rect_coords[1], rect_coords[3]) + height // 2
        self.canvas.create_text(rect_center_x, rect_center_y,
                                text=schema.code, justify=self.text_center, font='Arial 14')

        shift = width // (in_count + 1)
        for i in range(in_count):
            cur_x = rect_coords[0] + shift * (i + 1)
            from_y = rect_coords[3]
            to_y = rect_coords[3] + self.arrow_length
            self.canvas.create_line(cur_x, from_y, cur_x, to_y, arrow=self.arrow_first)

        shift = width // (out_count + 1)
        for i in range(out_count):
            cur_x = rect_coords[0] + shift * (i + 1)
            from_y = rect_coords[1]
            to_y = rect_coords[1] - self.arrow_length
            self.canvas.create_line(cur_x, from_y, cur_x, to_y, arrow=self.arrow_last)

    def execute(self):
        self.root.mainloop()


def main():
    loader = Loader()
    cm = CollectManager()

    mod1 = loader.load_schema('decryptor')
    mod2 = loader.load_schema('decryptor')
    mod3 = loader.load_schema('and')

    uid1 = cm.add(mod1)
    uid2 = cm.add(mod2)
    cm.connect({uid1: {'D0': [uid2, 'A'], 'D1': [uid2, 'B'], 'D2': [uid2, 'C']}})

    uid3 = cm.add(mod3)
    cm.connect({uid2: {'D0': [uid3, 'I1'], 'D1': [uid3, 'I2']}})

    mw = MainWindow()
    mw.draw_schema(mod1)
    mw.execute()

    ins = {'A': 1, 'B': 0, 'C': 0}
    cm.execute(uid1, ins, True)


if __name__ == '__main__':
    main()
