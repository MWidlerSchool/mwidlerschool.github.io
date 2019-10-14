import tkinter
from noise_demo_2d_array import array2D

pixelArr = None
lineList = None

def init(canvas, size):
   """
   Initialize the global values used to speed up painting
   """
   global pixelArr
   global lineList
   lineList = []
   pixelArr = array2D(size, size)
   for x in range(size):
      for y in range(size):
         newRect = canvas.create_rectangle(x * 2, y * 2, x * 2, y * 2, outline = "white")
         pixelArr.set(newRect, x, y)

def getGreyString(val):
   """
   Return a string of the desired grey's hex value
   """
   val = int(val * 256)
   val = val + (val * 256) + (val * 65536)
   return "#{:06x}".format(val)
   

def paint(canvas, paintingTemplate):
   """
   Paint the canvas, depending on what was passed.
   Brokend apart a bit for readability.
   """
   global lineList
   global pixelArr
   for item in lineList:
      canvas.delete(item)
   
   if isinstance(paintingTemplate, array2D):
      for x in range(paintingTemplate.width):
         for y in range(paintingTemplate.height):
            # get the value for the pixel on the range 0, 1
            intensityValue = paintingTemplate.get(x, y)
            # express the intensity as a hex value
            greyStr = getGreyString(intensityValue) 
            # draw a 2x2 square
            canvas.itemconfig(pixelArr.get(x, y), outline = greyStr)
   
   elif isinstance(paintingTemplate, list):
      lineList = []
      height = len(paintingTemplate)
      # paint it white
      for x in range(height):
         for y in range(height):
            canvas.itemconfig(pixelArr.get(x, y), outline = "white")
      for x in range(height - 1):
         # get the y-values for the line
         y1 = int(paintingTemplate[x] * height) 
         y2 = int(paintingTemplate[x + 1] * height) 
         # draw a 2x2 square for each point
         lineList.append(canvas.create_line(x * 2, y1 * 2, (x + 1) * 2, y2 * 2, fill = "black"))
   # request screen update rather than waiting
   canvas.update_idletasks() 
   