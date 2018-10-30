
class AStarTable():
    """A hash table for an A* object's closed list"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.table = []
        for i in range(width * height):
            self.table.append(False)
    
    def add(self, nodeLoc):
        self.table[self.getHashIndex(nodeLoc)] = True
    
    def contains(self, nodeLoc):
        return self.table[self.getHashIndex(nodeLoc)]
    
    def getHashIndex(self, nodeLoc):
        return (nodeLoc[0] * self.height) + nodeLoc[1]