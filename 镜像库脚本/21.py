#! /usr/bin/python
#coding:utf-8

import os
dbname = os.popen("mysql -uroot -p'I.lw@2020' -h 10.20.3.44 -P 3306 -e \"show databases;\"| grep -Evi \"database|infor|perfor\"").read().strip('\n')
print(dbname)

dbnamelist = list(dbname.split('\n'))
print(dbnamelist)

for line in dbnamelist:
    print(line) 
