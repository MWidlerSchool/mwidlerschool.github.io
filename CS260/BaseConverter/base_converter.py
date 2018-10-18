class BaseConverter():
    """A class which converts values from one base to another."""
    _ZERO = ord('0')
    _NINE = ord('9')
    _ADJUSTED_A = ord('A') - 10
    
    def convert(self, num, oldBase, newBase):
        """This is the only method which should be called by users."""
        decNum = self.toBaseTen(num, oldBase)
        return self.toNewBase(decNum, newBase)
        
    def toBaseTen(self, num, base):
        """Converts an number of abritrary base to base 10 and returns it. Takes an int or string, returns an int."""
        numStr = str(num)
        strList = list(numStr)
        strList = self.reverseList(strList)
        newNum = 0
        i = 0
        while i < len(strList):
            newNum += (base ** i) * self.getDecValue(strList[i])
            i += 1
        return newNum
    
    def toNewBase(self, num, base):
        """Converts a base-10 number to an arbitrary base and returns it. Takes an int, returns a string."""
        valList = []
        while num > 0:
            valList.append(num % base)
            num = num // base
        valList = self.reverseList(valList)
        returnVal = ""
        for i in valList:
            returnVal += self.getCharValue(i)
        return returnVal
            
    
    def getDecValue(self, c):
        """Returns the decimal value of a character. Takes a length one string, returns an int."""
        charVal = ord(c)
        returnVal = None
        if charVal >= BaseConverter._ZERO and charVal <= BaseConverter._NINE:
            charVal -= BaseConverter._ZERO
        else:
            charVal -= BaseConverter._ADJUSTED_A
        return charVal
    
    def getCharValue(self, c):
        """Returns the character value of a number; essentially a one-digit base 62 number. Takes an int, returns a length one string."""
        returnVal = None
        if c >= 0 and c <= 9:
            returnVal = chr(c + BaseConverter._ZERO)
        else:
            returnVal = chr(c + BaseConverter._ADJUSTED_A)
        return returnVal
        
    def getDigitList(self, str):
        """Returns a list of individual one-character digits. Takes a string, returns a list of length one strings."""
        charList = list(str)
        intList = []
        for c in charList:
            intList.append(int(c))
    
    def reverseList(self, originalList):
        """Takes a list and returns a reversed copy. Does not care about list contents."""
        newList = []
        for i in reversed(originalList):
            newList.append(i)
        return newList

if __name__ == "__main__":
    bc = BaseConverter()
    
    decVal = "256"
    hexVal = str(bc.convert(256, 10, 16))
    octVal = str(bc.convert(256, 10, 8))
    binVal = str(bc.convert(256, 10, 2))
    
    print("256 in decimal:     {}".format(decVal))
    print("256 in hexidecimal: {}".format(hexVal))
    print("256 in octal:       {}".format(octVal))
    print("256 in binary:      {}".format(binVal))