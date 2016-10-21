#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import string
import re
import os
import sys
import argparse

def created(namediff):

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
		flag = 0 
		world = 0
		for j in string:
			if j != ' ' and flag == 0:
				world += 1
				flag =1
			elif j == ' ':
				flag = 0	
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
					if re.match('\d{1,4}$', quest2) != None:
						lenght = len(str(quest2))
						temp[quest2] = '[0-9]{'+str(lenght)+'}'
						print (temp[quest2])
						string = string.replace(quest2, temp[quest2])
					else:
						if re.match ('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$', quest2) != None:
							temp[quest2] = '[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}'
							string = string.replace(quest2, '[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}')
						else:
							temp[quest2] = '[a-zA-Z0-9_-.,]{1,}'
							string = string.replace(quest2, '[a-zA-Z0-9_-.,]{1,}')
				quest1 = input ("Wanted more changes in the line: \""+original+"\". It is necessary to modify - 'Y', leave as is - 'N': ")
			temp['patt'] = string
			temp['wrld'] = world
			temp['mod'] = 1
			tmpl[z] = temp
			z += 1
			x += 1
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

def add_del():
	def Parserad():
		parserad = argparse.ArgumentParser(description = "The Program for identity control configuration files of route HP ProCurve. Manually adding or deleting rows into an existing template.", epilog = "")
		parserad.add_argument ('-t', '--template', required = True, type = str, help = 'Specify the folder and name of the template file. Example: -t /usr/share/template.txt. Required parameter.')
		parserad.add_argument ('-nr', '--newrows', required = False, type = str, help = 'Copy the string to add. If, for example, you need to add interface or vlan configure. Adding customization interface as one line. Exmaple: interface 24 broadcast-limit 25 exit ')	
		parserad.add_argument ('-ac', '--action', required = True, type = str, choices = ['add', 'del'], help = 'select the action "add" - add a string or "del" - remove the line. Required parameter.')
		return parserad

	parserad = Parserad()
	nameadd = parserad.parse_args(sys.argv[1:])
	pattern = {}

	if nameadd.action.lower() == 'add':
		
		fil = open(nameadd.template, 'r')
		pattern = fil.readlines()
		fil.close()
		pattern[0]
		print (pattern.get('0'))
#		print (pattern)

	else:
		sys.exit()
		
if __name__ == '__main__':
	add_del()
