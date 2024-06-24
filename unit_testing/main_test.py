# python3 test.py
# python3 -m unittest [-v]

import unittest

import main


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_add_five_int(self):
        """Test an int"""
        result = main.add_five(1)
        self.assertEqual(result, 6)

    def test_add_five_string_int(self):
        """Test a string that can be casted to an int"""
        result = main.add_five("2")
        self.assertEqual(result, 7)

    def test_add_five_string(self):
        """Test a string that cannot be casted to an int"""
        result = main.add_five("three")
        self.assertIsInstance(result, ValueError)

    def test_add_five_none(self):
        """Test None"""
        result = main.add_five(None)
        self.assertIsInstance(result, TypeError)
        self.assertEqual(str(result), "Please enter a number")


if __name__ == "__main__":
    unittest.main()
