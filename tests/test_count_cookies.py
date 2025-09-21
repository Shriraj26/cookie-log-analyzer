import unittest
import os
from process import most_active_cookies, count_cookies
from csv_utility import _make_csv

class TestCountCookies(unittest.TestCase):
    
    def test_single_cookie_match(self):
        rows = [
            ["A", "2018-12-09T10:00:00+00:00"],
            ["B", "2018-12-08T10:00:00+00:00"],  # should be ignored
        ]
        file_path = _make_csv(rows)
        try:
            result = count_cookies(file_path, "2018-12-09")
            self.assertEqual(result, {"A": 1})
        finally:
            os.remove(file_path)

    def test_multiple_cookies_same_date(self):
        rows = [
            ["A", "2018-12-09T10:00:00+00:00"],
            ["B", "2018-12-09T11:00:00+00:00"],
            ["A", "2018-12-09T12:00:00+00:00"],
        ]
        file_path = _make_csv(rows)
        try:
            result = count_cookies(file_path, "2018-12-09")
            self.assertEqual(result, {"A": 2, "B": 1})
        finally:
            os.remove(file_path)

    def test_no_cookies_for_date(self):
        rows = [
            ["A", "2018-12-08T10:00:00+00:00"],
            ["B", "2018-12-07T11:00:00+00:00"],
        ]
        file_path = _make_csv(rows)
        try:
            result = count_cookies(file_path, "2018-12-09")
            self.assertEqual(result, {})
        finally:
            os.remove(file_path)

    def test_break_on_later_date(self):
        rows = [
            ["A", "2018-12-10T09:00:00+00:00"],
            ["B", "2018-12-09T10:00:00+00:00"],
            ["C", "2018-12-08T10:00:00+00:00"], # Should not reach here  
        ]
        file_path = _make_csv(rows)
        try:
            result = count_cookies(file_path, "2018-12-09")
            self.assertEqual(result, {"B": 1})
        finally:
            os.remove(file_path)

    def test_empty_map(self):
        self.assertEqual(most_active_cookies({}), [])