import kivy
kivy.require('1.9.0')

WIDTH = '320'
HEIGHT = '240'

from kivy.app import App
from kivy.config import Config
Config.set('graphics','width', WIDTH)
Config.set('graphics', 'height', HEIGHT)
Config.set('graphics', 'fullscreen', 1)

from chronos.views.ChronosView import ChronosView

class ChronosApp(App):
    def __init__(self, **kwargs):
        App.__init__(self)
        self.stage = ChronosView()

    def build(self):
        return self.stage.build()
