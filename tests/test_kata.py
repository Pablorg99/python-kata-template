import unittest
from src.kata import Kata


class TestClass(unittest.TestCase):
    def test_method(self):
        return_value = Kata().rule()

        self.assertEqual("green", return_value)


if __name__ == '__main__':
    unittest.main()
