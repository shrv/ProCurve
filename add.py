#!/usr/bin/python
# -*- coding: UTF-8 -*-

def created():
	import string
	import re
	import os
	import sys
	
	dir = '/home/frankk/python/python_project/test/router/'
	files = [fil for fil in os.listdir(dir) if fil.endswith(('.txt'))]
	fdir = dir+files[0]
	
	read = open(fdir,'r').readlines()
	new_read = []
	for x in range(len(read)):
		if "hostname" in read[x]:
			for y in range(x,len(read)):
				new_read.append(read[y])
			else:
				break
		
	for x in range(len(new_read)):
		print (new_read[x])	
		quest1 = input ("You need to modify the line or leave as is. It is necessary to modify - 'Y', leave as is - 'N'")
		if quest1.lower() == 'y':
			print ('Y')
		elif quest1.lower() != 'n':
			print ('Incorrect characters are introduced')
			sys.exit()
		else :
			print ('N')
		
created()
