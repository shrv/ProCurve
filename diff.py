#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import string
import argparse
import os
import add
import conf
import re

def Parser():
	parser = argparse.ArgumentParser(description = "The Program for identity control configuration files of route HP ProCurve", epilog = "")
	parser.add_argument ('-t', '--template', required = False, type = str, help = 'Specify the folder and name of the template file, the default name TEMPLATE.TXT and parent directory. If the file was not created, the parameter point is not required.')
	parser.add_argument ('-d', '--dir', required = True, type = str,help = 'Specify the folder with the router configuration files')
	
	return parser

parser = Parser()
namediff = parser.parse_args(sys.argv[1:])

if namediff.template == None:
	template = (os.path.dirname(__file__)+'/template.txt')
else:
	template = namediff.template
files = [fil for fil in os.listdir(namediff.dir) if fil.endswith(('.txt'))]

if (len(files)) == 0:
	print ('In "'+namediff.dir+'" directory configuration files not found')
	sys.exit()
if (os.path.isfile(template)) == False:
	template = (os.path.split(template))
	print ('In directory "'+template[0]+'" file "'+template[1]+'" not found')
	quest_add_template = input ('You want to create a template?[y/n]')
	if quest_add_template.lower() == 'n':
		sys.exit()
	elif quest_add_template.lower() != 'y':
		print ('An invalid symbol')
		sys.exit()
	else:
		add.created(namediff)
else:
	conf.check()

