import os
import logging
import logging.handlers
from config_reader import ConfigReader


class LogManager(object):
    """Logging framework for the monitoring agent"""
    def __init__(self):
        self.logger = logging.getLogger("agent-logger")
        config_reader = ConfigReader("config.txt")
        config = config_reader.load_config()
        log_level = config['log_level']
        log_file = config['log_file']
        console_debug = config['console_debug']
        if console_debug.strip() is "True":
            console_debug = True
        else:
            console_debug = False
        self.create_logger(log_level, log_file, console_debug=console_debug)

    def create_logger(self, log_level, log_file, console_debug=True):
        """
        Returns the logger object taking the following as inputs
        :param log_level: INFO,DEBUG,ERROR are log levels
        :param log_file: Full path to the log file
        :param console_debug: Boolean value that enables/disables console debug
        :return: logger object
        """
        if log_level not in logging._levelNames:
            print "Error: loglevel '{0}' is invalid, must be one of (DEBUG, INFO, WARNING, ERROR)".format(log_level)
            exit(2)

        log_format = "%(asctime)s  %(module)-10s %(lineno)-4d %(processName)s %(levelname)-5s %(funcName)s: %(message)s"

        formatter = logging.Formatter(log_format)
        self.logger.setLevel(log_level)

        fh = logging.handlers.RotatingFileHandler(filename=log_file, maxBytes=2097152, backupCount=10)  # backupcount is the no. of files to keep while rotating
        fh.setFormatter(formatter)
        fh.setLevel(log_level)    # this hard-coding makes log file to always have all the logs making it easier to debug any issue
        self.logger.addHandler(fh)

        if console_debug:
            # adding the console debug log to see the logs on the same window
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

