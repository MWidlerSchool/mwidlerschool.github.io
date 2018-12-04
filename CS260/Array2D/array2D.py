class Array2D():
    """An implementation for two-dimensional arrays, despite internally being one-dimensional."""
    
    def __init__(self, w, h, defVal = None):
        """Initialize the array. Size cannot be changed after initialization."""
        self.__width = w
        self.__height = h
        size = w * h
        self.__array = [defVal] * size
    
    def __getIndex(self, x, y):
        """Internal method to convert cartesian coordinates to array indices."""
        return (x * self.height) + y
    
    def isInBounds(self, x, y):
        """Returns a boolean indicating if the passed location is in bounds."""
        if (x >= 0 and x < self.__width and
            y >= 0 and y < self.__height):
            return True
        return False
    
    @property
    def width(self):
        """Return the width without allowing the user to change it."""
        return self.__width
    
    @property
    def height(self):
        """Return the height without allowing the user to change it."""
        return self.__height
    
    def get(self, x, y):
        """Get the contents of a cell."""
        if (self.isInBounds(x, y)):
            return self.__array[self.__getIndex(x, y)]
        else:
            raise IndexError("Array index out of range: [{}, {}] is outside of [{}, {}].".format(
                x, y, self.__width, self.__height))
    
    def set(self, x, y, data):
        """Set the contents of a cell."""
        if (self.isInBounds(x, y)):
            self.__array[self.__getIndex(x, y)] = data
        else:
            raise IndexError("Array index out of range: [{}, {}] is outside of [{}, {}].".format(
                x, y, self.__width, self.__height))

if __name__ == "__main__":
    arr = Array2D(3, 4)
    arr.set(2, 3, "Word")