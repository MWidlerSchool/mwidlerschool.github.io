import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):
    
    def test_basics(self):
        testFract = Fraction(1, 4)
        self.assertEqual(testFract.num, 1)
        self.assertEqual(testFract.den, 4)
        self.assertEqual(str(testFract), "1/4")
    
    def testArithmetic(self):
        half = Fraction(1, 2)
        third = Fraction(1, 3)
        quarter = Fraction(1, 4)
        self.assertEqual(half + quarter, Fraction(3, 4))
        self.assertEqual(half - quarter, quarter)
        self.assertEqual(half * half, quarter)
        self.assertEqual(half / third, Fraction(3, 2))
    
    def testLogic(self):
        half = Fraction(1, 2)
        third = Fraction(1, 3)
        quarter = Fraction(1, 4)
        self.assertTrue(half == Fraction(2, 4))
        self.assertTrue(half != third)
        self.assertTrue(half > quarter)
        self.assertTrue(half >= third)
        self.assertTrue(third < half)
        self.assertTrue(quarter <= half)
        


if __name__ == "__main__":
    unittest.main()