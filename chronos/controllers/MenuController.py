class MenuController(object):
    def __init__(self, view):
        self.view = view

    def clear_canvas(self, obj):
        self.view.get_canvas().clear()
