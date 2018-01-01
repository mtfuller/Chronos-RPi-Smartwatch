import json
from pprint import pprint

from kivy.app import App
from kivy.gesture import GestureDatabase
from kivy.uix.boxlayout import BoxLayout
from kivy.gesture import Gesture

class GestureRecorderLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(GestureRecorderLayout, self).__init__(**kwargs)
        self.manager = GestureManager()


    def on_touch_down(self, touch):
        #create an user defined variable and add the touch coordinates
        touch.ud['gesture_path'] = [(touch.x, touch.y)]
        super(GestureRecorderLayout, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        touch.ud['gesture_path'].append((touch.x, touch.y))
        super(GestureRecorderLayout, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if 'gesture_path' in touch.ud:
            name = raw_input("What would you like to name the gesture?\nName: ")
            self.manager.add_gesture(name, touch.ud['gesture_path'])
            self.manager.save()
            super(GestureRecorderLayout, self).on_touch_up(touch)

class GestureRecorder(App):
    def __init__(self, **kwargs):
        super(GestureRecorder, self).__init__(**kwargs)

    def build(self):
        return GestureRecorderLayout()

class GestureManager(object):
    def __init__(self, path='./chronos/assets/gestures/'):
        with open(path+'gestures.json', "r+") as f:
            self.path = path
            self.str_gestures = json.load(f)
            self.db = GestureDatabase()
            for name, gesture_string in self.str_gestures.items():
                gesture = self.db.str_to_gesture(gesture_string)
                gesture.name = name
                self.db.add_gesture(gesture)

    def add_gesture(self, name, gesture_path):
        gesture = Gesture()
        gesture.add_stroke(gesture_path)
        gesture.normalize()
        if name in self.str_gestures:
            raise ValueError('Cannot overwrite existing gesture in file.')
        gesture.name = name
        self.str_gestures[name] = self.db.gesture_to_str(gesture).decode('utf-8')
        self.db.add_gesture(gesture)

    def save(self, path=None):
        if not path:
            path = self.path
        with open(path+'gestures.json', "r+") as f:
            f.seek(0)
            json.dump(self.str_gestures, f)
            f.truncate()