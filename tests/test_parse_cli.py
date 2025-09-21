import unittest
import sys
from process import parse_cli
from argparse import Namespace

class TestParseCli(unittest.TestCase):
    
    def test_parse_cli_valid_args(self):
        test_args = ["process.py", "-f", "cookies.csv", "-d", "2018-12-09"]
        sys.argv = test_args  # temporarily override
        args = parse_cli()
        self.assertIsInstance(args, Namespace)
        self.assertEqual(args.file, "cookies.csv")
        self.assertEqual(args.date, "2018-12-09")

    def test_parse_cli_missing_file(self):
        test_args = ["process.py", "-d", "2018-12-09"]
        sys.argv = test_args
        with self.assertRaises(SystemExit):  # argparse exits if required arg missing
            parse_cli()

    def test_parse_cli_missing_date(self):
        test_args = ["process.py", "-f", "cookies.csv"]
        sys.argv = test_args
        with self.assertRaises(SystemExit):
            parse_cli()

