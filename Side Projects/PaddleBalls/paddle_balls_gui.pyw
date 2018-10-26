import tkinter
import random
import threading
import paddle_balls_ball
import paddle_balls_paddle
import paddle_balls_timer
import paddle_balls_collision_checker

class PaddleBallsMain(tkinter.Frame):
    
    def __init__(self, master):
        """Initialize frame and components."""
        super(PaddleBallsMain, self).__init__(master)
        master.title("Paddle Balls")
        
        # make the canvas
        canvas = tkinter.Canvas(master, width = 600, height = 600)
        canvas.pack()
        
        # create the moving objects
        ball = self.getBalls(canvas)
        paddle = paddle_balls_paddle.PBPaddle(canvas)
        paddle.setLoc(200, 200)
        
        # create the collision checker and timer, and hook them up
        cCheck = paddle_balls_collision_checker.CollisionChecker()
        self.timer = paddle_balls_timer.Timer(1/30)
        for i in ball:
            cCheck.add(i)
            self.timer.add(i)
        self.timer.add(cCheck)
        self.timer.add(paddle)
        cCheck.add(paddle)
        
        # send key input to the paddle and grab focus to the window
        canvas.bind("<Key>", paddle.keyInput)
        canvas.focus_set()
        
        master.mainloop()
    
    def getBalls(self, canvas):
        """Generate a bunch of balls."""
        ball = [paddle_balls_ball.PBBall(canvas, color = "red"),
                paddle_balls_ball.PBBall(canvas, color = "orange"),
                paddle_balls_ball.PBBall(canvas, color = "yellow"),
                paddle_balls_ball.PBBall(canvas, color = "green"),
                paddle_balls_ball.PBBall(canvas, color = "blue"),
                paddle_balls_ball.PBBall(canvas, color = "indigo"),
                paddle_balls_ball.PBBall(canvas, color = "violet"),
                paddle_balls_ball.PBBall(canvas, color = "white"),
                paddle_balls_ball.PBBall(canvas, color = "black")]
        for i in range(0, len(ball)):
            ball[i].setLoc(random.randint(0, 100), random.randint(50, 550))
            ball[i].xSpeed = random.randint(10, 15)
            ball[i].ySpeed= random.randint(10, 15)
        return ball
    
    def destroy(self):
        """Terminate the timer on the way out, or it keeps running."""
        self.timer.destroy()
        tkinter.Frame.destroy(self)
        
    

if __name__ == "__main__":
    PaddleBallsMain(tkinter.Tk())