# python3 test_github_community.py
# python3 -m unittest test_github_community.py 

import unittest
import os

checklist = []

class CommunityTestCase(unittest.TestCase):
	"""Tests for Github Community Guidelines"""
	files = None
	flag_community = False

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
	def test_README(self):
		"""Is there a README file ?"""
		self.assertTrue('README' in self.files or \
						'README.md' in self.files)

	def test_LICENSE(self):
		"""Is there a LICENSE file ?"""
		self.assertTrue('LICENSE' in self.files or \
						'LICENSE.md' in self.files)


	@unittest.skipIf(not flag_community,
					'repo not open to contributions')
	def test_CODE_OF_CONDUCT(self):
		"""Is there a CODE_OF_CONDUCT file ?"""
		self.assertTrue('CODE_OF_CONDUCT' in self.files or \
						'CODE_OF_CONDUCT.md' in self.files)

	@unittest.skipIf(not flag_community,
					'repo not open to contributions')
	def test_CONTRIBUTING(self):
		"""Is there a CONTRIBUTING file ?"""
		self.assertTrue('CONTRIBUTING' in self.files or \
						'CONTRIBUTING.md' in self.files)

	@unittest.skipIf(not flag_community,
					'repo not open to contributions')
	def test_ISSUE_TEMPLATE(self):
		"""Is there a ISSUE_TEMPLATE file ?"""
		self.assertTrue('ISSUE_TEMPLATE' in self.files or \
						'ISSUE_TEMPLATE.md' in self.files)

	@unittest.skipIf(not flag_community,
					'repo not open to contributions')
	def test_PULL_REQUEST_TEMPLATE(self):
		"""Is there a PULL_REQUEST_TEMPLATE file ?"""
		self.assertTrue('PULL_REQUEST_TEMPLATE' in self.files or \
						'PULL_REQUEST_TEMPLATE.md' in self.files)


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