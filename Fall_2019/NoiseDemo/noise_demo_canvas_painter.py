import tkinter
from noise_demo_2d_array import array2D
from PIL import Image
from PIL import ImageTk

# persistent references for drawing
imgList = []
curImg = None # this is also stored in imgList when calculated

def getGreyTuple(val):
   """
   Return a three-item tuple of the desired grey's color value for RGB calls
   """
   val = int(val * 256)
   return (val, val, val)
   

def paint(canvas, paintingTemplate):
   """
   Paint the canvas, depending on what was passed.
   Brokend apart a bit for readability.
   Drawn at *2 size
   """
   #clear previous data
   global imgList
   global curImg
   for item in imgList:
      canvas.delete(item)
   imgList = []
   
   # declare out of loops so that we're assigning rather than creating
   xx = 0
   yy = 0
   
   # for painting 2d arrays
   if isinstance(paintingTemplate, array2D):
      # create new image
      curImg = Image.new("RGB", (paintingTemplate.width * 2, paintingTemplate.height * 2))
      # pixel setting loop
      for x in range(paintingTemplate.width):
         for y in range(paintingTemplate.height):
            # limit how often we're calculating positions
            xx = x + x
            yy = y + y
            # generate the grey value as a tuple
            greyTuple = getGreyTuple(paintingTemplate.get(x, y))
            # set four pixels
            curImg.putpixel((xx, yy), greyTuple)
            curImg.putpixel((xx + 1, yy), greyTuple)
            curImg.putpixel((xx, yy + 1), greyTuple)
            curImg.putpixel((xx + 1, yy + 1), greyTuple)
      # cast to PhotoImage so it can be drawn
      curImg = ImageTk.PhotoImage(curImg)
      # draw it and save a reference
      imgList.append(canvas.create_image(0, 0, image = curImg, anchor = "nw"))
      
   # for painting 1d arrays
   elif isinstance(paintingTemplate, list):
      height = len(paintingTemplate) * 2
      for x in range(len(paintingTemplate) - 1):
         # get the y-values for the line segment
         y1 = int(paintingTemplate[x] * height) 
         y2 = int(paintingTemplate[x + 1] * height)
         # set the x values for the line segment
         xx = x + x
         # draw a short line segment
         imgList.append(canvas.create_line(xx, y1, xx + 2, y2, fill = "black"))
         
   # request screen update rather than waiting
   canvas.update_idletasks()