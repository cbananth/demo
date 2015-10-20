from stats_monitor import Monitor
import os
import logging

logger = logging.getLogger("agent-logger")


class SysDigMonitor(Monitor):
    """Concrete class for agent monitor using Sysdig"""
    def __init__(self):
        self.host_stats = {}
        self.container_stats = {}
        logger.info("Using Sysdig to monitor Docker")

    def collect_host_stats(self):
        return os.getenv("HOME")

    def collect_container_stats(self):
        pass

    def collect_errors(self):
        pass

    def stream_logs(self):
        pass
