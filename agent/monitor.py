import logging

logger = logging.getLogger("agent-logger")


class Monitor(object):
    """Abstract class for agent monitor"""
    def __init__(self, driver):
        self.host_stats = {}
        self.container_stats = {}
        self.driver = driver()

    def collect_host_stats(self):
        return self.driver.collect_host_stats()

    def collect_container_stats(self):
        return self.driver.collect_container_stats()

    def collect_errors(self):
        return self.driver.collect_errors()

    def stream_logs(self):
        return self.driver.stream_logs()

