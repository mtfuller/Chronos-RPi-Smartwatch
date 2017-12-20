class Event(object):
    def __init__(self):
        self.subscribers = set([])

    def subscribe(self, func):
        '''
        Adds the given function reference to the event. Returns true if the is successfully subscribed to the event.
        Otherwise, returns false.

        :param func: A reference to a callable instance (function, method, etc.).
        :return: boolean
        '''
        if func in self.subscribers:
            return False
        self.subscribers.add(func)
        return True

    def unsubscribe(self, func):
        '''
        Removes the given function from the event. Returns true if the is successfully un-subscribed from the event.
        Otherwise, returns false.

        :param func: A reference to a callable instance (function, method, etc.).
        :return: boolean
        '''
        if func not in self.subscribers:
            return False
        self.subscribers.remove(func)
        return True

    def fire(self, **kwargs):
        '''
        Calls each function that is subscribed to the event, passing in the kwargs given.
        '''
        for func in self.subscribers:
            func(**kwargs)

    def getSubCount(self):
        '''
        Returns the number of functions that are subscribed to this event.

        :return: int
        '''
        return len(self.subscribers)

    def empty(self):
        '''
        Returns true if there are no functions subscribed to the event. Otherwise, returns false.

        :return: boolean
        '''
        return self.getSubCount() == 0