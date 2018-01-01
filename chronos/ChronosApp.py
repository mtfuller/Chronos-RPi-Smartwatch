from kivy.app import App
from kivy.core.window import Window
from chronos.views.ChronosView import ChronosView
#Window.fullscreen = True

class ChronosApp(App):
    WIDTH = 320
    HEIGHT = 240

    def __init__(self, **kwargs):
        App.__init__(self)
        Window.size = (ChronosApp.WIDTH, ChronosApp.HEIGHT)
        self.stage = ChronosView()

    def build(self):
        return self.stage.build()
