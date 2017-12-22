from kivy.uix.widget import Widget
from kivy.uix.button import Button

from chronos.controllers.MenuController import MenuController
from chronos.views.MenuView import MenuView

class ChronosView():
    def __init__(self, **kwargs):
        super().__init__()
        self.menu = MenuView()

    def build(self):
        return self.menu