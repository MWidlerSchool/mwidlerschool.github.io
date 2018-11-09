import random

class BTree:
    """A binary tree implementation, using a Python list. Intended to work with numbers as data members."""
    
    def __init__(self):
        self.__nodeList = [None]
        self.__height = 1
    
    def sizeCheck(self, newIndex):
        """Make sure that the list is long enough to hold the new item"""
        if len(self) <= newIndex:
            self.__nodeList += [None] * (len(self.__nodeList) + 1)
            self.__height += 1
            self.sizeCheck(newIndex)
            
    def clear(self):
        """Clears the list and resets its values."""
        self.__nodeList = [None]
        self.__height = 1
    
    @property
    def height(self):
        """The height of the tree, in levels."""
        return self.__height
    
    def getLeft(curIndex):
        """Returns the index of the left child of the passed index."""
        return (curIndex * 2) + 1
    
    def getRight(curIndex):
        """Returns the index of the right child of the passed index."""
        return (curIndex + 1) * 2
    
    def getParent(curIndex):
        """Returns the index of the parent of the passed index."""
        return (curIndex - 1) // 2
    
    def add(self, newData, dataLoc = 0):
        """Add a new item to the tree. """
        self.sizeCheck(dataLoc)
        if self.__nodeList[dataLoc] == None:
            self.__nodeList[dataLoc] = newData
        elif self.__nodeList[dataLoc] > newData: # go left
            self.add(newData, BTree.getLeft(dataLoc))
        elif self.__nodeList[dataLoc] < newData: # go right
            self.add(newData, BTree.getRight(dataLoc))
        # data which matches the entry is discarded
    
    def inorder(self, index = 0, returnList = None):
        """Returns a list (no gaps) generated by LVR. This will be all items in ascending order."""
        if returnList == None:
            returnList = []
        if index < len(self) and self.__nodeList[index] is not None:
            self.inorder(BTree.getLeft(index), returnList)
            returnList.append(self.__nodeList[index])
            self.inorder(BTree.getRight(index), returnList)
        return returnList   # only actually used by the first call
    
    def preorder(self, index = 0, returnList = None):
        """Returns a list (no gaps) generated by VLR."""
        if returnList == None:
            returnList = []
        if index < len(self) and self.__nodeList[index] is not None:
            returnList.append(self.__nodeList[index])
            self.preorder(BTree.getLeft(index), returnList)
            self.preorder(BTree.getRight(index), returnList)
        return returnList   # only actually used by the first call
    
    def postorder(self, index = 0, returnList = None):
        """Returns a list (no gaps) generated by LRV."""
        if returnList == None:
            returnList = []
        if index < len(self) and self.__nodeList[index] is not None:
            self.postorder(BTree.getLeft(index), returnList)
            self.postorder(BTree.getRight(index), returnList)
            returnList.append(self.__nodeList[index])
        return returnList   # only actually used by the first call
    
    def reverseorder(self, index = 0, returnList = None):
        """Returns a list (no gaps) generated by RLV. This will be all items in descending order."""
        if returnList == None:
            returnList = []
        if index < len(self) and self.__nodeList[index] is not None:
            self.reverseorder(BTree.getRight(index), returnList)
            returnList.append(self.__nodeList[index])
            self.reverseorder(BTree.getLeft(index), returnList)
        return returnList   # only actually used by the first call
        
    def getLevel(self, level):
        """Returns one level of the tree as a list."""
        start = (2 ** level) - 1
        end = (2 ** (level + 1)) - 1
        lvlList = []
        for i in range(start, end):
            lvlList.append(self.__nodeList[i])
        return lvlList
    
    def balance(self, oldList = None, newList = None):
        """Balances the list by recursively adding the middle item of a sorted list and splitting it."""
        # initialize on first call
        topCall = False
        if oldList == None or newList == None:
            oldList = self.inorder()
            newList = []
            topCall = True
        # base case
        if len(oldList) <= 2:
            newList.append(oldList[0])
            if len(oldList) == 2:
                newList.append(oldList[1])
        else:
            midpoint = len(oldList) // 2
            newList.append(oldList[midpoint])
            self.balance(oldList[:midpoint], newList)
            self.balance(oldList[midpoint + 1:], newList)
        if topCall:
            totalSize = len(self)
            self.clear()
            for val in newList:
                self.add(val)
            
    
    def __str__(self):
        """Standard toString method. Returns the complete array."""
        return str(self.__nodeList)
    
    def __len__(self):
        """Note that this returns the total size of the list, INCLUDING None elements."""
        return len(self.__nodeList)
    
    def print(self):
        """Prints the tree as a list of each level."""
        for i in range(0, self.height):
            print("Level {}:".format(i), end = "")
            print(tree.getLevel(i))

if __name__ == "__main__":
    tree = BTree()
    for i in range(1, 100):
        tree.add(random.randint(0, 1000))
    tree.print()
    print("Items in unbalanced tree: {}".format(len(tree.inorder())))
    print("Levels in unbalanced tree: {}".format(tree.height))
    tree.balance()
    tree.print()
    print("Items in balanced tree: {}".format(len(tree.inorder())))
    print("Levels in unbalanced tree: {}".format(tree.height))