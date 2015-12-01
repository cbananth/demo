'''
Created on 27-Oct-2015

@author: root
'''
from influxdb import InfluxDBClient as dbclient

class MonDB(object):
    def __init__(self):
        self.db = dbclient("localhost", 8086, "root", "root", database="dockstats",timeout=3)
    
    def write_series(self, data={}, database=None):
#         data = [
#         {
#             "measurement": "cpu_statistics",
#             Optionally tags can be passed here if not sent as a method argument
#             "tags": {
#                 "id": "12345"
#             },
#             "time": "2009-11-10T23:00:00Z",
#             "fields": {
#                 "value": 0.64
#             }
#         }]
        self.db.write_points(data, time_precision='s', database=database, retention_policy="default")
    
    def read_series(self, query):
        result = self.db.query(query)
        print str(result)

if __name__ == "__main__":
    mondb = MonDB()
    mondb.read_series("select * from cpu")
