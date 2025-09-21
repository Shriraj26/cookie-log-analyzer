import unittest
import tempfile
import os
from process import validate_file, validate_date

class TestValidate(unittest.TestCase):

    def test_file_exists(self):
        
        # Create a temporary file that will have a path
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_path = tmp.name

        try:
            result = validate_file(tmp_path)
            self.assertEqual(result, tmp_path)
        finally:
            # Clean up temp file
            os.remove(tmp_path)

    def test_file_does_not_exist(self):
        fake_path = "file_that_does_not_exist.csv"
        with self.assertRaises(FileNotFoundError):
            validate_file(fake_path)

    def test_validate_date(self):
        self.assertEqual(validate_date("2018-12-09"), "2018-12-09")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            validate_date("20181209")  # missing dashes

    def test_invalid_non_digit(self):
        with self.assertRaises(ValueError):
            validate_date("2018-1a-09")

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            validate_date("2018-13-10")

    def test_invalid_day_range(self):
        with self.assertRaises(ValueError):
            validate_date("2018-12-32")

    def test_invalid_calendar_date(self):
        with self.assertRaises(ValueError):
            validate_date("2018-02-30")