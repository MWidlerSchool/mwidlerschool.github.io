import random

class MHeap:
    """A min/max heap implementation, using a Python list. Intended to work with numbers as data members."""
    
    def __init__(self):
        """Initialize the heap. Defaults to being a max heap."""
        self.__nodeList = [None]
        self.__height = 1
        self.__elements = 0
        self.__maxHeap = True
    
    def setAsMaxHeap(self):
        """Sets the heap as a max heap. Does not resort any existing data."""
        self.__maxHeap = True
    
    def setAsMinHeap(self):
        """Sets the heap as a min heap. Does not resort any existing data."""
        self.__maxHeap = False
    
    def add(self, newData):
        """Add a new item to the heap, and bubbles it up to maintain the proper sort."""
        newPos = self.__elements
        self.__elements += 1
        self.sizeCheck(newPos)
        self.__nodeList[newPos] = newData
        self.bubble(newPos)
    
    def bubble(self, index):
        """Compares to base case, and calls the proper bubbling type."""
        if index > 0:
            if self.__maxHeap:
                self.maxCheck(index);
            else:
                self.minCheck(index);
    
    def minCheck(self, index):
        """Bubbles up using minimum priority."""
        parent = MHeap.getParent(index)
        if self.__nodeList[index] < self.__nodeList[parent]:
            self.__nodeList[index], self.__nodeList[parent] = self.__nodeList[parent], self.__nodeList[index]
            self.bubble(parent)
    
    def maxCheck(self, index):
        """Bubbles up using maximum priority."""
        parent = MHeap.getParent(index)
        if self.__nodeList[index] > self.__nodeList[parent]:
            self.__nodeList[index], self.__nodeList[parent] = self.__nodeList[parent], self.__nodeList[index]
            self.bubble(parent)
    
    def sizeCheck(self, newIndex):
        """Make sure that the list is long enough to hold the new item"""
        if len(self) <= newIndex:
            self.__nodeList += [None] * (len(self.__nodeList) + 1)
            self.__height += 1
            self.sizeCheck(newIndex)
            
    def clear(self):
        """Clears the heap and resets its values."""
        self.__nodeList = [None]
        self.__height = 1
        self.__elements = 0
    
    @property
    def height(self):
        """The height of the heap, in levels."""
        return self.__height
    
    def getParent(curIndex):
        """Returns the index of the parent of the passed index."""
        return (curIndex - 1) // 2
        
    def getLevel(self, level):
        """Returns one level of the tree as a list."""
        start = (2 ** level) - 1
        end = (2 ** (level + 1)) - 1
        lvlList = []
        for i in range(start, end):
            lvlList.append(self.__nodeList[i])
        return lvlList
    
    def __str__(self):
        """Standard toString method. Returns the complete array."""
        return str(self.__nodeList)
    
    def __len__(self):
        """Note that this returns the total size of the list, INCLUDING None elements."""
        return len(self.__nodeList)
        
    def numOfElements(self):
        """Returns the number of elements."""
        return self.__elements
    
    def print(self):
        """Prints the tree as a list of each level."""
        for i in range(0, self.height):
            print("Level {}:".format(i), end = "")
            print(self.getLevel(i))

if __name__ == "__main__":
    heap = MHeap()
    for i in range(1, 100):
        heap.add(random.randint(0, 1000))
    heap.print()
    
    heap = MHeap()
    heap.setAsMinHeap()
    for i in range(1, 100):
        heap.add(random.randint(0, 1000))
    heap.print()