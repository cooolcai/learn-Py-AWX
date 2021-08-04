#! /usr/bin/python
#coding:utf-8
#主py文件，将所有功能都集中到这里使用。

#引用依赖包
import os
zbx_server = '192.168.101.229'
zbx_server_active = '192.168.101.229:10050'
zbx_rpm = 'zabbix-agent-5.0.14-1.el7.x86_64.rpm'
zbx_agent = str(os.popen('rpm -qa |grep zabbix-agent').read().strip('\n'))
print(zbx_agent)

if zbx_agent != '':
    os.system("sed -i '117 aServer=%s' /etc/zabbix/zabbix_agentd.conf" % (zbx_server))
    os.system("sed -i '158 aServerActive=%s' /etc/zabbix/zabbix_agentd.conf" % (zbx_server_active))
    os.system("service zabbix-agent restart")
    print(os.system("service zabbix-agent status"))
    zbx_check_1 = str(os.popen('service zabbix-agent status|grep Active|awk \'{print $1$2$3}y\'').read().strip('\n'))
    if zbx_check_1 != 'Active:active(running)':
        print("zbx-agt start failed,please check the conf file!")
else:
    os.system("rpm -ivh /media/zbx-agt/%s" % (zbx_rpm))
    os.system("sed -i 's/Server=127.0.0.1/Server=%s/g' /etc/zabbix/zabbix_agentd.conf" % (zbx_server))
    os.system("sed -i 's/ServerActive=127.0.0.1/ServerActive=%s/g' /etc/zabbix/zabbix_agentd.conf" % (zbx_server_active))
    os.system("service zabbix-agent start && systemctl enable zabbix-agent")
    zbx_check_2 = str(os.popen('service zabbix-agent status|grep Active|awk \'{print $1$2$3}y\'').read().strip('\n'))
    if zbx_check_2 != 'Active:active(running)':
        print("zbx-agt start failed,please check the conf file!")
    print(os.system("service zabbix-agent status"))
