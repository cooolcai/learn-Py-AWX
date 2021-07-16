#! /usr/bin/python
#coding:utf-8
#可用于卸载mariadb-lib依赖包，也可卸载其它软件包
import os
var1 = str(os.popen('rpm -qa |grep tree').read())
os.system("yum remove -y %s" % (var1))
print (type(var1))
print var1