#! /usr/bin/python
#coding:utf-8

import os
db_node_c = 'db_commodity_node22'
db_node_t = 'db_transaction_node22'
sql_dir = '/opt/merchant-sql/'

os.system("mysql -uroot -p'I.lw@2020' -e \"drop database if exists %s;\"" % (db_node_c))
os.system("mysql -uroot -p'I.lw@2020' -e \"create database %s DEFAULT CHARACTER SET utf8;\"" % (db_node_c))
os.system("sed -i 's/db_commodity_node21/%s/g' %snode-c.sql" % (db_node_c,sql_dir))
#os.system("sed -i 's/db_transaction_node21/%s/g' %snode-c.sql" % (db_node_t,sql_dir))
os.system("mysql -uroot -p'I.lw@2020' %s < %s%s.sql" % (db_node_c,sql_dir,db_node_c))
