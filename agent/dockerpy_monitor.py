from stats_monitor import Monitor
import docker
from docker import Client
import threading
import logging

logger = logging.getLogger("agent-logger")

class DockerPyMonitor(Monitor):
    """Concrete class for agent monitor using DockerPy"""
    def __init__(self):
        # client = Client(base_url="unix://var/run/docker.sock")
        # result = client.inspect_container('c4e106bf9a32')
        self.container_stats = {}
        self.client = Client(base_url='tcp://127.0.0.1:2375')

    def collect_host_stats(self):
        logger.info("Collecting Host statistics")

    def collect_container_stats(self, container_id):
        self.container_stats[container_id] = self._get_container_stats(container_id)
        logger.info("Collecting container stats for id %s" % container_id)
        return self.container_stats

    def collect_all_container_stats(self):
        for container in self._list_all_containers():
            self.container_stats[container] = self.collect_container_stats(container)
        return self.container_stats

    def stream_logs(self):
        return {}

    def list_all_containers(self):
        # todo: Needs to be tested
        # to do : Satya : Modify this for implementing list of containers
        # threading.Timer(5.0, self.list_all_containers).start()
        # client = docker.Client(base_url='unix://var/run/docker.sock', version="1.20")
        # return client.containers()
        return ['1234', '5678']

    def _get_container_stats(self, id):
        # to do : Satya : Modify this for implementing threading logic
        stats = self.client.stats(id)
        return stats



