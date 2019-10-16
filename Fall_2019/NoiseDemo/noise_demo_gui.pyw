import tkinter
import random
import noise_demo_canvas_painter as painter
import noise_demo_generator as generator
from noise_demo_2d_array import array2D

class NoiseDemoMain(tkinter.Frame):
   
   def __init__(self, master):
      """Initialize frame and components."""
      super(NoiseDemoMain, self).__init__(master)
      master.title("Noise Demo")
      
      self.displaySize = 500
      self.halfSize = self.displaySize // 2
      
      # make the canvas
      self.canvas = tkinter.Canvas(master, width = self.displaySize + 200, height = self.displaySize + 100)
      self.canvas.pack()
      
      # make the widgets
      randomButton = tkinter.Button(master, text = "Random Noise", command = self.generateRandom)
      randomButton.place(x = self.displaySize, y = 0, width = 200, height = 100)
      
      perlin1DButton = tkinter.Button(master, text = "1D Perlin Noise", command = self.generate1DPerlin)
      perlin1DButton.place(x = self.displaySize, y = 100, width = 200, height = 100)
      
      perlin2DButton = tkinter.Button(master, text = "2D Perlin Noise", command = self.generate2DPerlin)
      perlin2DButton.place(x = self.displaySize, y = 200, width = 200, height = 100)
      
      octaveLabel = tkinter.Label(master, text = "Octaves:")
      octaveLabel.place(x = self.displaySize, y = 300, width = 100, height = 50)
      self.octaveField = tkinter.Entry(master)
      self.octaveField.insert(0, "1")
      self.octaveField.place(x = self.displaySize + 100, y = 300, width = 100, height = 50)
      
      self.interpVal = tkinter.StringVar(master)
      optionTuple = {"Linear Interpolation", "Cosine Interpolation"}
      self.interpVal.set("Cosine Interpolation")
      self.interpDD = tkinter.OptionMenu(master, self.interpVal, *optionTuple)
      self.interpDD.place(x = self.displaySize, y = 350, width = 200, height = 50)
      
      xStepLabel = tkinter.Label(master, text = "X Step\nSample Rate:")
      xStepLabel.place(x = self.displaySize, y = 400, width = 100, height = 50)
      self.xStepField = tkinter.Entry(master)
      self.xStepField.insert(0, "50")
      self.xStepField.place(x = self.displaySize + 100, y = 400, width = 100, height = 50)
      
      yStepLabel = tkinter.Label(master, text = "Y Step\nSample Rate")
      yStepLabel.place(x = self.displaySize, y = 450, width = 100, height = 50)
      self.yStepField = tkinter.Entry(master)
      self.yStepField.insert(0, "50")
      self.yStepField.place(x = self.displaySize + 100, y = 450, width = 100, height = 50)
      
      # start the main thread for the canvas
      master.mainloop()
   
   def getParams(self):
      """
      Collect paramaters from entry fields and return as a list.
      """
      octaves = int(self.octaveField.get())
      xStepFreq = int(self.xStepField.get())
      yStepFreq = int(self.yStepField.get())
      size = self.halfSize # half size so that we do 62k pixels per octave rather than a quarter million
      interp = self.interpVal.get().split()[0].lower()
      return [octaves, xStepFreq, yStepFreq, size, interp]
   
   def generateRandom(self):
      painter.paint(self.canvas, generator.getRandomNoise(self.halfSize))
   
   def generate1DPerlin(self):
      painter.paint(self.canvas, generator.get1DChoir(self.getParams()))
   
   def generate2DPerlin(self):
      painter.paint(self.canvas, generator.get2DChoir(self.getParams()))

if __name__ == "__main__":
   NoiseDemoMain(tkinter.Tk())
