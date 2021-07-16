#! /usr/bin/python
#coding:utf-8
#主py文件，将所有功能都集中到这里使用。

import os
import tarfile
var1 = str(os.popen('rpm -qa |grep maria').read())
os.system("yum remove -y %s" % (var1))
os.chdir("/media")
os.system("pwd")