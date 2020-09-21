import tkinter.ttk as ttk
from tkinterhtml import TkinterHtml
from PIL import Image, ImageTk


class HtmlViewer(ttk.Frame):
    def __init__(self, parent, width, height):
        self.parent = parent
        self.page = 0
        self.dir = './views/static/'
        self.files = ['page1.html', 'page2.html', 'page3.html']
        self.images = []
        self.contents = []

        super().__init__(parent, width=width, height=height)

        self.pagination_frame = ttk.Frame(self, width=width, height=50)
        self.pagination_frame.pack(side='bottom')

        self.prev_button = ttk.Button(self.pagination_frame, text='<=', command=self.pick_prev)
        self.prev_button.pack(side='left')

        self.page_label = ttk.Label(self.pagination_frame, font='Arial 14 bold')
        self.page_label.pack(side='left')

        self.next_button = ttk.Button(self.pagination_frame, text='=>', command=self.pick_next)
        self.next_button.pack(side='left')

        self.html_frame = TkinterHtml(self,
                                      width=width,
                                      height=height-50,
                                      fontscale=0.7,
                                      imagecmd=self.load_img)
        vsb = ttk.Scrollbar(self, orient='vertical', command=self.html_frame.yview)
        self.html_frame.configure(yscrollcommand=vsb)
        vsb.pack(side='right')
        self.html_frame.pack()

        self.load_files()
        self.refresh()

    def load_img(self, file_name):
        file_path = self.dir + file_name

        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        self.images.append(photo)
        return photo

    def load_files(self):
        self.contents = []
        for file_name in self.files:
            file_path = self.dir + file_name
            with open(file_path, 'r', encoding='utf8') as file:
                data = file.read().replace('\n', '')
                self.contents.append(data)
        self.refresh()

    def pick_prev(self):
        if not self.contents or self.page - 1 < 0:
            return
        self.page -= 1
        self.refresh()

    def pick_next(self):
        if not self.contents or self.page + 1 >= len(self.contents):
            return
        self.page += 1
        self.refresh()

    def refresh(self):
        if not self.contents:
            return
        if self.page == 0:
            self.prev_button.configure(state='disabled')
        else:
            self.prev_button.configure(state='normal')

        self.page_label.configure(text=self.page + 1)

        if self.page == len(self.contents) - 1:
            self.next_button.configure(state='disabled')
        else:
            self.next_button.configure(state='normal')
        self.html_frame.reset()
        self.html_frame.parse(self.contents[self.page])

