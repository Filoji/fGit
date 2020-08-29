import sys
import os

#chech if there is a '.fgit' directory
def check_dir(directory):
	return os.path.isdir(os.path.join(directory, '.fgit'))

#create a project
def create_project(directory, name, user, here):
	if not here:
		os.makedirs(os.path.join(directory, name))
		os.makedirs(os.path.join(directory, name, '.fgit'))
		os.makedirs(os.path.join(directory, name, '.fgit', 'master'))
		project_file = open(os.path.join(directory, name, '.fgit', 'project'), 'w')
		project_file.write("""name={0}
creator={1}
version=0
working_version=0
working_branch=master
allbranches:
master""".format(name, user))
		project_file.close()
	else:
		os.makedirs(os.path.join(directory, '.fgit'))
		os.makedirs(os.path.join(directory, '.fgit', 'master'))
		project_file = open(os.path.join(directory, '.fgit', 'project'), 'w')
		project_file.write("""name={0}
creator={1}
version=0
working_version=0
working_branch=master
allbranches:
master""".format(name, user))
		project_file.close()

class Colors(object):
	yellow='\033[1;33m'
	green='\033[1;32m'
	underlined='\033[4m'
	bold='\033[1m'
	italic='\033[3m'
	stop='\033[0m'
	error='\033[1;31mError: \033[0m'