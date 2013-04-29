import unittest, pywatcher, os, time, sys


class TestServer(unittest.TestCase):
	def setUp(self):
		os.system('mkdir files-test && cd files-test/ && touch file.html && touch file.css')
		self.first_modify_html = os.path.getmtime('files-test/file.html')
		self.first_modify_css = os.path.getmtime('files-test/file.css')

	def tearDown(self):
		os.system('rm -rf files-test')

	def test_should_return_a_list_containing_the_last_modification_time_of_files(self):
		get_times = pywatcher.get_time_files('files-test/')

		self.assertEqual(len(get_times), 2)
		self.assertEqual(get_times[0], self.first_modify_html)
		self.assertEqual(get_times[0], self.first_modify_css)

	def test_after_of_modifying_the_files_should_return_different_values(self):
		pass
		# f = open('files-test/file.html', 'w')
		# f.write('lorem ipsum')
		# f.close()

		# get_times = pywatcher.get_time_files('files-test/')

		# self.assertNotEqual(get_times[0], self.first_modify_html)

	def test_should_return_true_if_has_modification(self):
		current_times = [1367168649.0, 1367168649.2]
		past_times = [1467168649.0, 1367168649.2]
		has_modification = pywatcher.has_modification(current_times, past_times)

		self.assertTrue(has_modification)

	def test_should_return_false_if_not_has_modification(self):
		current_times = [1367168649.0, 1367168649.2]
		past_times = [1367168649.0, 1367168649.2]
		has_modification = pywatcher.has_modification(current_times, past_times)

		self.assertFalse(has_modification)

	def test_should_throw_error_when_not_receive_parameters(self):
		response = os.system('python pywatcher.py')
		self.assertFalse(response == 0)

	def test_should_throw_error_when_receive_invalid_parameters(self):
		response = os.system('python pywatcher.py --hh=test --rr=test')
		self.assertFalse(response == 0)

	def test_should_throw_error_when_receive_directory_invalid(self):
		response = os.system('python pywatcher.py --directory=fake-directory/ --command="echo test"')
		self.assertFalse(response == 0)

	def test_should_ok_when_receive_valid_parameters(self):
		pass
		# response = os.system('python pywatcher.py --directory=files-test/ --command="echo test"')
		# self.assertTrue(response == 0)

if __name__ == '__main__':
	unittest.main()
