from config_reader import ConfigReader
import logging
from monitor import Monitor
from log_manager import LogManager

logger = logging.getLogger("agent-logger")


class Agent(object):
    def __init__(self):
        log_mgr = LogManager()
        config_reader = ConfigReader("config.txt")
        config = config_reader.load_config()
        logger.info("Loaded configurations")
        driver = config['monitoring_driver']
        file_name, cls_name = driver.strip().split(".")

        module = __import__(file_name)
        driver_class = getattr(module, cls_name)
        self.monitor = Monitor(driver_class)


if __name__ == "__main__":
    agent = Agent()

    logger.info("Home Directory : %s" % agent.monitor.collect_host_stats())
