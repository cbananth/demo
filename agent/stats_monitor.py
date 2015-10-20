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

    def collect_container_stats(self, id):
        return self.driver.collect_container_stats(id)

    def stream_logs(self):
        return self.driver.stream_logs()

    def list_all_containers(self):
        return self.driver.list_all_containers()

