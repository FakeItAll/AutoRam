import webview


class WebViewWindow(object):
    def __init__(self):
        self.dir = './views/static/'
        file_path = self.dir + 'page.html'
        self.width = 800
        self.hegiht = 600
        webview.create_window('', file_path, width=self.width, height=self.hegiht)
        webview.start()
