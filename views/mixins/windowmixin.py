class WindowMixin(object):
    def geometry(self, params):
        super().geometry('{}x{}+{}+{}'.format(*params))
