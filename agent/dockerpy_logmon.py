from log_monitor import LogMonitor
import logging
logger = logging.getLogger("agent-logger")


class DockerPyLogMon(LogMonitor):
    """Concrete class for monitoring logs using Docker-Py"""
    def __init__(self):
        pass

    def get_app_logs(self):
        logger.info("Collecting logs using Docker-Py")
        return []

    def get_error_logs(self):
        logger.info("Collecting Errors using Docker-Py")
        return []

    def _filter_logs(self):
        return []
