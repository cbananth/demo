from config_reader import ConfigReader
import logging
from monitor import Monitor
from log_manager import LogManager
import docker
import threading
logger = logging.getLogger("agent-logger")


class Agent(object):
    """Agent runs on each host collecting statistics from the host and the containers"""
    def __init__(self):
        log_mgr = LogManager()
        config_reader = ConfigReader("config.ini")
        config = config_reader.load_config()
        logger.info("Loaded configurations")
        driver = config['monitoring_driver']
        file_name, cls_name = driver.strip().split(".")
        module = __import__(file_name)
        driver_class = getattr(module, cls_name)
        self.monitor = Monitor(driver_class)
        self.stats = {}
        self.containers = []

    def get_all_stats(self):
        self.stats['host'] = self.monitor.collect_host_stats()
        self.stats['container'] = self.monitor.collect_container_stats()

    def get_all_errors(self):
        self.stats['error'] = self.monitor.collect_errors()

    def list_all_containers(self):
        #todo: Needs to be tested
        threading.Timer(5.0, self.list_all_containers).start()
        client = docker.Client(base_url='unix://var/run/docker.sock', version="1.20")
        self.containers = client.containers()

# if __name__ == "__main__":
#    agent = Agent()

#    logger.info("Home Directory : %s" % agent.monitor.collect_host_stats())
