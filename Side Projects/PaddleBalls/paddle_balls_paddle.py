import tkinter

class PBPaddle():
    def __init__(self, canv, size = 100, color = "grey"):
        """Initialize the paddle."""
        self.size = size
        self.color = color
        self.xLoc = 0.0
        self.yLoc = 0.0
        self.xSpeed = 0.0
        self.ySpeed = 0.0
        self.canv = canv
        self.moveDist = 7
        self.id = self.canv.create_rectangle(0, 0, self.size, self.size, fill = self.color)
    
    def setLoc(self, x, y):
        """Set the location (based on NW corner) on the canvas."""
        self.xLoc = float(x)
        self.yLoc = float(y)
        self.canv.coords(self.id, int(self.xLoc), int(self.yLoc), int(self.xLoc) + self.size, int(self.yLoc) + self.size)
    
    def bounce(self, newDir):
        """'Bounce' in a particular direction. Used to push the paddle back onscreen if pushed off."""
        if newDir == "north":
            self.move("Up")
        elif newDir == "south":
            self.move("Down")
        elif newDir == "west":
            self.move("Left")
        elif newDir == "east":
            self.move("Right")

    def tickElapsed(self):
        """Currently unused."""
        pass
    
    def keyInput(self, event):
        """Trigger movement from keyboard input."""
        self.move(event.keysym)
    
    def move(self, dir):
        """Move the paddle. Seperate from keyInput() so that it can be called by bounce()."""
        if dir == "Left":
            self.setLoc(self.xLoc - self.moveDist, self.yLoc)
        elif dir == "Right":
            self.setLoc(self.xLoc + self.moveDist, self.yLoc)
        elif dir == "Up":
            self.setLoc(self.xLoc, self.yLoc - self.moveDist)
        elif dir == "Down":
            self.setLoc(self.xLoc, self.yLoc + self.moveDist)