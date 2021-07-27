#! /usr/bin/python
#coding:utf-8
#主py文件，将所有功能都集中到这里使用。

#引用依赖包
import os
import tarfile

var1 = "5.0.7"
var2 = "Ynyc2019a@!"

#解压安装包

os.system("pwd")
os.system("tar -cvf /etc/yum.repos.d/repo.bak.tar /etc/yum.repos.d/* && rm -rf /etc/yum.repo.d/*.repo")
os.system("mv /media/gcc-761810-repo.repo /etc/yum.repo.d/gcc-761810-repo.repo && yum clean all && yum makecache")
os.system("yum install gcc -y")
os.system("yum install tcl -y")

os.chdir("/media/")
os.system("pwd")
tarfile.open("redis-%s.tar.gz" % (var1)).extractall()
tarfile.open("redis-%s.tar.gz" % (var1)).close
os.system("mv redis-%s /usr/local" % (var1))

os.chdir("/usr/local/redis-%s/" % (var1))
os.system("pwd")
os.system("make && make test")

os.system('sed -i "s/^bind 127.0.0.1/bind 0.0.0.0/" redis.conf')
os.system('sed -i "s/^protected-mode yes/protected-mode no/" redis.conf')
os.system('sed -i "s/^daemonize no/daemonize yes/" redis.conf')
os.system('sed -i "/requirepass foobared/a\requirepass %s" redis.conf ' % (var2))

requirepass Ynyc2019a@!
Huawei12#$