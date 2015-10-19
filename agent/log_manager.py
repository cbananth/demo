import os
import logging


class LogManager(object):
    """Logging framework for the monitoring agent"""
    def __init__(self, log_level, log_folder):
        self.logger = logging.getLogger("agent-logger")
        if log_level not in logging._levelNames:
            print "Error: loglevel '{0}' is invalid, must be one of (DEBUG, INFO, WARNING, ERROR)".format(log_level)
            exit(2)

        # check log dir, create if not present
        if not os.path.isdir(log_folder):
            os.mkdir(log_folder, 0777)
        if not os.path.isdir(log_folder):
            print "logs folder missing in {}\n".format(log_folder)

