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
str1 = "[mysqld]\ndatadir=/\nsocket=/var/lib/mysql/mysql.sock\n\nsymbolic-links=0\n\noptimizer_switch='derived_merge=off'\n\nsql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION\n\nmax_connections=1024\n\ncharacter_set_server=utf8\ninit_connect='SET NAMES utf8'\nport=5575\nlower_case_table_names=1\n\n[mysqld_safe]\nlog-error=/var/log/mysqld.log\npid-file=/var/run/mysqld/mysqld.pid\n\nserver-id = 1111\n\nlog_bin = mysql-bin\nbinlog_format = row\nbinlog_row_image = full\n\nexpire_logs_days = 10\n"
str2 = str(os.popen("ifconfig ens192 |grep netmask|awk '{print $2}'|awk -F. '{print $3$4}'").read().splitlines())
mysql_conf = "/etc/my.cnf"

#备份及修改配置文件
os.system("cp /etc/my.cnf /etc/my.cnf.old")
os.system("echo >/etc/my.cnf")
f = open("/etc/my.cnf","w")
f.write(str1)
f.close

#使用shell模块，对配置文件进行修改

#使用shell模块，启动mysqld
os.system("service mysqld start")

#启动mysqld后，awk或者grep获取默认password
var3 = str(os.popen('cat /var/log/mysqld.log |grep "temporary password"|awk '{print $11}'').os.read())
str3 = "use mysql;\nalter user root@localhost identified by 'I.lw@2020';\ndelete from mysql.user where user!='root' or host!='localhost';\ngrant all on *.* to root@'%' identified by 'I.lw@2020';\nflush privileges;"

#生成初始化sql文件
f2 = open("/media/mysql-ini.sql","w")
f2.write(str3)
f2.close

#执行初始化文件
os.system("mysql -u root -p$var3 -h localhost < /media/mysql-ini.sql")
os.system("service mysqld restart")
################################################
#修改my.cnf文件（可加循环：若不存在某行配置，则新增，否则保持）
#需要新增的配置：datadir、engine、bin-log

#首次启动mysqld，生成默认password
#启动mysqld后，awk或者grep获取默认password
#var3 = str(os.popen('cat /var/log/mysqld.log |grep "temporary password"|awk '{print $11}''))

#使用至少两个变量，第一个是默认password，第二个是自定义password
#方式一：使用变量作为参数，使用安全脚本进行安装，指定数据库密码
#方式二：使用默认密码登录参数，通过各种mysql设置命令修改密码、用户权限、端口等。

#重启mysql



