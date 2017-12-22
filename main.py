from chronos.ChronosApp import ChronosApp
from chronos.services.ServiceManager import ServiceManager

if __name__ == '__main__':
    chronos = ChronosApp()
    chronos.run()
    ServiceManager.dispose()