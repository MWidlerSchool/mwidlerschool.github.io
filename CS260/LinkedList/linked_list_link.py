class LLLink():

    def __init__(self, d, p = None, n = None):
        """Initializer. If either side is not given a value, points to self in that direction."""
        self.previous = p
        self.next = n
        self.data = d
        if self.previous == None:
            self.previous = self
        if self.next == None:
            self.next = self
    
    def insertAfter(self, newLink):
        """Inserts the passed node immedeatly after this one, adjusting connections as necessary."""
        newLink.previous = self
        newLink.next = self.next
        self.next.previous = newLink
        self.next = newLink
    
    def insertBefore(self, newLink):
        """Inserts the passed node immedeatly before this one, adjusting connections as necessary."""
        newLink.previous = self.previous
        newLink.next = self
        self.previous.next = newLink
        self.previous = newLink
        
    def remove(self):
        """Attaches the next and previous links to each other."""
        self.next.previous = self.previous
        self.previous.next = self.next