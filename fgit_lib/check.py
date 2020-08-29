import sys
import os
from . import utils

#Check if the directory contain a '.fgit' project
#if there are no directory gave, check the working directory
def check():
	if len(sys.argv) == 2:
		if utils.check_dir(os.getcwd()):
			print('Yes, There is a fGit project here.')
		else:
			print('No, There is no fGit project here.')
	elif sys.argv[2][:3] == '-t=':
		if os.path.isdir(sys.argv[2]):
			if utils.check_dir(sys.argv[2][3:]):
				print('Yes, There is a fGit project in {}.'.format(os.path.abspath(sys.argv[2][3:])))
			else:
				print('No, There is no fGit project in {}.'.format(os.path.abspath(sys.argv[2][3:])))
		else:
			print("{}There is no directory named '{}'.".format(utils.Colors.error, os.path.abspath(sys.argv[2][3:])))
	else:
		print("{}Unknow argument : '{}'.".format(utils.Colors.error, sys.argv[2]))