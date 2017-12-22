from chronos.services.ServiceManager import ServiceManager

class ClockController(object):
    def __init__(self, func):
        self.set_clock = func
        self.clock_service = ServiceManager.get_service('clock')
        self.clock_service.get_event('clock').subscribe(self.update_clock)

    def update_clock(self, **kwargs):
        t = kwargs['time']
        self.set_clock(t.hour, t.minute)