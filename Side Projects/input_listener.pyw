import tkinter

class InputListener(tkinter.Frame):
        
    def __init__(self, master):
        """Initialize frame and components."""
        super(InputListener, self).__init__(master)
        master.title("KeyTest")
        self.keepRunning = True
        
        # the frame
        frame = tkinter.Frame(master, width=300, height=300)
        frame.configure(bg = "orangered")
        self.passEvents(frame)
        
        # the field
        self.userMsg = tkinter.StringVar("")
        userMsgBox = tkinter.Label(master, textvariable = self.userMsg, anchor = "c")
        userMsgBox.place(x = 0, y = 100, width = 300, height = 100)
        userMsgBox.configure(bg = "cyan")
        self.passEvents(userMsgBox)
        
        # finish setup
        frame.pack()
        frame.focus_set()
        master.mainloop()
        
        self.infiniteLoop()
    
            
    def infiniteLoop(self):
        """This is just to demonstrate that the events (keyboard and mouse) are threaded."""
        while self.keepRunning:
            pass
    
    def keyPress(self, event):
        """Print to the field when a key is pressed."""
        self.userMsg.set("Pressed '{}'".format(event.keysym))
    
    def mouseClick(self, event):
        """Print mouseclicks to the field."""
        self.userMsg.set("Mouse button {} clicked at {}, {}".format(event.num, event.x, event.y))

    def passEvents(self, obj):
        """While the frame always catches key events, if the field is clicked it catches the mouse event. All widgets should be passed to this function, 
        or they'll be 'dead zones' for mouse clicks."""
        obj.bind("<Key>", self.keyPress)
        obj.bind("<Button>", self.mouseClick)
    
    def destroy(self):
        """Ends the infinite loop from the constructor before exiting (otherwise Python keeps running in the background)."""
        self.keepRunning = False
        tkinter.Frame.destroy(self)
        
    

if __name__ == "__main__":
    InputListener(tkinter.Tk())