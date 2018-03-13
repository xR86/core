# python3 tests/test_git.py
# python3 -m unittest tests/test_git.py 

import unittest
import os

checklist = []

class GitTestCase(unittest.TestCase):
	"""Tests for Git Guidelines"""
	files = None

	currentResult = None # holds last result object passed to run method

	def setUp(self):
		root, dirs, files = os.walk('./').__next__()
		self.files = list(filter(None, files))

	def tearDown(self):
		global checklist
		ok = self.currentResult.wasSuccessful()
		errors = self.currentResult.errors
		failures = self.currentResult.failures
		# print('All tests passed so far!' if ok else \
		# 		' %d errors and %d failures so far' % \
		# 		(len(errors), len(failures)))
		checklist = failures

	def run(self, result=None):
		self.currentResult = result # remember result for use in tearDown
		unittest.TestCase.run(self, result) # call superclass run method


	# TESTS
	def test_gitignore(self):
		"""Is there a .gitignore file ?"""
		self.assertTrue('.gitignore' in self.files)



if __name__ == '__main__':
	unittest.main(exit=False)

	print('\n\n\n' + '***' * 50 + '\n')
	print('Checklist:')
	for i in range(len(checklist)):
		test_name = str(checklist[i][0])
		end_ind = str(test_name).index('(')
		# print(test_name)
		print('[ ] ' + test_name[5:end_ind-1]) # function title
		# print(checklist[i][1]) # Traceback
	if len(checklist) == 0:
		print('Nothing to show ...')