#!/usr/bin/python
import tarfile
import os

def get_file_name(file_dir):
	L=[]
	for root,dirs,files in os.walk(file_dir):
		for file in files:
			#print(file)
			L.append(file)
            print(L)
	return L
