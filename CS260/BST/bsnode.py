class BSNode():
    """A node for a binary search tree."""
    
    def __init__(self, data):
        """Initialize the node."""
        self.data = data
        self.left = None
        self.right = None
    
    def add(self, newData):
        """New data fliters down to where it belongs"""
        if newData < self.data:
            if self.left == None:
                self.left = BSNode(newData)
            else:
                self.left.add(newData)
        elif newData > self.data:
            if self.right == None:
                self.right = BSNode(newData)
            else:
                self.right.add(newData)
                
    def hasLeft(self):
        """Because I'm a Java guy at heart"""
        return self.left != None
                
    def hasRight(self):
        """Because I'm a Java guy at heart"""
        return self.right != None