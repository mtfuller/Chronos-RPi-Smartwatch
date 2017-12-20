from chronos.services.Event import Event

class Service(object):
    def __init__(self):
        self.events = {}

    def add_event(self, name):
        '''
        Adds a new event to the collection of events. Returns true if an event has been added successfully. Otherwise,
        returns false.

        :param name: A String of the unique event name.
        :return: boolean
        '''
        if self.has_event(name):
            return False
        self.events[name] = Event()
        return True

    def get_event(self, name):
        '''
        Returns the event instance under the given unique name. If the name is not registered, it returns None.

        :param name: A String of the unique event name.
        :return: Event or None
        '''
        if self.has_event(name):
            return self.events[name]
        return None

    def has_event(self, name):
        '''
        Returns true if the given name has an associated Event instance with it.

        :param name: A String of the unique event name.
        :return: boolean
        '''
        return name in self.events

    def get_event_count(self):
        '''
        Returns the number of events that are registered.

        :return: int
        '''
        return len(self.events)

    def empty(self):
        '''
        Returns true if there are currently no registered events.

        :return: boolean
        '''
        return self.get_event_count() == 0