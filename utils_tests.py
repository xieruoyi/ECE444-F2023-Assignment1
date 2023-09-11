import unittest
from utils import utils

class TestUtils(unittest.TestCase):
    def test_reversed(self):
        self.assertEqual(utils.reversed(12345), 54321)
        self.assertEqual(utils.reversed(0), 0)
        with self.assertRaises(ValueError):
            utils.reversed("123")
            utils.reversed(12.34)

    def test_formatter(self):
        self.assertEqual(utils.formatter(42), ('0b101010', '0o52'))
        self.assertEqual(utils.formatter(0), ('0b0', '0o0'))
        with self.assertRaises(ValueError):
            utils.formatter("123")
            utils.formatter(12.34)

if __name__ == '__main__':
    unittest.main()
