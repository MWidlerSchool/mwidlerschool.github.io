import random

class MHeap:
    """A min/max heap implementation, using a Python list. Intended to work with numbers as data members."""
    
    def __init__(self):
        """Initialize the heap. Defaults to being a max heap."""
        self.__nodeList = [None]
        self.__height = 1
        self.__elements = 0
        self.__compareUp = self.__maxCheckUp
        self.__compareDown = self.__maxCheckDown
        
    
    def setAsMaxHeap(self):
        """Sets the heap as a max heap. Does not resort any existing data."""
        self.__compareUp = self.__maxCheckUp
        self.__compareDown = self.__maxCheckDown
    
    def setAsMinHeap(self):
        """Sets the heap as a min heap. Does not resort any existing data."""
        self.__compareUp = self.__minCheckUp
        self.__compareDown = self.__minCheckDown
    
    def push(self, newData):
        """Add a new item to the heap, and bubbles it up to maintain the proper sort."""
        newPos = self.__elements
        self.__elements += 1
        self.sizeCheck(newPos)
        self.__nodeList[newPos] = newData
        self.bubble(newPos)
    
    def pop(self):
        """Remove the top item from the heap, swap with the last item, and sink it."""
        self.__elements -= 1
        lastIndex = self.__elements
        returnVal = self.__nodeList[0]
        self.__nodeList[0] = None
        self.swapPosition(0, lastIndex)
        self.sink(0)
        return returnVal
    
    def bubble(self, index):
        """Compares to base case, and calls the proper bubbling type."""
        if index > 0:
            self.__compareUp(index)
    
    def sink(self, index):
        """Compares to base case, and calls the proper sinking type."""
        if not self.isOnBase(index):
            self.__compareDown(index)
    
    
    def __minCheckUp(self, index):
        """Bubbles up using minimum priority. Stops if no swap is needed."""
        parent = MHeap.getParent(index)
        if self.__nodeList[index] < self.__nodeList[parent]:
            self.swapPosition(parent, index)
            self.bubble(parent)
    
    def __maxCheckUp(self, index):
        """Bubbles up using maximum priority. Stops if no swap is needed."""
        parent = MHeap.getParent(index)
        if self.__nodeList[index] > self.__nodeList[parent]:
            self.swapPosition(parent, index)
            self.bubble(parent)
    
    def __minCheckDown(self, index):
        """Sinks down using minimum priority. Stops if no swap is needed."""
        child = self.getMinChild(index)
        if (self.__nodeList[child] is not None and
            self.__nodeList[child] < self.__nodeList[index]):
            self.swapPosition(child, index)
            self.sink(child)
    
    def __maxCheckDown(self, index):
        """Sink down using maximum priority. Stops if no swap is needed."""
        child = self.getMaxChild(index)
        if (self.__nodeList[child] is not None and
            self.__nodeList[child] > self.__nodeList[index]):
            self.swapPosition(child, index)
            self.sink(child)
    
    def sizeCheck(self, newIndex):
        """Make sure that the list is long enough to hold the new item"""
        if len(self) <= newIndex:
            self.__nodeList += [None] * (len(self.__nodeList) + 1)
            self.__height += 1
            self.sizeCheck(newIndex)
    
    def swapPosition(self, indexA, indexB):
        """Swaps the position of the elements at the passed indices."""
        self.__nodeList[indexA], self.__nodeList[indexB] = self.__nodeList[indexB], self.__nodeList[indexA]
    
    
    def isOnBase(self, index):
        """Returns a boolean value indicating if the passed index is on the lowest level of the heap."""
        return index >= (2 ** (self.__height - 1)) - 1
            
    def clear(self):
        """Clears the heap and resets its values."""
        self.__nodeList = [None]
        self.__height = 1
        self.__elements = 0
        self.__compareUp = self.__maxCheckUp
        self.__compareDown = self.__maxCheckDown
    
    @property
    def height(self):
        """The height of the heap, in levels."""
        return self.__height
    
    def getParent(curIndex):
        """Returns the index of the parent of the passed index."""
        return (curIndex - 1) // 2
    
    def getLeft(curIndex):
        """Returns the index of the left child of the passed index."""
        return (curIndex * 2) + 1
    
    def getRight(curIndex):
        """Returns the index of the right child of the passed index."""
        return (curIndex + 1) * 2
    
    def getMinChild(self, curIndex):
        """Returns the index of the smallest child node, or None."""
        minChild = None
        if not (MHeap.getLeft(curIndex) > self.numOfElements()):
            left = MHeap.getLeft(curIndex)
            right = MHeap.getRight(curIndex)
            if self.__nodeList[left] is None and self.__nodeList[right] is not None:
                minChild = right
            elif self.__nodeList[right] is None and self.__nodeList[left] is not None:
                minChild = left
            else:
                minChild = left
                if self.__nodeList[left] > self.__nodeList[right]:
                    minChild = right
        return minChild
    
    def getMaxChild(self, curIndex):
        """Returns the index of the largest child node, or None."""
        maxChild = None
        if not (MHeap.getLeft(curIndex) > self.numOfElements()):
            left = MHeap.getLeft(curIndex)
            right = MHeap.getRight(curIndex)
            if self.__nodeList[left] is None and self.__nodeList[right] is not None:
                maxChild = right
            elif self.__nodeList[right] is None and self.__nodeList[left] is not None:
                maxChild = left
            else:
                maxChild = left
                if self.__nodeList[left] < self.__nodeList[right]:
                    maxChild = right
        return maxChild
        
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
        heap.push(random.randint(0, 1000))
    print("Max Heap:")
    heap.print()
    print("pop() = {}".format(heap.pop()))
    print("Max Heap:")
    heap.print()
    
    heap = MHeap()
    heap.setAsMinHeap()
    for i in range(1, 100):
        heap.push(random.randint(0, 1000))
    print("\n\nMin Heap:")
    heap.print()
    print("pop() = {}".format(heap.pop()))
    print("Min Heap:")
    heap.print()