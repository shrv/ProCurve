#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def created(namediff):
	import string
	import re
	import os
	import sys
	
	tmpl = {}
	z = 0
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
	
	x = 0	
	while x < len(new_read):
		if x < (len(new_read)-1):	
			if re.match (' ',new_read[x+1]) == None:
				string = new_read[x]
				string = string.rstrip('\n')
			else:
				string = new_read[x]
				string = string.rstrip('\n')
				x = x + 1
				string += new_read[x]
				string = string.rstrip('\n')
				while x < len(new_read) and re.search ('exit', new_read[x+1]) == None:
					x = x + 1
					string += new_read[x]
					string = string.rstrip('\n')
				x = x + 1
				string += ' '+new_read[x]
				string = string.rstrip('\n')
		else:
			string = new_read[x]
			string = string.rstrip('\n')	
		original = string
		world = len(original.split(' '))	
		print ("\n")
		print ("=================")
		print ("string: "+string)
		quest1 = input ("You need to modify the line or leave as is in string: \""+original+"\". It is necessary to modify - 'Y', leave as is - 'N': ")
		if quest1.lower() == 'y':
			temp = {}
			temp['orig'] = string
			while quest1.lower() == 'y':
				quest2 = input ("Enter a part of a string \""+original+"\" , which is variable, is not required to take into consider. Specify strictly in line configuration: ")
				print ("\n")
				if re.search(quest2, string) == None:
					print ("Said part of the line in the template is not found.")
				elif re.search('\s', quest2) != None:
					print ("It is impossible to replace immediately in line to specify two or more words or a set of numbers.\n Specifies whether one word. For instance vlan 412, you must first vlan, and then 412.\n")
				else:
					if re.match('vlan (1|2)[0-9]{2}', string) == None:
						temp[quest2] = '[a-zA-Z0-9\_\-\.\,]{1,}'
						string = string.replace(quest2, '[a-zA-Z0-9\_\-\.\,]{1,}')
					else:
						if re.match ('vlan (1|2)(4|5)[0-9]', string) == None:
							temp[quest2] = '(1|2)[0-9]{2}'
							string = string.replace(quest2, '(1|2)[0-9]{2}')
						else:
							temp[quest2] = '(1|2)(4|5)[0-9]'
							string = string.replace(quest2, '(1|2)(4|5)[0-9]')
				quest1 = input ("Wanted more changes in the line: \""+original+"\". It is necessary to modify - 'Y', leave as is - 'N': ")
			temp['patt'] = string
			temp['wrld'] = world
			temp['mod'] = 1
			tmpl[z] = temp
			z += 1
		elif quest1.lower() != 'n':
			print ('Incorrect characters are introduced')
			sys.exit()
		else :
			temp = {}
			temp['orig'] = string
			temp['patt'] = string
			temp['wrld'] = world
			temp['mod'] = 0
			tmpl[z] = temp
			z += 1
			x += 1
	template_dir = (os.path.dirname(__file__)+'/template.txt')
	f = open(template_dir, 'w')
	f.write(str(tmpl))
	f.close()	
