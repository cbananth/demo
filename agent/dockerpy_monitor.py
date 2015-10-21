from stats_monitor import Monitor
import docker
from docker import Client
import threading
import logging
import time
import msgpack
from multiprocessing import Process
from demo.agent.util import output
logger = logging.getLogger("agent-logger")

class DockerPyMonitor(Monitor):
    """Concrete class for agent monitor using DockerPy"""
    def __init__(self):
        # client = Client(base_url="unix://var/run/docker.sock")
        # result = client.inspect_container('c4e106bf9a32')
        self.container_stats = {}
        self.client = Client(base_url='unix://var/run/docker.sock')
        self.container_list = []

    def collect_host_stats(self):
        logger.info("Collecting Host statistics")

    def collect_container_stats(self, container_id):
        self.container_stats[container_id] = self._get_container_stats(container_id)
        logger.info("Collecting container stats for id %s" % container_id)
        return self.container_stats

    def collect_all_container_stats(self):
        for container in self.list_all_containers():
            id,name = container
#             print "Collecting stats for " + str(name)
            self._get_container_stats(id)
        return self.container_stats

    def stream_logs(self):
        return {}

    def list_all_containers(self):
        
        def repeat():
            mylist = []
            threading.Timer(5.0,repeat).start()
            result = self.client.containers()
            for row in result:
                idc = str(row['Id'])
                name = str(row['Names'])
                mylist.append((idc,name))
            self.container_list = mylist
#             print('Containers: \n\n' + str(self.container_list))
#             print self.container_stats.keys()
        repeat()
        # todo: Needs to be tested
        # to do : Satya : Modify this for implementing list of containers
        # threading.Timer(5.0, self.list_all_containers).start()
        # client = docker.Client(base_url='unix://var/run/docker.sock', version="1.20")
        # return client.containers()
        #return ['1234', '5678']
        return self.container_list
    def _get_container_stats(self, id):
        # to do : Satya : Modify this for implementing threading logic
        stats= self.client.stats(id, decode=True)
        for elt in stats:
            print ("status")
            self.container_stats[id] = str(elt)
            break
            
        

    
if __name__ == "__main__":
    dockMon = DockerPyMonitor()
    #dockMon.list_all_containers()
    dockMon.collect_all_container_stats()
#     print str(dockMon.container_stats.keys())
    



