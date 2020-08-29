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
	else:
		if os.path.isdir(sys.argv[2]):
			if utils.check_dir(sys.argv[2]):
				print('Yes, There is a fGit project in {}.'.format(os.path.abspath(sys.argv[2])))
			else:
				print('No, There is no fGit project in {}.'.format(os.path.abspath(sys.argv[2])))
		else:
			print("There is no directory named '{}'.".format(os.path.abspath(sys.argv[2])))