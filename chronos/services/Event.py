class Event(object):
    def __init__(self):
        self.subscribers = set([])

    def subscribe(self, func):
        if func in self.subscribers:
            return False
        self.subscribers.add(func)
        return True

    def unsubscribe(self, func):
        if func not in self.subscribers:
            return False
        self.subscribers.remove(func)
        return True

    def fire(self, **kwargs):
        for func in self.subscribers:
            func(**kwargs)

    def getSubCount(self):
        return len(self.subscribers)

    def empty(self):
        return self.getSubCount() == 0