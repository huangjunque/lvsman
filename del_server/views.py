#coding:utf-8
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect
from configs.config import Get_data, Add_data
import os

current_path = os.getcwd()
def play(request):
	vip_port = Get_data("vip_nodes","vip",current_path + '/configs/config.ini').display()
	node_ips = Get_data("vip_nodes","nodes",current_path + '/configs/config.ini').display()
	return render_to_response('play.html', {
		'title':'删的就是你',
		'vip_port':vip_port,
		'node_ips':node_ips
		})
def del_vip(request):
	check_box_list = request.REQUEST.getlist("check_box_list")
	now_vip = Get_data("vip_nodes","vip",current_path + '/configs/config.ini').display()
	for ip in check_box_list:
		now_vip.remove(ip)
	Add_data("vip_nodes","vip",now_vip).add(current_path + '/configs/config.ini')
	#return HttpResponseRedirect('/play_vip/', context_instance = RequestContext(request))
	return HttpResponseRedirect('/play/')
def del_node(request):
	check_box_list = request.REQUEST.getlist("check_box_list_1")
	now_node_ip = Get_data("vip_nodes","nodes",current_path + '/configs/config.ini').display()
	for ip in check_box_list:
		now_node_ip.remove(ip)
	Add_data("vip_nodes","nodes",now_node_ip).add(current_path + '/configs/config.ini')
	return HttpResponseRedirect('/play/')