from stats_monitor import Monitor
import logging

logger = logging.getLogger("agent-logger")


class PcpMonitor(Monitor):
    """Concrete class for agent monitor using PCP"""
    def __init__(self):
        logger.info("Using PCP to monitor Docker")

    def collect_host_stats(self):

        self.host_stats['memory'] = self._get_mem_stats()
        self.host_stats['cpu'] = self._get_cpu_stats()
        self.host_stats['disk'] = self._get_disk_stats()
        self.host_stats['network'] = self._get_nw_stats()

        return self.host_stats

    def collect_container_stats(self, container_id):
        self.container_stats[container_id] = self._get_container_stats(container_id)
        return self.container_stats

    def collect_errors(self):
        pass

    def stream_logs(self):
        return {}

    def _get_mem_stats(self):
        return {}

    def _get_cpu_stats(self):
        return {}

    def _get_disk_stats(self):
        return {}

    def _get_nw_stats(self):
        return {}

    def _get_container_stats(self, id):
        return {}