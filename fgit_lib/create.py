import sys
import os
from . import utils

def h(directory):
	return utils.check_dir(directory)

def t(directory):
	return os.path.isdir(directory)

def n(directory, name, here):
	return not os.path.isdir(os.path.join(directory, name)) or here

#Create a new fGit project
def create():
	here=False
	name=''
	directory=os.getcwd()
	if len(sys.argv) == 2:#'fgit create'
		directory = os.getcwd()
	else:
		args=[i[:3] for i in sys.argv[2:]]
		for i in args:
			if not i in ['-h', '-t=', '-n=']:
				print("{}Unknow parameter: '{}'.".format(utils.Colors.error, sys.argv[args.index(i)+2]))
				return 0
		if '-t=' in args:#Change the target directory
			if t(sys.argv[args.index('-t=')+2][3:]):
				directory=sys.argv[args.index('-t')+2][3:]
			else:
				print("{}There is no directory named '{}'.".format(utils.Colors.error, os.path.abspath(sys.argv[args.index('-t=')+2][3:])))
				return 0
		if '-h' in args:#Just Here ! You don't see it ?
			here=True
			if h(directory):
				print("{}There is already a fGit project on '{}'.".format(utils.Colors.error, os.path.abspath(directory)))
				return 0
		if '-n=' in args:
			if n(directory, sys.argv[args.index('-n=')+2][3:], here):
				name=sys.argv[args.index('-n=')+2][3:]
			else:
				print("{}There is already a directory named '{}'.".format(utils.Colors.error, os.path.abspath(sys.argv[args.index('-n=')+2][3:])))
				return 0
	if os.path.isfile(os.path.join(os.getenv('HOME'), '.fgit-config')):#Check if there is file on '~/.fgit-config'
		fgit_file = open(os.path.join(os.getenv('HOME'), '.fgit-config'), 'r')
		user = fgit_file.readline()
		if user[-1:] == "\n":
			user=user[:-1]
		fgit_file.close()
	else:
		user = input('fGit creator name: ')
	if name == '':
		name = input('fGit project name: ')
	if n(directory, name, here):
		utils.create_project(directory, name, user, here)
		if not here:
			print("{1}Project successfully created, do {2}'cd '{0}''{1}to acces to it.{2}".format(os.path.join(os.path.abspath(directory), name), utils.Colors.green, utils.Colors.stop))
		else:
			print("Project successfully created.")
	else:
		print("{1}There is already a directory named '{0}'".format(os.path.join(os.path.abspath(directory), name), utils.Colors.error))