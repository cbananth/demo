from config_reader import ConfigReader
from log_manager import LogManager
from log_manager import LogManager

logger = LogManager().logger

class Agent(object):
    def __init__(self):
        config_reader = ConfigReader("config.txt")
        config = config_reader.load_config()
        driver = config['monitoring_driver']
        file_name, cls_name = driver.strip().split(".")

        module = __import__(file_name)
        my_class = getattr(module, cls_name)
        self.monitor_driver = my_class()
        logger.debug("This is a debug message!!!")


if __name__ == "__main__":
    agent = Agent()

    logger.info("Command status : %s" % agent.monitor_driver.collect_host_stats())
