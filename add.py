#!/usr/bin/python python3
# -*- coding: UTF-8 -*-

def created(namediff):
	import string
	import re
	import os
	import sys
	
	tmpl = {}
	z = 0
	#dir = '/media/root/ARCH_201601/python_project/test/router/'
	files = [fil for fil in os.listdir(namediff.dir) if fil.endswith(('.txt'))]
	fdir = namediff.dir+files[0]
	
	read = open(fdir,'r').readlines()
	new_read = []
	for x in range(len(read)):
		if "hostname" in read[x]:
			for y in range(x,len(read)):
				new_read.append(read[y])
			else:
				break
		
	for x in range(len(new_read)):
		string = new_read[x]
		string = string.rstrip('\n')	
		print (string)
		quest1 = input ("You need to modify the line or leave as is. It is necessary to modify - 'Y', leave as is - 'N': ")
		if quest1.lower() == 'y':
			temp = {}
			temp['orig'] = string
			while quest1.lower() == 'y':
				quest2 = input ("Enter a part of a string, which is variable, is not required to take into consider. Specify strictly in line configuration: ")
				if re.search(quest2, string) == None:
					print ("Said part of the line in the template is not found.")
				else:
					if re.match('vlan (1|2)[0-9]{2}', string) == None:
						temp[quest2] = '[a-zA-Z0-9\_\-\.]{1,}'
						string = string.replace(quest2, '[a-zA-Z0-9\_\-\.]{1,}')
					else:
						if re.match ('vlan (1|2)(4|5)[0-9]', string) == None:
							temp[quest2] = '(1|2)[0-9]{2}'
							string = string.replace(quest2, '(1|2)[0-9]{2}')
						else:
							temp[quest2] = '(1|2)(4|5)[0-9]'
							string = string.replace(quest2, '(1|2)(4|5)[0-9]')
				quest1 = input ("You need to modify the line or leave as is. It is necessary to modify - 'Y', leave as is - 'N': ")
			temp['patt'] = string
			tmpl[z] = temp
			z += 1
		elif quest1.lower() != 'n':
			print ('Incorrect characters are introduced')
			sys.exit()
		else :
			temp = {}
			temp['orig'] = string
			temp['patt'] = string
			tmpl[z] = temp
			z += 1
	template_dir = (os.path.dirname(__file__)+'/template.txt')
	f = open(template_dir, 'w')
	f.write(str(tmpl))
	f.close()	
#created()
