from calendar import month_name

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

from chronos.controllers.ClockController import ClockController

from kivy.gesture import GestureDatabase
from kivy.uix.boxlayout import BoxLayout
from kivy.gesture import Gesture

from chronos.controllers.MenuController import MenuController

Builder.load_string("""
<MenuView>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: './chronos/assets/img/splash_back.png'

<WelcomeScreen>:
    FloatLayout:
        size_hint: (None, None)
        size: (320,125)
        pos_hint:{'right': 1}
        Label:
            id: clock
            text: '00:00'
            font_size: '72'
            halign: 'right'
            text_size: (295,75)
        Label:
            id: date
            text: 'January 1, 2018'
            font_size: '16'
            text_size: (295,95)
            halign: 'right'
            

<AppScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size: (320,50)
            Button:
                text: 'Button1'
            Button:
                text: 'Button2'
            Button:
                text: 'Button3'
        GridLayout:
            rows: 2
            cols: 3
            Button:
                text: 'Button1'
            Button:
                text: 'Button2'
            Button:
                text: 'Button3'
""")


class GestureBox(BoxLayout):
    def __init__(self, **kwargs):
        super(GestureBox, self).__init__(**kwargs)

    def on_left_to_right_line(self):
        pass

    def on_touch_down(self, touch):
        #create an user defined variable and add the touch coordinates
        touch.ud['gesture_path'] = [(touch.x, touch.y)]
        super().on_touch_down(touch)

    def on_touch_move(self, touch):
        touch.ud['gesture_path'].append((touch.x, touch.y))
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if 'gesture_path' in touch.ud:
            #create a gesture object
            gesture = Gesture()
            #add the movement coordinates
            gesture.add_stroke(touch.ud['gesture_path'])
            #normalize so thwu willtolerate size variations
            gesture.normalize()
            #minscore to be attained for a match to be true
            print(gesture)
        super(GestureBox, self).on_touch_up(touch)

# Declare both screens
class WelcomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.clock = self.ids.clock
        self.date = self.ids.date
        self.clock_controller = ClockController(self.set_clock)

    def set_clock(self, hour, min, month, day, year):
        spacer = ":0" if (int(min / 10)) == 0 else ":"
        hour = hour if hour <= 12 else hour - 12
        self.clock.text = str(hour) + spacer + str(min)
        self.date.text = "%s %d, %d" % (month_name[month], day, year)

class AppScreen(Screen):
    pass

class MenuView(GestureBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_controller = MenuController()
        self.menu_controller.bind_gesture('left_to_right', self.next)
        self.screen_manager = ScreenManager()
        self.welcome_screen = WelcomeScreen(name='menu')
        self.settings_screen = AppScreen(name='apps')
        self.screen_manager.add_widget(self.welcome_screen)
        self.screen_manager.add_widget(self.settings_screen)
        self.add_widget(self.screen_manager)
        self.screen_manager.current = 'menu'

    def next(self):
        self.screen_manager.current = self.screen_manager.next()

    def on_touch_up(self, touch):
        if 'gesture_path' in touch.ud:
            gesture = Gesture()
            gesture.add_stroke(touch.ud['gesture_path'])
            gesture.normalize()
            self.menu_controller.match_gesture(gesture)
        super(GestureBox, self).on_touch_up(touch)
