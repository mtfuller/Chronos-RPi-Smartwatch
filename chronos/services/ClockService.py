from datetime import datetime, timedelta
from threading import Thread
from time import sleep

from chronos.services.Service import Service

class ClockService(Service):
    def __init__(self):
        super(ClockService, self).__init__()
        self.running = True
        self.add_event('clock')
        self.clock_event = self.get_event('clock')
        self.clock = Thread(target=self.clock_update)
        self.clock.start()

    def dispose(self):
        super(ClockService, self).dispose()
        self.running = False
        self.clock.join()

    def get_time(self):
        return datetime.now()

    def clock_update(self):
        while self.running:
            self.clock_event.fire(time=self.get_time())
            now = self.get_time()
            print(now)
            later = now + timedelta(seconds=1)
            later.replace(microsecond=0)
            diff = later - now
            print(diff)
            sleep(diff.total_seconds())

