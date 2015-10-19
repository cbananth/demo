from monitor import Monitor
import os
from log_manager import LogManager

logger = LogManager().logger


class PcpMonitor(Monitor):
    """Concrete class for agent monitor using PCP"""
    def __init__(self):
        self.host_stats = {}
        self.container_stats = {}
        logger.info("Using PCP to monitor Docker")

    def collect_host_stats(self):
        result = os.system('hostname')
        return result

    def collect_container_stats(self):
        pass

    def collect_errors(self):
        pass

    def stream_logs(self):
        pass
