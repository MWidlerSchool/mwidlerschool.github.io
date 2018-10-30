
"""
OL = open list, CL = closed list, H = estimated distance to target,
G = distance traveled so far
	
Procedure:
	1) Add origin node to OL
	2) Node P = the node which has the lowest H+G on the OL.
	3) For each passable cell adjacent to P that is not on the CL,
		if new cell == target, end.
		newG = P.G + entry cost of this node.
		If not on OL: Add to OL.  G = newG
		If on OL: if G > newG, G = newG, parent = P
		else do nothing
   4) Add P to CL.  Go to step 2.

Once you end, then follow the parents back for the target node to find the path.
"""

from a_star_node import AStarNode as Node
from a_star_table import AStarTable as Table
from a_star_list import AStarList
import random
import math

class AStarObj():
    """The main class for an A* pathing function."""
    
    #static constant
    MAX_LOOPS = 1000
    
    def __init__(self, boolMap, start, end, diagOkay = False):
        """Initializer. Also generates the path, if one exists."""
        self.path = None
        self.end = end
        self.start = start
        self.openList = AStarList(Node(start, None, AStarObj.getDistHeur(start, end), 0))
        self.closedList = Table(len(boolMap), len(boolMap[0]))
        self.loops = 0
        path = None
        self.pathExists = self.iterate(boolMap, diagOkay)
    
    def iterate(self, boolMap, diagOkay):
        """Main work method. Follows the procedure outlined at top of this file."""
        hasPath = False
        while hasPath == False and len(self.openList) > 0 and self.loops < AStarObj.MAX_LOOPS:
            node = self.openList.pop()
            locList = [[1, 0, 10], [-1, 0, 10], [0, 1, 10], [0, -1, 10]] #x, y, and distance
            if diagOkay:
                locList += [[1, 1, 14], [1, -1, 14], [-1, 1, 14], [-1, -1, 14]] #x, y, and distance
            for loc in locList:
                curLoc = [node.loc[0] + loc[0], node.loc[1] + loc[1]]
                if boolMap[curLoc[0]][curLoc[1]] and self.closedList.contains(curLoc) == False:
                    if curLoc == self.end:
                        hasPath = True
                        self.openList.pushToFront(Node(curLoc, node, 0, loc[2]))   #if the end is found, it's placed at the front of the list
                    elif self.openList.contains(curLoc):
                        self.openList.update(curLoc, node, loc[2])
                    else:
                        self.openList.push(Node(curLoc, node, AStarObj.getDistHeur(curLoc, self.end), loc[2]))
            self.closedList.add(node.loc)
            self.loops += 1
        return hasPath
    
    def getPath(self):
        """Returns a standard Python list containing the xy coordinates of the path, or an empty list if no path exists."""
        nodePath = []
        if self.pathExists:
            nodePath.append(self.openList.pop())
            while nodePath[len(nodePath) - 1].loc != self.start:
                nodePath.append(nodePath[len(nodePath) - 1].parent)
        locPath = []
        for n in nodePath:
            locPath.append(n.loc)
        return locPath
    
    @staticmethod
    def getDistHeur(origin, terminus):
        """Returns the distance heuristic. Speed can be drastically improved by increasing the multiplier (from 10 to 11, even), but this 
        leads to non-optimal moves near the start."""
        x = origin[0] - terminus[0]
        y = origin[1] - terminus[1]
        return int(math.sqrt((x * x) + (y * y))) * 10
    
    @staticmethod
    def getTestMap(start, end, width, height):
        """Returns a semi-random test map."""
        boolMap = []
        for i in range(width):
            boolMap.append([])
            for j in range(height):
                boolMap[i].append(True)
        for i in range(width):  #paint top and bottom
            boolMap[i][0] = False
            boolMap[i][height - 1] = False
        for i in range(height): #paint left and right
            boolMap[0][i] = False
            boolMap[width - 1][i] = False
        for x in range(1, width - 1):   #random obstacles
            for y in range(1, height - 1):
                if random.randint(0, 100) <= 25:
                    boolMap[x][y] = False
        wallX = 5 + random.randint(0, 5)
        for y in range (1, height):
            boolMap[wallX][y] = False   #random wall
        boolMap[wallX][random.randint(0, 5) + (height // 2)] = True # hole in wall near center
        boolMap[start[0]][start[1]] = True   #ensure start and end are reachable
        boolMap[end[0]][end[1]] = True
        return boolMap
    
    @staticmethod
    def getOutputMap(boolMap, path, start, end):
        """Returns the boolMap as a string map, with the path and endpoints overlain."""
        width = len(boolMap)
        height = len(boolMap[0])
        outMap = []
        for x in range(width):
            outMap.append([])
            for y in range(height):
                outMap[x].append(" ")
        for x in range(width):
            for y in range(height):
                if not boolMap[x][y]:
                    outMap[x][y] = "#"
        for i in path:
            outMap[i[0]][i[1]] = "X"
        outMap[start[0]][start[1]] = "S"
        outMap[end[0]][end[1]] = "E"
        return outMap
    
    
    
if __name__ == "__main__":
    width = 30 + random.randint(0, 31)
    height = 20
    start = [1, random.randint(1, height - 1)]
    end = [width - 2, random.randint(1, height - 1)]
    boolMap = AStarObj.getTestMap(start, end, width, height)
    aStar = AStarObj(boolMap, start, end, True)
    path = aStar.getPath()
    outMap = AStarObj.getOutputMap(boolMap, path, start, end)
    dispStr = []
    for y in range(height):
        dispStr.append(outMap[0][y] + " ")
        for x in range(1, width):
            dispStr[y] += (outMap[x][y] + " ")
    print("Loops: {}".format(aStar.loops))
    print("Path: {}".format(path))
    for i in range(height):
        print(dispStr[i])