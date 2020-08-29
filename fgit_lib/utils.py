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
		project_file = open(os.path.join(directory, name, '.fgit', 'project'), 'w')
		project_file.write("""name={0}
creator={1}
version={2}
working_version={2}""".format(name, user, '0'))
		project_file.close()
	else:
		os.makedirs(os.path.join(directory, '.fgit'))
		project_file = open(os.path.join(directory, '.fgit', 'project'), 'w')
		project_file.write("""name={0}
creator={1}
version={2}
working_version={2}""".format(name, user, '0'))
		project_file.close()