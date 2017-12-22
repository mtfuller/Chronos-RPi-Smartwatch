from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
from kivy.uix.widget import Widget

from chronos.controllers.ClockController import ClockController

Builder.load_string("""
<MenuView>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: './chronos/assets/img/splash_back.png'
            
<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
class WelcomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = FloatLayout()
        self.clock = Label(text="00:00", size_hint=(1.0, 1.0), font_size='72', padding_y='20', padding_x='20', halign="right", valign="bottom")
        self.clock.bind(size=self.clock.setter('text_size'))
        layout.add_widget(self.clock)
        self.add_widget(layout)
        self.clock_controller = ClockController(self.set_clock)

    def set_clock(self, hour, min):
        spacer = ":0" if (min / 10) == 0 else ":"
        hour = hour + 1 if hour <= 12 else hour - 12
        self.clock.text = str(hour) + spacer + str(min)

class SettingsScreen(Screen):
    pass

class MenuView(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.welcome_screen = WelcomeScreen(name='menu')
        self.settings_screen = SettingsScreen(name='settings')
        self.add_widget(self.welcome_screen)
        self.add_widget(self.settings_screen)
        self.current = 'menu'