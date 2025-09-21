import unittest
from process import compare_dates

class TestCookieLogs(unittest.TestCase):

    def test_equal_dates(self):
        result = compare_dates("2018-12-09", "2018-12-09T10:00:00+00:00")
        self.assertEqual(result, 0)

    def test_input_date_after_timestamp(self):
        result = compare_dates("2018-12-10", "2018-12-09T23:59:59+00:00")
        self.assertEqual(result, 1)

    def test_input_date_before_timestamp(self):
        result = compare_dates("2018-12-08", "2018-12-09T00:00:00+00:00")
        self.assertEqual(result, -1)

    def test_invalid_timestamp(self):
        with self.assertRaises(ValueError):
            compare_dates("2018-12-09", "invalid-timestamp")