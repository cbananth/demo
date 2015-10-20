import logging

from config_reader import ConfigReader
from stats_monitor import Monitor
from log_monitor import LogMonitor
from log_manager import LogManager

logger = logging.getLogger("agent-logger")
STAT_MON = "stats_monitoring_driver"
LOG_MON = "log_monitoring_driver"


class Agent(object):
    """Agent runs on each host collecting statistics from the host and the containers"""
    def __init__(self):
        self.stats = {}
        self.log_stream = []
        self.containers = []
        self.monitor = None
        self.log_collector = None
        log_mgr = LogManager()

        # Read config file and load the dictionary
        config_reader = ConfigReader("config.ini")
        self.config = config_reader.load_config()
        logger.info("Loaded configurations")

        self._load_stats_monitor()
        self._load_log_collector()
        self.containers = self.list_all_containers()

    def get_all_stats(self):
        stat_dict = {}
        self.stats['host'] = self.monitor.collect_host_stats()
        for elt in self.containers:
            stat_dict[elt] = self.monitor.collect_container_stats(elt)
            self.stats['container'] = stat_dict

    def get_all_logs(self):
        self.log_stream = self.log_collector.get_app_logs()

    def get_all_errors(self):
        self.stats['error'] = self.log_collector.get_error_logs()

    def list_all_containers(self):
        return self.monitor.list_all_containers()

    def _load_stats_monitor(self):
        """Dynamically load the stats monitoring driver"""
        driver = self.config[STAT_MON]
        file_name, cls_name = driver.strip().split(".")
        module = __import__(file_name)
        driver_class = getattr(module, cls_name)
        self.monitor = Monitor(driver_class)

    def _load_log_collector(self):
        """Dynamically load the log collector driver"""
        log_driver = self.config[LOG_MON]
        file_name, cls_name = log_driver.strip().split(".")
        module = __import__(file_name)
        driver_class = getattr(module, cls_name)
        self.log_collector = LogMonitor(driver_class)


if __name__ == "__main__":
    agent = Agent()
    agent.get_all_stats()
    agent.get_all_logs()
    agent.get_all_errors()

