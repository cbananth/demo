from stats_monitor import Monitor
from docker import Client
import threading
import logging
import mondb
from model import Model
import datetime
import time

# import time

logger = logging.getLogger("agent-logger")

class DockerPyMonitor(Monitor):
    """Concrete class for agent monitor using DockerPy"""
    def __init__(self):
        self.container_stats = {}
        self.client = Client(base_url='unix://var/run/docker.sock')
        self.container_list = []

    def collect_host_stats(self):
        logger.info("Collecting Host statistics")

    def collect_container_stats(self, container_id):
        dbclient = mondb.MonDB()
        st = StatsThread(self.client, dbclient)
        self.container_stats = st.container_stats
        #time.sleep(20)

    def collect_all_container_stats(self):
        for cid in self.list_all_containers():
            print cid
            self._get_container_stats(cid)
        return self.container_stats

    def stream_logs(self):
        return {}

    def list_all_containers(self):
        
        def repeat():
            mylist = []
            idlist = []
            threading.Timer(5.0,repeat).start()
            result = self.client.containers()
            for row in result:
                idc = str(row['Id'])
                name = str(row['Names'])
                mylist.append((idc,name))
                idlist.append(idc)
            self.container_list = idlist
        repeat()
        return self.container_list
            
    def _docker_info (self):
        info= self.client.info()
        print info
    
if __name__ == "__main__":
    dockMon = DockerPyMonitor()
    #dockMon.list_all_containers()
    #dockMon.collect_all_container_stats()
    #dockMon.docker_info()
#     print str(dockMon.container_stats.keys())
    
class StatsThread(object):
    def __init__(self, client, dbclient):
        self.client = client
        self.ids = []
        self.container_stats = {}
        self.statslist = []
        self.statsdict = {}
        self.dbclient = dbclient
        self.container_stats = self.thread_list_container()

    def thread_list_container(self):
        statsdict = {}
        def repeat():
            idc = ""
            name = ""
            try:
                threading.Timer(5.0,repeat).start()
                result = self.client.containers()
                for row in result:
                    idc = str(row['Id'])
                    name = str(row['Names'])
                    print "name = " + str(name)
                    stats = self.stats_repeat(idc)
                    statsdict = self.populate_model(stats, idc, name)
            except Exception as e:
                pass
            except TypeError as t:
                pass
        repeat()
        return statsdict
    
    def stats_repeat(self, cid):
        try:
            threading.Timer(30.0,self.stats_repeat).start()
            stats = self.client.stats(cid, decode=True).next()
            return stats
        except Exception as e:
            pass
        except TypeError as t:
            pass
#         for elt in stats:
#             print "%s %s %s " % ("*" * 25, cid, "*" * 25)
#             print stats[elt]
#             print "%s %s %s " % ("*" * 25, cid, "*" * 25)

    def populate_model(self, stats, cid, name):
        model = Model(cid)
        model.create_model()
        statsdict = {}
        def get_statslist(stats):
            for key in stats.keys():
                if isinstance(stats[key], dict):
                    get_statslist(stats[key])
                else:
                    statsdict[key] = stats[key]
        for key in stats.keys():
            if str(key) == "cpu_stats":
                get_statslist(stats[key])
                model.set_stats('cpu', statsdict)
            if str(key) == "network":
                get_statslist(stats[key])
                model.set_stats('network', statsdict)
            if str(key) == "memory_stats":
                get_statslist(stats[key])
                model.set_stats('memory', statsdict)
            if str(key) == "blkio_stats":
                get_statslist(stats[key])
                model.set_stats('disk', statsdict)

        for key in model.model_stats[model.cid].keys():
            points = model.model_stats[model.cid][key]
            #print points
            json_data = self.get_json_data(points, key, model.cid, name)
            self.dbclient.write_series(json_data) 
        print model.model_stats
        #print str(self.dbclient.read_series("select * from cpu_load_short"))
        return model.model_stats
        
    
    def get_json_data(self, points, key, cid, name):
#         print points
#         points_data = {}
#         i = 0
        print name
        for pk in points.keys():
            points[pk] = str(points[pk])
#             i = i+1
#             if i>7:
#                 break
        print key
        print cid
        print points
        json_data = [
        {
            "measurement": key,
#             Optionally tags can be passed here if not sent as a method argument
            "tags": {'id' : cid, 'name' : str(name)},
#             "time": "2009-11-10T23:00:00Z",
             "fields": points,
        }]
        
        return json_data
        


