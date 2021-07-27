#! /usr/bin/python
#coding:utf-8
import os

os.system("sudo service mysqld restart")
str3 = str(os.popen("netstat -ano |grep 5575").read().strip('\n'))
print(str3)
