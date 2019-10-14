import random
import math
from noise_demo_2d_array import array2D

def interpolateLinear(p1, p2, xOff):
   """
   Takes two points, and how far from the first to the second the you're looking for
   (in the domain of [0.0, 1.0))
   """
   return p1 + ((p2 - p1) * xOff)

def interpolateCosine(p1, p2, xOff):
   """
   Takes two points, and how far from the first to the second the you're looking for
   (in the domain of [0.0, 1.0))
   """
   xOff = ((-1.0 * math.cos(math.pi * xOff)) *.5) + .5
   return interpolateLinear(p1, p2, xOff)

def get1DNoiseValue(point, valList, interpolation = "cosine"):
   """
   Calculates 1D noise on a given point (double), and a list of values (doubles).
   """
   # set interpolation style, defaulting to cosine
   interpStyle = interpolateCosine
   if interpolation == "linear":
      interpStyle = interpolateLinear
   # set values, wrapping if too big
   pt1 = int(point)   # left point
   if pt1 >= len(valList):
      pt1 = pt1 % len(valList)
   pt2 = pt1 + 1      # right point
   if pt2 >= len(valList):
      pt2 = 0
   xOff = point - pt1 # remainder
   return interpStyle(valList[pt1], valList[pt2], xOff)

def get2DNoiseValue(xPoint, yPoint, valArr, interpolation = "cosine"):
   """
   Calculates 2D noise on a given point (double, double), and a 2D array of values.
   """
   # set interpolation style, defaulting to cosine
   interpStyle = interpolateCosine
   if interpolation == "linear":
      interpStyle = interpolateLinear
   # determine values
   xPoint = xPoint % valArr.width; # bind to array boundries
   yPoint = yPoint % valArr.height;
   xOrigin = int(xPoint) # floor to get starting indices
   yOrigin = int(yPoint)
   xTerminus = xOrigin + 1 # ending indices are n + 1
   yTerminus = yOrigin + 1
   # wrap if beyond array bounds
   if xTerminus == valArr.width:
      xTerminus = 0
   if yTerminus == valArr.height:
      yTerminus = 0
   xInset = xPoint - xOrigin # how far from the start
   yInset = yPoint - yOrigin
   
   # actual point locations
   p1 = valArr.get(xOrigin, yOrigin)
   p2 = valArr.get(xTerminus, yOrigin)
   p3 = valArr.get(xOrigin, yTerminus)
   p4 = valArr.get(xTerminus, yTerminus)
   
   # interpolate
   px1 = interpStyle(p1, p2, xInset)
   px2 = interpStyle(p3, p4, xInset)
   return interpStyle(px1, px2, yInset)

def getRandomNoise(size):
   arr = array2D(size, size)
   for x in range(size):
      for y in range(size):
         arr.set(random.random(), x, y)
   return arr

def get1DPerlinNoise(params):
   """
   Returns a single octave of 1D noise
   """
   divisor = params[1]
   size = params[3]
   style = params[4]
   # this is what we'll eventually output
   noiseArr = [0.0] * size
   # make a 1D array of random values at 1/n size
   randomArr = [0.0] * (size // divisor)
   for i in range(len(randomArr)):
      randomArr[i] = random.random()
   for j in range(len(noiseArr)):
      noiseArr[j] = get1DNoiseValue(j / divisor, randomArr, style)
   return noiseArr

def get1DChoir(params):
   """
   Creates several octaves of 1D noise, then hands them off to be combined
   and returns that combination.
   """
   octaves = params[0]
   if octaves == 1:
      return get1DPerlinNoise(params)
   noiseList = []
   for i in range(octaves):
      noiseList.append(get1DPerlinNoise(params))
      # each octave has half the smoothness of the previous
      params[1] = params[1] // 2
   return combine1DNoise(noiseList)

def combine1DNoise(noiseList):
   """
   Combines several octaves of 1D noise. Each octave impacts the final output
   twice as much as the next.
   """
   totalOctaves = len(noiseList)
   listLen = len(noiseList[0])
   totalWeight = (2 ** totalOctaves) - 1
   outArr = [0.0] * listLen
   weightArr = []
   # calculate octave weights
   for i in range(totalOctaves):
      weightArr.append((2 ** (totalOctaves - i - 1)) / totalWeight)
   # combine, factoring in weights
   for x in range(listLen):
      for j in range(totalOctaves):
         outArr[x] += noiseList[j][x] * weightArr[j]
   return outArr

def get2DPerlinNoise(params):
   """
   Returns a single octave of 2D noise
   """
   xDivisor = params[1]
   yDivisor = params[2]
   size = params[3]
   style = params[4]
   maxDimension = max(xDivisor, yDivisor)
   # this is what we'll eventually output
   noiseArr = array2D(size, size)
   # make a 2D array of random values at 1/n size
   randomArr = getRandomNoise(size // maxDimension)
   for x in range(size):
      for y in range(size):
         val = get2DNoiseValue(x / xDivisor, y / yDivisor, randomArr, style)
         noiseArr.set(val, x, y)
   return noiseArr

def get2DChoir(params):
   """
   Creates several octaves of 2D noise, then hands them off to be combined
   and returns that combination.
   """
   octaves = params[0]
   if octaves == 1:
      return get2DPerlinNoise(params)
   noiseList = []
   for i in range(octaves):
      noiseList.append(get2DPerlinNoise(params))
      # each octave has half the smoothness of the previous
      params[1] = params[1] // 2
      params[2] = params[2] // 2
   return combine2DNoise(noiseList)

def combine2DNoise(noiseList):
   """
   Combines several octaves of 2D noise. Each octave impacts the final output
   twice as much as the next.
   """
   totalOctaves = len(noiseList)
   width = noiseList[0].width
   height = noiseList[0].height
   totalWeight = (2 ** totalOctaves) - 1
   outArr = array2D(width, height)
   weightArr = []
   # calculate octave weights
   for i in range(totalOctaves):
      weightArr.append((2 ** (totalOctaves - i - 1)) / totalWeight)
   # combine, accounting for weights
   for x in range(width):
      for y in range(height):
         for j in range(totalOctaves):
            val = outArr.get(x, y)
            val += noiseList[j].get(x, y) * weightArr[j]
            outArr.set(val, x, y)
   return outArr
