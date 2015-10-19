

class Monitor(object):
    """Abstract class for agent monitor"""
    def __init__(self, strategy):
        self.host_stats = {}
        self.container_stats = {}
        self.driver = strategy()
        pass

    def collect_host_stats(self):
        pass

    def collect_container_stats(self):
        pass

    def collect_errors(self):
        pass

    def stream_logs(self):
        pass

