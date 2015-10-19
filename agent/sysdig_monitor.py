from monitor import Monitor
import os


class SysDigMonitor(Monitor):
    """Concrete class for agent monitor using Sysdig"""
    def __init__(self):
        self.host_stats = {}
        self.container_stats = {}
        print "Using Sysdig to monitor Docker"

    def collect_host_stats(self):
        result = os.system('hostname')
        return result

    def collect_container_stats(self):
        pass

    def collect_errors(self):
        pass

    def stream_logs(self):
        pass
