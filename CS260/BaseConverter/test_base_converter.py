import unittest
from base_converter import BaseConverter

class TestBaseConverter(unittest.TestCase):
    """Unit testing class BaseConverter."""

    def test_link(self):
        bc = BaseConverter()
        self.assertEqual(bc.convert(10, 10, 16), "A")
        self.assertEqual(bc.convert(256, 10, 16), "100")
        self.assertEqual(bc.convert(256, 10, 8), "400")
        self.assertEqual(bc.convert(255, 10, 2), "11111111")


if __name__ == "__main__":
    unittest.main()