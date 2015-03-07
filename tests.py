import exercise
import unittest

class TestIsLeapYear(unittest.TestCase):
	def test_2000_is_a_leap_year(self):
		self.assertTrue(exercise.is_leap_year(2000), '2000 is a leap year')

	def test_1800_is_not_a_leap_year(self):
		self.assertIsNotNone(exercise.is_leap_year(1800), 'is_leap_year does not return None')
		self.assertFalse(exercise.is_leap_year(1800), '1800 is not a leap year')

	def test_2012_is_a_leap_year(self):
		self.assertIsNotNone(exercise.is_leap_year(2012), 'is_leap_year does not return None')
		self.assertFalse(exercise.is_leap_year(2012), '2012 is not a leap year')

class TestIsPalindrome(unittest.TestCase):
	def test_madam_is_a_palindrome(self):
		self.assertTrue(exercise.is_palindrome('madam'), 'madam which has an odd number of letters is a palindrome')

	def test_anna_is_a_palindrome(self):
		self.assertTrue(exercise.is_palindrome('anna'), 'anna which has an even number of letters is a palindrome')

	def test_hello_is_not_a_palindrome(self):
		self.assertIsNotNone(exercise.is_palindrome('hello'), 'is_leap_year does not return None')
		self.assertFalse(exercise.is_palindrome('hello'), 'hello is not a palindrome')

class TestDescriptiveStats(unittest.TestCase):
	def test_mode_returns_the_largest_value_at_the_end_of_a_list(self):
		self.assertEqual(exercise.mode([10, 203, 434]), 434, 'the mode of [10, 203, 434] is 434')

	def test_mode_returns_the_largest_value_at_the_start_of_a_list(self):
		self.assertEqual(exercise.mode([434, 203, 10]), 434, 'the mode of [434, 203, 10] is 434')

	def test_mode_returns_the_largest_value_at_the_middle_of_the_list(self):
		self.assertEqual(exercise.mode([434, 203, 505, 23, 100, 10]), 505, 'the mode of [434, 203, 505, 23, 100, 10] is 434')

	def test_median_for_list_with_an_even_length(self):
		self.assertEqual(exercise.median([434, 200, 505, 23, 100, 10]), 150, 'the median of [434, 200, 505, 23, 100, 10] is 150')

	def test_median_for_list_with_an_odd_length(self):
		self.assertEqual(exercise.median([434, 200, 505, 100, 10]), 200, 'the median of [434, 200, 505, 100, 10] is 200')		

if __name__ == '__main__':
	test_loader = unittest.TestLoader()
	suites = unittest.TestSuite(map(
		lambda test_case: test_loader.loadTestsFromTestCase(test_case),
		[TestIsLeapYear, TestIsPalindrome, TestDescriptiveStats])
	)
	unittest.TextTestRunner().run(suites)