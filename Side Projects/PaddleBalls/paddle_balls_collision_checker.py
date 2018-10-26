
import paddle_balls_ball
import paddle_balls_paddle
import random

class CollisionChecker():
    """Manages collisions."""
    
    def __init__(self):
        """Initialize the list of objects to be managed."""
        self.checkList = []
    
    def add(self, obj):
        """Append an item. The paddle should be the last item added."""
        self.checkList.append(obj)
    
    def tickElapsed(self):
        """When kicked by timer, check if any objects are colliding, and bounce them if they are."""
        i = 0
        for i in range(0, len(self.checkList)):
            self.wallCheck(self.checkList[i])
            for j in range(i + 1, len(self.checkList)):
                CollisionChecker.check(self.checkList[i], self.checkList[j])
            
    @staticmethod
    def ballsAreColliding(ball1, ball2):
        """Checks if two balls are colliding, returning a boolean."""
        xDist = abs(ball1.xLoc - ball2.xLoc)
        yDist = abs(ball1.yLoc - ball2.yLoc)
        if xDist <= (ball1.radius() + ball2.radius()) and yDist <= (ball1.radius() + ball2.radius()):
            return True
        return False
    
    @staticmethod
    def pointInPaddle(point, paddle):
        """Checks if a point (a tuple with two ints) is inside a paddle. Returns a boolean."""
        horizontallyWithin = point[0] >= paddle.xLoc and point[0] <= paddle.xLoc + paddle.size
        verticallyWithin = point[1] >= paddle.yLoc and point[1] <= paddle.yLoc + paddle.size
        return horizontallyWithin and verticallyWithin
    
    @staticmethod
    def check(obj1, obj2):
        """Checks if two objects are colliding, calling their collision methods if they are. 
            obj1 smust always be a ball"""
        
        #Collided with another ball
        if type(obj2) == paddle_balls_ball.PBBall:
            if CollisionChecker.ballsAreColliding(obj1, obj2):
                obj1.collideWithBall(obj2)
        
        #Collided with paddle
        if type(obj2) == paddle_balls_paddle.PBPaddle:
            collisionPoints = obj1.getCollisionPoints()
            vertBounce = 0
            horizBounce = 0
            
            if CollisionChecker.pointInPaddle(collisionPoints[0], obj2): # N sensor
                obj1.bounce("south")
            if CollisionChecker.pointInPaddle(collisionPoints[1], obj2): # E sensor
                obj1.bounce("west")
            if CollisionChecker.pointInPaddle(collisionPoints[2], obj2): # S sensor
                obj1.bounce("north")
            if CollisionChecker.pointInPaddle(collisionPoints[3], obj2): # W sensor
                obj1.bounce("east")
    
    @staticmethod
    def wallCheck(obj1):
        """Checks if an object is colliding with a wall, and bounces it back if it is."""
        if obj1.xLoc <= 0:
            obj1.bounce("east")
        elif obj1.yLoc <= 0:
            obj1.bounce("south")
        elif obj1.xLoc >= 600 - obj1.size:
            obj1.bounce("west")
        elif obj1.yLoc >= 600 - obj1.size:
            obj1.bounce("north")