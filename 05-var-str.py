#! /usr/bin/python
import os
var1 = str(os.popen('rpm -qa |grep maria').read())
#os.system("yum remove %s -y" % (var1))
print (type(var1))
print var1