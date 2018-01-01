from kivy.uix.widget import Widget
from kivy.uix.button import Button

from chronos.controllers.MenuController import MenuController
from chronos.views.MenuView import MenuView

class ChronosView(object):
    def __init__(self, **kwargs):
        self.menu = MenuView()

    def build(self):
        return self.menu