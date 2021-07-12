#! /usr/bin/python
import os
dir = '/root'
dir2 = '/tmp'
os.system("ls %s ; ls %s" % (dir,dir2))
#直接定义变量，使用str类型，在执行os.system时不会报错。
#但是os.system执行完后会有一个返回值： 0
#于是，判断console上的返回值并不是os.system的返回值。
