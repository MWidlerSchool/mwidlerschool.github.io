from bsnode import BSNode

class BSTree():
    """A class for a binary search tree."""
    
    def __init__(self):
        """Initialize the tree."""
        self.head = None
    
    
    def add(self, data):
        """If the tree is empty, add the first item. Otherwise roll down until the proper location is found."""
        if self.head == None:
            self.head = BSNode(data)
        else:
            self.head.add(data)
            
            
    def getAsList(self):
        """Return as an ordered list."""
        return self.inorder(self.head, [])
        
    
    def inorder(self, node, result):
        """An LVR traversal of the tree. Called internally"""
        if node.hasLeft(): #L
            self.inorder(node.left, result)
        
        result.append(node.data) #V
        
        if node.hasRight(): #R
            self.inorder(node.right, result)
            
        return result
        
