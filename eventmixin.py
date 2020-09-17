class EventMixin(object):
    def click_listen(self, callback):
        event_name = '<Button-1>'
        self.bind(event_name, callback)

    def click_listen_tag(self, guid, callback):
        event_name = '<Button-1>'
        self.parent.tag_bind(guid, event_name, callback)

    def listen(self, event_name, callback, base_event=False):
        if not base_event:
            cmd = self.register(callback) + ' %d'
            event_name = '<<{}>>'.format(event_name)
            self.tk.call('bind', self, event_name, cmd)
        else:
            event_name = '<{}>'.format(event_name)
            self.bind('<Button-1>', callback)

    def emit(self, event_name, data):
        event_name = '<<{}>>'.format(event_name)
        self.parent.event_generate(event_name, data=data)