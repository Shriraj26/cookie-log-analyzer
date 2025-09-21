import unittest
from process import most_active_cookies

class TestMostActiveCookies(unittest.TestCase):

    def test_single_cookie(self):
        result = most_active_cookies({"A": 3})
        self.assertEqual(result, ["A"])

    def test_multiple_cookies_no_tie(self):
        result = most_active_cookies({"A": 1, "B": 5, "C": 3})
        self.assertEqual(result, ["B"])

    def test_multiple_cookies_with_tie(self):
        result = most_active_cookies({"A": 4, "B": 4, "C": 2})
        # Order doesn't matter
        self.assertCountEqual(result, ["A", "B"])

    def test_all_cookies_tied(self):
        result = most_active_cookies({"A": 2, "B": 2, "C": 2})
        self.assertCountEqual(result, ["A", "B", "C"])