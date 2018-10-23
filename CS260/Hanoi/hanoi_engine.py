import time

from hanoi_stack import HanoiStack

class HanoiEngine():
    """An engine for running the Towers of Hanoi problem recursively."""
    
    def __init__(self):
        """Initializer."""
        self.setHeight(0)
    
    def clearSpindles(self):
        """Creates three empty spindles."""
        self.spindle = [HanoiStack(), HanoiStack(), HanoiStack()]
        self.size = 0
    
    def setHeight(self, height):
        """Clears the spindles, then creates a stack of numbered elements from b (at bottom) to 1 (at top) on spindle 0."""
        self.clearSpindles()
        for i in range(height):
            self.spindle[0].push(height - i)
        self.size = height
    
    def movesNeeded(self):
        """Returns the minimum number of moves needed to solve the stacks."""
        return (2 ** self.size) - 1
    
    def actualMove(self, diskNum, source, dest):
        """Actually moves a disk from one spindle to another. Throws an exception if the disk number doesn't match 
        what's on top of the source spindle (unless we're clearing the stack because of an early exit)."""
        disk = self.spindle[source].pop()
        if disk != diskNum:
            raise Exception("Disk mismatch!")
        self.spindle[dest].push(disk)
        time.sleep(.05)
    
    def run(self):
        """Runs the program. This is a seperate function call because you can neither reference self in a function 
        heading nor overload a function name (ie, I can't call 
            solve(self, diskNum = self.size, source = 0, dest = 1, temp = 2) 
        ).
        """
        self.solve(self.size, 0, 1, 2)
    
    def solve(self, diskNum, source, dest, temp):
        """The main recursive function."""
        if diskNum == 1:
            self.actualMove(diskNum, source, dest)
        else:
            self.solve(diskNum - 1, source, temp, dest)
            self.actualMove(diskNum, source, dest)
            self.solve(diskNum - 1, temp, dest, source)
