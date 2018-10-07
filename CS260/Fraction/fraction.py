class Fraction():
    """A class to keep track of fractions."""
    def __init__(self, n, d = 1):
        self.num = n
        self.den = d
        self.simplify()
    
    def __str__(self):
        """Return as a string."""
        return "{}/{}".format(self.num, self.den)
    
    def add(self, other):
        """Addition. Converts to least common multiple."""
        newN = self.num
        newD = self.den
        if isinstance(other, Fraction):
            if other.den == self.den:
                newN = self.num + other.num
            else:
                newN = (self.num * other.den) + (other.num * self.den)
                newD = self.den * other.den
        elif isinstance(other, int):
            newN = self.num + (other * self.den)
        else:
            raise TypeException("This operation requires Fractions or ints.")
        returnVal = Fraction(newN, newD)
        returnVal.simplify()
        return returnVal
    
    def subtract(self, other):
        """Performs subtraction using negative addition."""
        if not isinstance(other, Fraction):
            raise TypeException("This operation requires two fractions.")
        newOther = Fraction(-other.num, other.den)
        return self.add(newOther)
    
    def multiply(self, other):
        """Multiplication."""
        if not isinstance(other, Fraction):
            raise TypeException("This operation requires two fractions.")
        returnVal = Fraction(self.num * other.num, self.den * other.den)
        returnVal.simplify()
        return returnVal
    
    def divide(self, other):
        """Division, by multiplying the reciprocal."""
        if not isinstance(other, Fraction):
            raise TypeException("This operation requires two fractions.")
        returnVal = Fraction(self.num * other.den, self.den * other.num)
        returnVal.simplify()
        return returnVal
    
    def equals(self, other):
        """Checks equivalence."""
        returnVal = True
        if not isinstance(other, Fraction):
            returnVal = False
        self.simplify()
        other.simplify()
        return returnVal and ((self.num == other.num) and (self.den == other.den))
    
    def greaterThan(self, other):
        """Greater Than comparison by conversion to double."""
        if not isinstance(other, Fraction):
            raise TypeException("This operation requires two fractions.")
        return (self.num / self.den) > (other.num / other.den)
    
    def lessThan(self, other):
        """Greater Than comparison by conversion to double."""
        if not isinstance(other, Fraction):
            raise TypeException("This operation requires two fractions.")
        return (self.num / self.den) < (other.num / other.den)
    
    def __add__(self, that):
        return self.add(that)
    
    def __sub__(self, that):
        return self.subtract(that)
        
    def __mul__(self, that):
        return self.multiply(that)
    
    def __truediv__(self, that):
        return self.divide(that)
    
    def __eq__(self, that):
        return self.equals(that)
    
    def __ne__(self, that):
        return not self.equals(that)
    
    def __gt__(self, that):
        return self.greaterThan(that)
    
    def __ge__(self, that):
        return self.greaterThan(that) or self.equals(that)
    
    def __lt__(self, that):
        return self.lessThan(that)
    
    def __le__(self, that):
        return self.lessThan(that) or self.equals(that)
        
        
    def simplify(self):
        """Uses findGCD() to reduce the fraction to its simplest form."""
        if self.num != 0:
            divisor = Fraction.findGCD(abs(self.num), abs(self.den))
            # floor division, or we get floats
            if divisor > 1:
                self.num = self.num // divisor
                self.den = self.den // divisor
            if (self.num < 0 and self.den < 0) or (self.num >= 0 and self.den < 0):
                self.num *= -1
                self.den *= -1
        
    
    @classmethod
    def findGCD(cls, a, b):
        """Includes wierd gyrations for instructors requirment of single exit functions."""
        big = max(a, b)
        small = min(a, b)
        remainder = 0
        while big >= small:
            big -= small
        remainder = big
        returnVal = small
        if remainder != 0:
            returnVal = Fraction.findGCD(small, remainder)
        return returnVal
