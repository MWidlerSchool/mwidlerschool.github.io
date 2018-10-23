import tkinter
import threading
import hanoi_engine
import time
import sys

#declare constants
windowSize = "500x300"
widgetWidth = 250
widgetHeight = 75
stackHeight = 8
    

class Hanoi_GUI(tkinter.Frame):
        
    def __init__(self, master):
        """Initialize frame"""
        super(Hanoi_GUI, self).__init__(master)
        self.engine = hanoi_engine.HanoiEngine()
        self.engine.setHeight(stackHeight)
        self.tower0String = None
        self.tower1String = None
        self.tower2String = None
        self.create_widgets(master)
        self.engineThread = threading.Thread(target = self.engine.run)
        self.guiThread = threading.Thread(target = self.updateScreen)
        self.guiThread.start()
        
    def runButtonPressed(self):
        """Run the program."""
        self.engine.setHeight(stackHeight)
        self.engineThread.start()
        
    def quitButtonPressed(self):
        """Quit out. Threads manually terminated so they don't run on after the window closes."""
        del(self.engineThread)
        del(self.guiThread)
        self.master.destroy()
    
    def updateScreen(self):
        """Endlessly updates the screen. Called by a thread (or else it would lock the program)."""
        while True:
            self.tower0String.set(str(self.engine.spindle[0]))
            self.tower1String.set(str(self.engine.spindle[1]))
            self.tower2String.set(str(self.engine.spindle[2]))

    def create_widgets(self, master):
        """Create the GUI components."""
        self.tower0String = tkinter.StringVar()
        self.tower1String = tkinter.StringVar()
        self.tower2String = tkinter.StringVar()
        self.tower0String.set("")
        self.tower1String.set("")
        self.tower2String.set("")
        tower0Label = tkinter.Label(master, textvariable = self.tower0String, anchor = "w")
        tower0Label.place(x = 0, y = 0, width = widgetWidth, height = widgetHeight)
        
        tower1Label = tkinter.Label(master, textvariable = self.tower1String, anchor = "w")
        tower1Label.place(x = 0, y = widgetHeight, width = widgetWidth, height = widgetHeight)
        
        tower2Label = tkinter.Label(master, textvariable = self.tower2String, anchor = "w")
        tower2Label.place(x = 0, y = widgetHeight * 2, width = widgetWidth, height = widgetHeight)
        
        runButton = tkinter.Button(master, text = "Run", command = self.runButtonPressed)
        runButton.place(x = 0, y = widgetHeight * 3, width = widgetWidth, height = widgetHeight)
        
        quitButton = tkinter.Button(master, text = "Quit", command = self.quitButtonPressed)
        quitButton.place(x = widgetWidth, y = widgetHeight * 3, width = widgetWidth, height = widgetHeight)
        
if __name__ == "__main__":
    root=tkinter.Tk()
    root.title("Towers of Hanoi")
    root.geometry(windowSize)
    app = Hanoi_GUI(master = root)
    root.mainloop()

