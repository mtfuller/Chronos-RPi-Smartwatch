from random import random
from kivy.graphics import Color, Ellipse, Line

class PainterController(object):
    def __init__(self, view):
        self.view = view

    def touch_down(self, touch):
        color = (random(), 1, 1)
        with self.view.get_canvas():
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
