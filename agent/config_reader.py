import ConfigParser


class ConfigReader(object):

    def __init__(self, config_file):
        self.conf_parser = ConfigParser.ConfigParser()
        self.conf_parser.read(config_file)
        self.config = {}

    def load_config(self):
        for section in self.conf_parser.sections():
            for option in self.conf_parser.options(section):
                self.config[option] = self.conf_parser.get(section, option)
        return self.config

if __name__ == "__main__":

    cr = ConfigReader("config.txt")
    print cr.load_config()
