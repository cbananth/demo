
class Model(object):
    def __init__(self, cid):
        self.model_stats= {}
        self.cid = cid
    def create_model(self):
        self.model_stats = {
            self.cid : {
                    'cpu' : {},
                    'network' : {},
                    'disk' : {},
                    'memory' : {}
            }
        }
    def set_stats(self, key_class, statsdict):
        self.model_stats[self.cid][key_class] = statsdict
    
    def get_stats(self):
        return self.model_stats

if __name__ == "__main__":
    mod = Model()
    mod.create_model()
    mod.set_stats('cpu', 'precpu_stat', {'system_cpu' : 1, 'kernel_cpu' : 2})
    print mod.get_stats()