from fontTools.misc.bezierTools import splitCubicAtT


baseFontPath = "../../fonts/TTF/"
fontPaths = {
    "Neon": "Tilt-Neon.ttf",
    "Prism": "Tilt-Prism.ttf",
    "Warp": "Tilt-Warp.ttf"}
    
captionFontPath = baseFontPath + fontPaths["Warp"]
    
w, h = (1200, 600)

curveEaseInOut = [(0, 0), (500, 0), (500, 1000), (1000, 1000)]
curveEaseOut = [(0, 0), (500, 0), (1000, 500), (1000, 1000)]
curveEaseIn = [(0, 0), (0, 500), (500, 1000), (1000, 1000)]
curveLinear = [(0, 0), (333, 333), (667, 667), (1000, 1000)]


def findFactor(minimum, value, maximum):
    maxOffset = maximum - minimum
    valueOffset = value - minimum
    return valueOffset/maxOffset
    
def interpolate(minimum,  maximum, factor):
    return minimum + (maximum - minimum) * factor 
       
AXISINFO = {
    "HROT": dict(name="Horizontal Rotation", minimum=-45, maximum=45, default=0),
    "VROT": dict(name="Vertical Rotation", minimum=-45, maximum=45, default=0)}
    
def drawSliders(varInfo, sliderWidth=300, sliderSpacing=80):
    # Measure the tag label
    font(captionFontPath)
    fontSize(sliderSpacing*0.75)
    tagWidth, tagHeight = textSize("HHHH")
    # Draw
    with savedState():
        scale(0.5)
        translate(sliderSpacing, sliderSpacing-tagHeight)
        # Draw the sliers
        for varTag in varInfo:
            translate(0, sliderSpacing)
            # Label
            fill(1)
            stroke(None)
            strokeWidth(0)
            font(captionFontPath)
            fontSize(sliderSpacing*0.75)
            text(varTag.upper(), (0, 0))
            # Line
            fill(None)
            stroke(1)
            strokeWidth(5)
            lineStart = tagWidth + sliderSpacing*0.25
            lineEnd = sliderWidth+lineStart
            offsetY = tagHeight * 0.15
            line((lineStart, offsetY), (lineEnd, offsetY))
            # Position
            v = varInfo[varTag]
            minimum = AXISINFO[varTag]["minimum"]
            maximum = AXISINFO[varTag]["maximum"]
            f = findFactor(minimum, v, maximum)
            dotLoc = (lineStart + f * sliderWidth, offsetY)
            r = 20
            fill(1)
            stroke(None)
            oval(dotLoc[0]-r, dotLoc[1]-r, r*2, r*2)
            
def interpolate(f, a, b):
    return a + (b - a) * f

def interpolatePoint(f, a, b):
    return (interpolate(f, a[0], b[0]), interpolate(f, a[1], b[1]))

def drawCurve(curve):
    # Draw a curve, for testing
    newPage(1000, 1000)
    path = BezierPath()
    path.moveTo(curve[0])
    path.curveTo(*curve[1:])
    fill(None)
    stroke(0)
    strokeWidth(3)
    drawPath(path)
    fill(0)
    stroke(None)
    fontSize(30)
    text(str(curve), (20, 20))

def split(curve, t):
    # Split a curve and return x and y
    split = splitCubicAtT(curve[0], curve[1], curve[2], curve[3], t)
    split = split[0][-1]
    return split

def getFrameInfo(f, curveX, curveY, curveSpeed, startLoc, endLoc):
    _, f = split(curveSpeed, f)
    f *= 0.001
    fLocX, _ = split(curveX, f)
    _, fLocY = split(curveY, f)
    fLocX *= 0.001
    fLocY *= 0.001
    x = interpolate(fLocX, startLoc[0], endLoc[0])
    y = interpolate(fLocY, startLoc[1], endLoc[1])
    return x, y
    

def drawText(txt, fontPath, var):
    fontSize = 500
    fs = FormattedString()
    fs.append(txt, font=fontPath, fontSize=fontSize, lineHeight=fontSize, fontVariations=var, fill=(0))
    path = BezierPath()
    path.text(fs, (0, fontSize*-0.72), align="center")
    fill(1)
    drawPath(path)
    

def drawPage(x, y, fontPath, duration=1/8):
    newPage(w, h)
    frameDuration(duration)
    fill(0.2)
    rect(0, 0, width(), height())
    with savedState():
        translate(width()*0.5, height()*0.85)
        var = {"HROT":x, "VROT": y}
        drawText("Abc", fontPath, var=var)
    drawSliders(var)
    



def makeAnimation(fontName, fontPath):

    newDrawing()
    
    curveX = curveEaseIn
    curveY = curveEaseIn
    curveSpeed = curveEaseInOut
    startLoc = (0, 0)
    endLoc = (-45, 45)
    totalFrames = 13
    for i in range(totalFrames):
        f = i / (totalFrames + 1)
        x, y = getFrameInfo(f, curveX, curveY, curveSpeed, startLoc, endLoc)
        drawPage(x, y, fontPath)
    
    curve = [(0, 0), (200, 1000), (500, 1000), (1000, 1000)]
    curveSpeed = curveEaseInOut
    startLoc = (-45, 45)
    endLoc = (45, 25)
    totalFrames = 35
    for i in range(totalFrames):
        f = i / (totalFrames + 1)
        x, y = getFrameInfo(f, curve, curve, curveSpeed, startLoc, endLoc)
        drawPage(x, y, fontPath)
    
    curveSpeed = curveEaseInOut
    startLoc = (45, 25)
    endLoc = (-45, -45)
    totalFrames = 20
    for i in range(totalFrames):
        f = i / (totalFrames + 1)
        x, y = getFrameInfo(f, curveEaseInOut, curveEaseInOut, curveSpeed, startLoc, endLoc)
        drawPage(x, y, fontPath)
    
    curveSpeed = curveEaseInOut
    startLoc = (-45, -45)
    endLoc = (45, -45)
    totalFrames = 25
    for i in range(totalFrames):
        f = i / (totalFrames + 1)
        x, y = getFrameInfo(f, curveEaseInOut, curveEaseInOut, curveSpeed, startLoc, endLoc)
        drawPage(x, y, fontPath)
    
    curveSpeed = curveEaseInOut
    startLoc = (45, -45)
    endLoc = (0, 0)
    totalFrames = 15
    for i in range(totalFrames):
        f = i / (totalFrames + 1)
        x, y = getFrameInfo(f, curveLinear, curveLinear, curveSpeed, startLoc, endLoc)
        drawPage(x, y, fontPath)

    # Hold at the end
    drawPage(0, 0, fontPath, duration=1)

    fileName = "Big-%s-Abc.gif" % fontName
    saveImage(fileName)



for fontName, fontPath in fontPaths.items():
    fontPath = baseFontPath + fontPath
    makeAnimation(fontName, fontPath)
    
    