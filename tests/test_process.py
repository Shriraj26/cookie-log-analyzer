import unittest

if __name__ == "__main__":
    # Discover and run all tests inside "tests" folder
    unittest.TestLoader().discover("tests")
    unittest.main(module=None)
