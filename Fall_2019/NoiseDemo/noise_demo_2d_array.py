class array2D():
   """
   A class which emulates a 2-dimensional array.
   """
   
   def __init__(self, w, h):
      """
      Initializer. Sets the width and height of the 2D array.
      """
      self.width = w
      self.height = h
      self.val = [0.0] * (self.width * self.height)
   
   def get(self, x, y):
      """
      Returns the value stored at x, y.
      """
      if self.__isInRange(x, y):
         return self.val[self.__getTrueIndex(x, y)]
      return None
   
   def set(self, data, x, y):
      """
      Returns the value stored at x, y.
      """
      if self.__isInRange(x, y):
         self.val[self.__getTrueIndex(x, y)] = data
   
   def __getTrueIndex(self, x, y):
      """
      Internal function. Returns the index in the actual array of the passed virtual index.
      """
      return x + (y * self.width)
   
   def __isInRange(self, x, y):
      """
      Internal function. Checks that a virtual index is valid.
      """
      return x >= 0 and y >= 0 and x < self.width and y < self.height