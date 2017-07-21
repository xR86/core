# Simple tests using pytest
# run with -> pytest -v

# import pytest
import os
from os.path import join, getsize

root_files = []

#
### Setup function ###
#

def setup_function():
	global root_files
	level = 0
	
	num_sep = "./".count(os.path.sep)
	for root, dirs, files in os.walk("./"):
		#print(sum(getsize(join(root, name)) for name in files), end=" ")
		#print("bytes in", len(files), "non-directory files")
		#
		root_files = files
		num_sep_this = root.count(os.path.sep)
		if num_sep + level <= num_sep_this:
			del dirs[:]
	root_files = set(root_files) # make "contain" check in O(1)

def test_setup_ran():
	setup_function()
	print("root_files: %s" % root_files)
	print(len(root_files))

	if root_files:
		assert True
	else:
		assert False


#
### TESTS functions ###
#

# TODO: should also check if it has open-source license
def test_has_license():
	if "LICENSE" in root_files:
		assert True
	else:
		assert False

# TODO: should check if it has well-formed .gitignore
# specifically, if it separates standard rules for language from custom rules
def test_has_gitignore():
	if ".gitignore" in root_files:
		assert True
	else:
		assert False

# TODO: should check if it has title, description, image | video | gif | link, link to documentation
# ... 
def test_has_readme():
	if "README.md" in root_files:
		assert True
	else:
		assert False
