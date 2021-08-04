#!/bin/bash 
for dbname in ` mysql -uroot -p'I.lw@2020' -e "show databases;" | grep -Evi "database|infor|perfor"`
do
    mysqldump -uroot -p"123456" --events -B $dbname | gzip > /mnt/${dbname}_bak.sql.gz
done