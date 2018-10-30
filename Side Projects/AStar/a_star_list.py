from a_star_list_link import LLLink as Link

class AStarList():
    """Linked list object. A modified version of a general purpose class to keep A* nodes sorted by f."""
    
    def __init__(self, data = None):
        """Initializer."""
        self.size = 0
        if data != None:
            self.addToEmpty(data)
    
    def __len__(self):
        return self.size
    
    def addToEmpty(self, data):
        """Add a node to an empty list."""
        self.head = Link(data)
        self.head.next = self.head
        self.head.previous = self.head
        self.size = 1
    
    def contains(self, newLoc):
        """Check if the list contains a node with a specific loc."""
        if len(self) == 0:
            return False
        curLink = self.head
        if curLink.data.loc == newLoc:
            return True
        curLink = curLink.next
        while curLink != self.head:
            if curLink.data.loc == newLoc:
                return True
            curLink = curLink.next
        return False
    
    def update(self, newLoc, possibleParent, stepDist):
        """Update the node with the passed location with the passed parent, if that parent is shorter."""
        curLink = self.head
        if curLink.data.loc == newLoc:
            curLink.data.update(possibleParent, stepDist)
        curLink = curLink.next
        while curLink != self.head:
            if curLink.data.loc == newLoc:
                curLink.data.update(possibleParent, stepDist)
                return
            curLink = curLink.next
    
    def push(self, node):
        """Push a new node into the list, maintaining a sort by f."""
        if len(self) == 0:
            self.addToEmpty(node)
        else:
            terminus = self.head.previous
            isInserted = False
            curLink = self.head
            while isInserted == False and curLink != terminus:
                if node.f < curLink.data.f:
                    curLink.insertBefore(Link(node))
                    isInserted = True
                    if curLink == self.head:
                        self.head = curLink.previous
                curLink = curLink.next
            if isInserted == False:
                self.head.insertBefore(Link(node))
            self.size += 1
    
    def pushToFront(self, node):
        """Adds a new node to the front of the list."""
        self.head.insertBefore(Link(node))
        self.head = self.head.previous
        self.size += 1
    
    def pop(self):
        """Pop the top (ie, lowest f) node off the list."""
        if self.size == 0:
            return None
        topNode = self.head.data
        newHead = self.head.next
        self.head.remove()
        self.head = newHead
        self.size -= 1
        if self.size == 0:
            self.head = None
        return topNode
    
    
    def getList(self):
        """Returns the list as a standard Python List, in reverse order."""
        curLink = self.head
        returnVal = []
        returnVal.append(curLink.data)
        curLink = curLink.next
        while curLink != self.head:
            returnVal.append(curLink.data)
            curLink = curLink.next
        return returnVal