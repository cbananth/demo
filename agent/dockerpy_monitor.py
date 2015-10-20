from monitor import Monitor
from docker import Client

class DockerPyMonitor(Monitor):
    """Concrete class for agent monitor using DockerPy"""
    def __init__(self):
        client = Client(base_url="unix://var/run/docker.sock")
        result = client.inspect_container('c4e106bf9a32')

    def collect_host_stats(self):
        pass

    def collect_container_stats(self, container_id):
        self.container_stats[container_id] = self._get_container_stats(container_id)
        return self.container_stats

    def collect_all_container_stats(self):
        for container in self._list_all_containers():
            self.container_stats[container] = self.collect_container_stats(container)
        return self.container_stats

    def collect_errors(self):
        pass

    def stream_logs(self):
        return {}

    def _list_all_containers(self):
        return []

