#! /usr/bin/python
import os
import tarfile
var1 = str(os.popen('rpm -qa |grep maria').read())
os.system("yum remove -y %s" % (var1))
os.chdir(media)
