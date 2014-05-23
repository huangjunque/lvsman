#!/usr/bin/env python

import os
import ConfigParser

class Get_data:
    def __init__(self,project,list,config_file_path):
        'get data from config.ini'
        dataConfig = ConfigParser.ConfigParser()
        dataConfig.read(config_file_path)

        self.data = dataConfig.get(project,list)
        self.data = self.data[1:-1]
        self.data = self.data.replace("'","")
	self.data = self.data.replace(" ","")
        self.data = self.data.strip()
        self.data = self.data.split(',')

    def display(self):
        return self.data

class Add_data:
     """docstring for Add_data"""
     def __init__(self, section,option,value):
         #conf = ConfigParser.ConfigParser()
         self.section = section
         self.option = option
         self.value = value
     def add(self, new_config_file_path):
        if os.path.isfile(new_config_file_path):
            pass
        else:
            #os.mknod(new_config_file_path)
            open(new_config_file_path,"w")
        conf = ConfigParser.ConfigParser()
        conf.read(new_config_file_path)
        all_section = conf.sections()
        #print all_section
        if self.section in all_section:
            conf.set(self.section,self.option,self.value)
            conf.write(open(new_config_file_path,"w"))
        else:
            conf.add_section(self.section)
            conf.set(self.section, self.option, self.value)
            conf.write(open(new_config_file_path,"w"))
