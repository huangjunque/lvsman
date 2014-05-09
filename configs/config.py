import ConfigParser

class Get_data:
    def __init__(self,project,list,config_file_path):
        'get data from config.ini'
        dataConfig = ConfigParser.ConfigParser()
        dataConfig.read(config_file_path)

        self.data = dataConfig.get(project,list)
        self.data = self.data[1:-1]
        self.data = self.data.split(',')

    def display(self):
        return self.data
