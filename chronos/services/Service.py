from chronos.services.Event import Event

class Service(object):
    def __init__(self):
        self.events = {}

    def add_event(self, name):
        if self.has_event(name):
            return False
        self.events[name] = Event()
        return True

    def get_event(self, name):
        if self.has_event(name):
            return self.events[name]
        return None

    def has_event(self, name):
        return name in self.events

    def get_event_count(self):
        return len(self.events)