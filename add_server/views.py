#coding:utf-8
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from configs.config import Get_data, Add_data
import os

def add_vip(request):
	return render_to_response('add_vip.html',
		{
		'title':'添加VIP'
		})

def add_node(request):
	return render_to_response('add_node.html',
		{
		'title':'添加后端节点服务器'
		})

def add_vip_data(request):
	if 'vip' and 'scheduler' in request.GET:
		vip_now = request.GET['vip']
		scheduler_now = request.GET['scheduler']
		status = os.system("fab add_vip:ip=%s,scheduler=%s" % (vip_now,scheduler_now))
		os.system("fab init_config")
		if status == 0:
			return HttpResponseRedirect('/play/')
		else:
			return HttpResponse('添加失败')
	else:
		return HttpResponse('信息不完整2个空必填')

def add_node_data(request):
	dic = {'DR':'-g', 'TUN':'-i', 'NAT':'-m'}
	if 'vip' and 'node' and 'select' in request.GET:
		vip_now = request.GET['vip']
		node_now = request.GET['node']
		model = request.GET['select']
		model_now = dic[model]
		weight_now = request.GET['weight']
		status = os.system("fab add_node:vip=%s,node=%s,model=%s,weight=%s" % (vip_now,node_now,model_now,weight_now))
		os.system("fab init_config")
		if status == 0:
			return HttpResponseRedirect('/play/')
		else:
			return HttpResponse('添加失败')
	else:
		return HttpResponse('信息不完整')