#coding:utf-8
from django.shortcuts import render_to_response
from configs.config import Get_data
import os


def index(req):
	current_path = os.getcwd()
	get_data = Get_data("nodes_port","443_ip",current_path + '/configs/config.ini')
	master_ip = get_data.display()
	return render_to_response('index.html',{'title':'状态','master_ip':master_ip})