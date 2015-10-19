from config_reader import ConfigReader
from monitor import Monitor
import importlib

global config

class Agent(object):
    def __init__(self):
        config_reader = ConfigReader("config.txt")
        config = config_reader.load_config()
        driver = config['monitoring_driver']
        file_name, cls_name = driver.strip().split(".")

        module = __import__(file_name)
        my_class = getattr(module, cls_name)
        self.monitor_driver = my_class()


if __name__ == "__main__":
    agent = Agent()
    print "Command status : %s" % agent.monitor_driver.collect_host_stats()
