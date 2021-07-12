#! /usr/bin/python
import os
var1 = str(os.popen('rpm -qa |grep maria').read())
os.system("yum remove -y %s" % (var1))