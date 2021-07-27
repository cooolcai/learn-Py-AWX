import os

""" str1 = '''[mysqld]
datadir=/
socket=/var/lib/mysql/mysql.sock

symbolic-links=0

optimizer_switch='derived_merge=off'

sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION

max_connections=1024

character_set_server=utf8
init_connect='SET NAMES utf8'
port=5575
lower_case_table_names=1

[mysqld_safe]
log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid

server-id = 1111

log_bin = mysql-bin
binlog_format = row
binlog_row_image = full

expire_logs_days = 10''' """

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
