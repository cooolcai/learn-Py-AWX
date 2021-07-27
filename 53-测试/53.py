#coding:utf-8
import os

#启动mysqld后，awk或者grep获取默认password
var3 = str(os.popen("cat /var/log/mysqld.log |grep 'temporary password'|awk '{print $11}'").read().strip('\n'))
str3 = "alter user root@localhost identified by 'I.lw@2020';\nuse mysql;\ndelete from mysql.user where user!='root' or host!='localhost';\ngrant all on *.* to root@'%' identified by 'I.lw@2020';\nflush privileges;"

#生成初始化sql文件
f2 = open("/media/mysql-ini.sql","w")
f2.write(str3)
f2.close

#执行初始化文件
os.system("mysql --connect-expired-password -u root -p'%s' -h localhost < /media/mysql-ini.sql" % (var3))
os.system("service mysqld restart")
