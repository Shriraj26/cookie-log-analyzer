import unittest
import os
import io
import sys
from contextlib import redirect_stdout
from process import main
from csv_utility import _make_csv

class TestIntegration(unittest.TestCase):

    def test_integration_single_cookie(self):
        rows = [
            ["A", "2018-12-09T10:00:00+00:00"],
            ["B", "2018-12-08T11:00:00+00:00"],
            ["A", "2018-12-09T12:00:00+00:00"],
        ]
        file_path = _make_csv(rows)

        try:
            sys.argv = ["process.py", "-f", file_path, "-d", "2018-12-09"]

            buf = io.StringIO()
            with redirect_stdout(buf):
                main()

            output = buf.getvalue().strip().split("\n")
            self.assertEqual(output, ["A"])
        finally:
            os.remove(file_path)

    def test_integration_multiple_cookies(self):
        rows = [
            ["A", "2018-12-09T10:00:00+00:00"],
            ["B", "2018-12-09T11:00:00+00:00"],
            ["A", "2018-12-09T12:00:00+00:00"],
            ["B", "2018-12-09T13:00:00+00:00"],
        ]
        file_path = _make_csv(rows)

        try:
            sys.argv = ["process.py", "-f", file_path, "-d", "2018-12-09"]

            buf = io.StringIO()
            with redirect_stdout(buf):
                main()

            output = buf.getvalue().strip().split("\n")
            self.assertCountEqual(output, ["A", "B"])  # order doesn't matter
        finally:
            os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
