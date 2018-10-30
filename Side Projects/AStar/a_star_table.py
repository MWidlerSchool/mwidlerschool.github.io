
class AStarTable():
    """A hash table for an A* object's closed list. Takes [x, y] locations as input."""
    
    def __init__(self, width, height):
        """Initialize the table. All entries initially False."""
        self.width = width
        self.height = height
        self.table = [False] * (width * height)
    
    def add(self, nodeLoc):
        """Mark an entry as True."""
        self.table[self.getHashIndex(nodeLoc)] = True
    
    def contains(self, nodeLoc):
        """Return the value stored at a particular location."""
        return self.table[self.getHashIndex(nodeLoc)]
    
    def getHashIndex(self, nodeLoc):
        """Get the hash index of an intiger pair."""
        return (nodeLoc[0] * self.height) + nodeLoc[1]