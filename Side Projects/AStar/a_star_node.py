
class AStarNode():
    """A node on an A* grid."""
    
    def __init__(self, loc, parentNode, toEnd, stepDist):
        """Initializes the node. The start node should have a parent of None."""
        self.loc = loc
        self.parent = parentNode
        self.h = toEnd
        self.g = 0
        if self.parent != None:
            self.g = self.parent.g + stepDist
        self.calcF()
        
    def update(self, prospectiveParent, stepDist):
        """Update the parent if presented with a shorter path."""
        if self.parent == None or self.g > prospectiveParent.g + stepDist:
            self.parent = prospectiveParent
            self.g = prospectiveParent.g + stepDist
            self.calcF()
    
    def calcF(self):
        """Calculate the estimated total path weight."""
        self.f = self.g + self.h