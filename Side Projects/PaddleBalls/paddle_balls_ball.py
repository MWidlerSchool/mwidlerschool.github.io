import tkinter
       
class PBBall():
    """A colored ball that bounces around the screen, off other balls, and off the paddle."""
    
    def __init__(self, canv, size = 25, color = "cyan"):
        """Initialize the instance variables. Default color is cyan because I like cyan."""
        self.size = size
        self.color = color
        self.xLoc = 0.0
        self.yLoc = 0.0
        self.xSpeed = 0.0
        self.ySpeed = 0.0
        self.canv = canv
        self.id = self.canv.create_oval(0, 0, self.size, self.size, fill = self.color)
        
    def radius(self):
        """Returns the radius of the ball, in pixels."""
        return self.size / 2
    
    def getCenterPoint(self):
        """Returns the center point of the ball."""
        return (self.xLoc + self.radius(), self.yLoc + self.radius())
    
    def getCollisionPoints(self):
        """Returns a tuple of tuples for N, E, S, W."""
        offset = self.size / 2
        xOrigin = self.xLoc + offset
        yOrigin = self.yLoc + offset
        return ((xOrigin, yOrigin - offset),
                (xOrigin + offset, yOrigin),
                (xOrigin, yOrigin + offset),
                (xOrigin - offset, yOrigin))
        
        
    def setLoc(self, x, y):
        """Set the location (based on bounding box NW corner) on the canvas."""
        self.xLoc = float(x)
        self.yLoc = float(y)
        self.canv.coords(self.id, int(self.xLoc), int(self.yLoc), int(self.xLoc) + self.size, int(self.yLoc) + self.size)
    
    def bounce(self, newDir):
        """Change to a specific direction."""
        if newDir == "north":
            self.ySpeed = abs(self.ySpeed) * -1
        elif newDir == "south":
            self.ySpeed = abs(self.ySpeed)
        elif newDir == "west":
            self.xSpeed = abs(self.xSpeed) * -1
        elif newDir == "east":
            self.xSpeed = abs(self.xSpeed) 
        elif newDir == "reverse":
            self.xSpeed = -self.xSpeed
            self.ySpeed = -self.ySpeed
        elif newDir == "northeast":
            self.bounce("north")
            self.bounce("east")
        elif newDir == "northwest":
            self.bounce("north")
            self.bounce("west")
        elif newDir == "southeast":
            self.bounce("south")
            self.bounce("east")
        elif newDir == "southwest":
            self.bounce("south")
            self.bounce("west")
    
    def collideWithBall(self, other):
        """Bounce off another ball. Also bounces the other ball, so don't call it twice."""
        deltaSelfX = self.xSpeed - other.xSpeed
        deltaSelfY = self.ySpeed - other.ySpeed
        deltaOtherX = other.xSpeed - self.xSpeed
        deltaOtherY = other.ySpeed - self.ySpeed
        
        self.xSpeed = self.xSpeed - deltaSelfX
        self.ySpeed = self.ySpeed - deltaSelfY
        other.xSpeed = other.xSpeed - deltaOtherX
        other.ySpeed = other.ySpeed - deltaOtherY
    
    def tickElapsed(self):
        """Update location when kicked by timer."""
        newX = self.xLoc + self.xSpeed
        newY = self.yLoc + self.ySpeed
        self.setLoc(newX, newY)