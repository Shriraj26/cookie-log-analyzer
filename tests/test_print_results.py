import unittest
from process import print_results
from contextlib import redirect_stdout
import io

class TestPrintResults(unittest.TestCase):

    def test_print_single_cookie(self):
            buf = io.StringIO()
            with redirect_stdout(buf):
                print_results(["A"])
            output = buf.getvalue().strip()
            self.assertEqual(output, "A")

    def test_print_multiple_cookies(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            print_results(["A", "B", "C"])
        output = buf.getvalue().strip().split("\n")
        self.assertEqual(output, ["A", "B", "C"])

    def test_print_empty_list(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            print_results([])
        output = buf.getvalue().strip()
        self.assertEqual(output, "")  # no output