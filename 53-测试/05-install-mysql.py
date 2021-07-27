#! /usr/bin/python
#coding:utf-8
#可用于卸载mariadb-lib依赖包，也可卸载其它软件包
import os
import os.path

#解决maria依赖冲突问题
var1 = str(os.popen('rpm -qa |grep tree').read())
print var1
if var1 == "":
    print "no dependency problem"
else:
    os.system("yum remove -y %s" % (var1))
    print "dependency problem is ok"

#创建数据目录
mysql_data = "/data/mysql-data/"
if os.path.exists(mysql_data): 
    print "/data/mysql is exist!"
else:
    os.makedirs(mysql_data)
    print "/data/mysql is crated"

#检查端口占用
""" mysql_port = str(os.popen("netstat -ntl| awk '{print $4}' |grep '8443'|awk -F: '{print $4}'").strip.read())
print mysql_port
if mysql_port == "8443":
    print "port is in used,failed!"
else:
    print "port is available，ok!"   
 """

#关闭selinux 
os.system("sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config")
os.system("setenforce 0")

#修改my.cnf文件
#获取server-id

#备份my.cnf文件
str1 = "[mysqld]\ndatadir=/\nsocket=/var/lib/mysql/mysql.sock\n\nsymbolic-links=0\n\noptimizer_switch='derived_merge=off'\n\nsql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION\n\nmax_connections=1024\n\ncharacter_set_server=utf8\ninit_connect='SET NAMES utf8'\nport=5575\nlower_case_table_names=1\n\n[mysqld_safe]\nlog-error=/var/log/mysqld.log\npid-file=/var/run/mysqld/mysqld.pid\n\nserver-id = 1111\n\nlog_bin = mysql-bin\nbinlog_format = row\nbinlog_row_image = full\n\nexpire_logs_days = 10\n"
str2 = str(os.popen("ifconfig ens192 |grep netmask|awk '{print $2}'|awk -F. '{print $3$4}'").read().splitlines())

mysql_conf = "/etc/my.cnf"
""" if os.path.exists(mysql_conf): 
    os.system("cp /etc/my.cnf /etc/my.cnf.old")
    os.system("echo >/etc/my.cnf")
    f = open("/etc/my.cnf","w")
    f.write(str1)
    f.close """
os.system("cp /etc/my.cnf /etc/my.cnf.old")
os.system("echo >/etc/my.cnf")
f = open("/etc/my.cnf","w")
f.write(str1)
f.close