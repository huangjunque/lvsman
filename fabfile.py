#coding:utf-8
from fabric.colors import red, green
from fabric.context_managers import cd
from fabric.operations import *
from fabric.api import *
import ConfigParser
from configs.config import Get_data, Add_data
import os
current_path = os.getcwd()
#master_ip = Get_data("master","ip",current_path + '/configs/config.ini').display()[0]
#slave_ip = Get_data("slave","ip",current_path + '/configs/config.ini').display()[0]
#定义角色
env.roledefs= {
	'master': ['lvs.master'],
	'slave': ['lvs.slave']
}

#env.hosts = ['192.168.1.211']
#只有slave 角色才执行host_type方法

def init_config():
	nodes_ip_tmp = []
	vips_tmp = []
	nodes_ip = os.popen("ssh lvs.master \"ipvsadm -ln\" |grep -|sed '1d'|awk '{print $2}'").readlines()
	for nodes in nodes_ip:
		node = nodes.strip()
		nodes_ip_tmp.append(node)
	nodes_ip = nodes_ip_tmp
	vips_ip = os.popen("ssh lvs.master \"ipvsadm -ln\"|grep  TCP|awk '{print $2}'").readlines()
	for vips in vips_ip:
		vip = vips.strip()
		vips_tmp.append(vip)
	vips_ip = vips_tmp
	master_ip = os.popen("grep lvs.master /etc/hosts |awk '{print $1}'").readlines()[0].strip()
	slave_ip = os.popen("grep lvs.slave /etc/hosts |awk '{print $1}'").readlines()[0].strip()
	Add_data("master", "name", "LVS-Master").add(current_path + '/configs/config.ini')
	Add_data("master", "ip", [master_ip]).add(current_path + '/configs/config.ini')
	Add_data("slave", "name", "LVS-Slave").add(current_path + '/configs/config.ini')
	Add_data("slave", "ip", [slave_ip]).add(current_path + '/configs/config.ini')
	Add_data("vip_nodes", "vip", vips_ip).add(current_path + '/configs/config.ini')
	Add_data("vip_nodes", "nodes", nodes_ip).add(current_path + '/configs/config.ini')
	Add_data("soft", "ip_v",'').add(current_path + '/configs/config.ini')
	Add_data("soft", "ke_v",'').add(current_path + '/configs/config.ini')
@roles('slave')
def host_type():
	run('uname -s')

def color():
	local('ls -l |wc -l')
	print (red("红色或者",bold=True)) \
		+ green("绿色")

def ctx_mgr():
	with cd('/var/www/'):
		run('ls')
def task_do():
	execute(host_type)
	execute(ctx_mgr)

@roles('slave')
def get_vip_port():
	with settings(
		hide('running', 'stdout', 'stderr', 'output'),
		warn_only=True
		):
		a = run("ipvsadm -ln |grep TCP |awk '{print $2}'")
		print a
		
def get_mem():
	with settings(
		hide('running', 'stdout', 'stderr', 'output'),
		warn_only=True
		):
		a = run("free | awk '/Mem/ {print int($2/1000)}'")
		print a

def get_cpu():
	with settings(
		hide('running', 'stdout', 'stderr', 'output'),
		warn_only=True
		):
		a = run('cat /proc/cpuinfo |grep processor|wc -l')
		print a

def get_cpu_mod():
	with settings(
		hide('running', 'stdout', 'stderr', 'output'),
		warn_only=True
		):
		a = run("cat /proc/cpuinfo |grep 'model name' |uniq |awk -F : '{print $2}'")
		print a

def get_ip():
	print env.hosts

@roles('master')
def get_status():
	with settings(
		hide('running', 'stdout', 'stderr', 'output'),
		warn_only=True
		):
		a = run('ipvsadm -ln')
		print a

@roles('master', 'slave')
def keep_version():
	with settings(
                hide('running', 'stdout', 'stderr', 'output'),
                warn_only=True
                ):
		a = run('keepalived -v')
		print a

@roles('master', 'slave')
def ipvsadm_version():
	with settings(
                hide('running', 'stdout', 'stderr', 'output'),
                warn_only=True
                ):
		a = run('ipvsadm -v')
		print a
