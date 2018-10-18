from linked_list_link import LLLink as Link

class BetterQueue():
    """A stack class implemented as a linked list. Push, pop, peek, and len are all O(1). str is O(n)."""
    
    def __init__(self, initialData = None):
        """Initializer."""
        self.head = None
        self.size = 0
        if initialData != None:
            self.push(initialData)
    
    def __len__(self):
        """Returns the length of the queue."""
        return self.size
    
    def __str__(self):
        """Returns a string representing the queue, in the same style as a list does."""
        returnVal = []
        node = self.head
        for i in range(self.size):
            returnVal.append(node.data)
            node = node.next
        return str(returnVal)
    
    def push(self, newData):
        """Add data to the end of the stack."""
        if self.head == None:
            self.head = Link(newData)
        else:
            self.head.previous.insertAfter(Link(newData))
        self.size += 1
    
    def pop(self):
        """Return data from the beginning of the stack."""
        data = None
        if self.size > 0:
            data = self.head.data
            self.size -= 1
            newHead = self.head.next
            self.head.remove()
            self.head = newHead
            if self.size == 0:
                head = None
        else:
            raise IndexError("Queue is empty.")
        return data
    
    def peek(self):
        """Return data from the beginning of the stack without popping it."""
        data = None
        if self.size > 0:
            data = self.head.data
        else:
            raise IndexError("Queue is empty.")
        return data
        
    def clear(self):
        """Clears the queue."""
        self.size = 0
        self.head = None