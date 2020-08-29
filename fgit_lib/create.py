import sys
import os
from . import utils

#Create a new fGit project
def create():
	here=False
	if len(sys.argv) == 2:#'fgit create', will create a project on './<name>/.fgit'
		directory = os.getcwd()
	elif sys.argv[2]=='-h': 
		if len(sys.argv) == 4:#'fgit create -h <directory>', will create a project on '<directory>/.fgit'
			if os.path.isdir(sys.argv[3]):
				directory = sys.argv[3]
			else:
				print("There is no directory named '{}'.".format(os.path.abspath(sys.argv[3])))
				return 0
		else:#'fgit create -h', will create a project on './.fgit'
			directory = os.getcwd()
		if utils.check_dir(directory):
			print('There is already a fGit project on {}.'.format(os.path.abspath(directory)))
			return 0
		here=True
	elif os.path.isdir(sys.argv[2]):#'fgit create <directory>', will create a project on '<directory>/<name>/.fgit'
		directory = sys.argv[2]
	else:
		print("There is no directory named '{}'.".format(os.path.abspath(sys.argv[2])))
		return 0
	if os.path.isfile(os.path.join(os.getenv('HOME'), '.fgit-config')):#Check if there is file on '~/.fgit-config'
		fgit_file = open(os.path.join(os.getenv('HOME'), '.fgit-config'), 'r')
		user = fgit_file.readline()
		if user[-1:] == "\n":
			user=user[:-1]
		fgit_file.close()
	else:
		user = input('Author name: ')
	name = input('fGit project name: ')
	if not os.path.isdir(os.path.join(directory, name)) or here:
		utils.create_project(directory, name, user, here)
		if not here:
			print("Project successfully created, do 'cd '{}''to acces to it.".format(os.path.join(os.path.abspath(directory), name)))
		else:
			print("Project successfully created.")
	else:
		print("Sorry, there is already a directory named '{}'".format(os.path.join(os.path.abspath(directory), name)))