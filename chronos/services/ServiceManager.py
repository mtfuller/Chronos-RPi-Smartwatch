from chronos.services.ClockService import ClockService

class __ServiceManager(object):
    def __init__(self):
        self.services = {
            'clock': ClockService(),
        }

    def dispose(self):
        for service in self.services:
            self.services[service].dispose()
            print("DISPOSED OF",service)

    def get_service(self, name):
        if name not in self.services:
            return None
        return self.services[name]

ServiceManager = __ServiceManager()