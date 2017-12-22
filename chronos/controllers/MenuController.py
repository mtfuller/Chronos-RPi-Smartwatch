from chronos.utils.GestureManager import GestureManager

class MenuController(object):
    def __init__(self):
        self.gestures = GestureManager()
        self.binded_func = {}


    def bind_gesture(self, gesture_name, func):
        if gesture_name not in self.gestures.str_gestures:
            raise ValueError('Gesture name does not exist')
        self.binded_func[gesture_name] = func

    def match_gesture(self, gesture):
        match = self.gestures.db.find(gesture, minscore=0.3)
        if match:
            if match[1].name in self.binded_func:
                self.binded_func[match[1].name]()
            print("{} happened".format(match[1].name))
