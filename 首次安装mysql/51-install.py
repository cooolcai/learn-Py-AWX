#! /usr/bin/python
#coding:utf-8
#主py文件，将所有功能都集中到这里使用。

#引用依赖包
import os
import tarfile

#卸载与mysql冲突的maria依赖包（此处可加排除逻辑：若存在则卸载，否则跳过）
var1 = str(os.popen('rpm -qa |grep maria').read())
os.system("yum remove -y %s" % (var1))

#解压安装包
os.chdir("/media")
os.system("pwd")
tarfile.open("mysql-5.7.31-1.el7.x86_64.rpm-bundle.tar").extractall()
tarfile.open("mysql-5.7.31-1.el7.x86_64.rpm-bundle.tar").close

#按顺序离线安装rpm文件
var2 = "5.7.31"
os.system("rpm -ivh mysql-community-common-%s-1.el7.x86_64.rpm" % (var2))
os.system("rpm -ivh mysql-community-libs-%s-1.el7.x86_64.rpm" % (var2))
os.system("rpm -ivh mysql-community-libs-compat-%s-1.el7.x86_64.rpm" % (var2))
os.system("rpm -ivh mysql-community-client-%s-1.el7.x86_64.rpm" % (var2))
os.system("rpm -ivh mysql-community-server-%s-1.el7.x86_64.rpm" % (var2))

#创建数据目录
mysql_data = "/data/mysql-data/"
if os.path.exists(mysql_data):
    print "/data/mysql is exist!"
else:
    os.makedirs(mysql_data)
    print "/data/mysql is crated"

#关闭selinux
os.system("sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config")
os.system("setenforce 0")

#配置文件默认模板
str1 = "[mysqld]\ndatadir=/data/mysql-data\nsocket=/var/lib/mysql/mysql.sock\n\nsymbolic-links=0\n\noptimizer_switch='derived_merge=off'\n\nsql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION\n\nmax_connections=1024\n\ncharacter_set_server=utf8\ninit_connect='SET NAMES utf8'\nport=5575\nlower_case_table_names=1\n\n[mysqld_safe]\nlog-error=/var/log/mysqld.log\npid-file=/var/run/mysqld/mysqld.pid\n\nserver-id = 1111\n\nlog_bin = mysql-bin\nbinlog_format = row\nbinlog_row_image = full\n\nexpire_logs_days = 10\n"
str2 = str(os.popen("ifconfig ens192 |grep netmask|awk '{print $2}'|awk -F. '{print $3$4}'").read().splitlines())
mysql_conf = "/etc/my.cnf"

#备份及修改配置文件
os.system("cp /etc/my.cnf /etc/my.cnf.old")
os.system("echo >/etc/my.cnf")
f = open("/etc/my.cnf","w")
f.write(str1)
f.close

#修改配置文件后重启mysql，检查是否生效
os.system("sudo service mysqld restart")
str3 = str(os.popen("netstat -ano |grep 5575").read().strip('\n'))
print(str3)
