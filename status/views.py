#coding:utf-8
from django.shortcuts import render_to_response
from configs.config import Get_data, Add_data
import os


def status(req):
	current_path = os.getcwd()
	mastername = Get_data("master","name",current_path + '/configs/config.ini').display()
	masterip = Get_data("master","ip",current_path + '/configs/config.ini').display()
	slavename = Get_data("slave","name",current_path + '/configs/config.ini').display()
	slaveip = Get_data("slave","ip",current_path + '/configs/config.ini').display()
	vip_port = Get_data("vip_nodes","vip",current_path + '/configs/config.ini').display()
	nodes_ip_port = Get_data("vip_nodes","nodes",current_path + '/configs/config.ini').display()
	keep_version =  Get_data("soft","ke_v",current_path + '/configs/config.ini').display()
	ipvsadm_version = Get_data("soft","ip_v",current_path + '/configs/config.ini').display()
	#print keep_version
	#print ipvsadm_version
	keep_version_tmp = []
	ipvsadm_version_tmp = [] 
	if keep_version == [''] and ipvsadm_version == ['']:
		keep_version = os.popen("fab keep_version |grep Kee|awk '{print $1,$2}'").readlines()
		for lines in keep_version:
			line = lines.strip('\'\n')
			keep_version_tmp.append(line)
			keep_version = keep_version_tmp		
		ipvsadm_version = os.popen("fab ipvsadm_version |grep IPVS").readlines()
		for lines in ipvsadm_version:
			line = lines.strip('\'\n')
			ipvsadm_version_tmp.append(line)
			ipvsadm_version = ipvsadm_version_tmp

		Add_data("soft","ke_v",keep_version).add(current_path + '/configs/config.ini')
		Add_data("soft","ip_v",ipvsadm_version).add(current_path + '/configs/config.ini')
		keep_version =  Get_data("soft","ke_v",current_path + '/configs/config.ini').display()
		ipvsadm_version = Get_data("soft","ip_v",current_path + '/configs/config.ini').display()
		return render_to_response('status.html',{'title':'状态',
			'masterip':masterip,
			'mastername':mastername,
			'slaveip':slaveip,
			'slavename':slavename,
			'vip':vip_port,
			'nodes':nodes_ip_port,
			'keep_version':keep_version,
			'ipvsadm_version':ipvsadm_version
			})
	else:		
		return render_to_response('status.html',{'title':'状态',
			'masterip':masterip,
			'mastername':mastername,
			'slaveip':slaveip,
			'slavename':slavename,
			'vip':vip_port,
			'nodes':nodes_ip_port,
			'keep_version':keep_version,
			'ipvsadm_version':ipvsadm_version
			})