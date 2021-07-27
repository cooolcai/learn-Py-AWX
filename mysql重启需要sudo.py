#! /usr/bin/python
#coding:utf-8
import os

os.system("sudo service mysqld restart")
os.system("service firewalld stop")
str3 = str(os.popen("netstat -ano |grep 5575").read().strip('\n'))
str4 = str(os.popen("service firewalld status|grep Active").read().strip('\n'))
print(str3)
print(str4)
