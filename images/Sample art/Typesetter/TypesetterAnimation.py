from fontTools.misc.bezierTools import splitCubicAtT

newDrawing()

w = 1000
h = 1000

fontSize = 900
offset = 280

bgColor = (0, 0, 0)
fgColor = (1, 1, 1)


newDrawing()


def easeCurve(f):
    curve = [(0, 0), (1000, 0), (0, 1000), (1000, 1000)] # ease in-out
    #curve = [(0, 0), (0, 900), (1000, 100), (1000, 1000)] # jump jump
    curve = [(0, 0), (1000, 0), (1000, 0), (1000, 1000)] # ease in
    split = splitCubicAtT(curve[0], curve[1], curve[2], curve[3], f)
    split = split[0][-1][1]
    return split/1000
    
    

def drawFrame(frameCount, txt, font, var):
    
    blinkOn = frameCount % 20 < 10

    newPage(w, h)
    frameDuration(1/15)
    
    fill(*bgColor)
    stroke(None)
    rect(0, 0, w, h)

    if blinkOn:
        strokeWidth(13)
        stroke(*fgColor)
        fill(None)
        line((w-100, 100), (w-100, h-100))

    fill(*fgColor)
    stroke(None)
    
    fs = FormattedString(
        txt,
        font=font,
        fill=fgColor,
        align="right",
        fontVariations=var,
        fontSize=fontSize)

    text(fs, (880, 200))



frameCount = 0

while True:
    
    for styleName in ["Neon", "Prism", "Warp"]:
    
        txt = ""
        font = "Tilt %s" % styleName
        var = dict(HROT=0, VROT=0)
    
        # Type "Tilt"
        for letter in "Tilt ":
            letterDelay = randint(5, 10)
            for i in range(letterDelay):
                drawFrame(frameCount, txt, font, var)
                frameCount += 1
            txt += letter
    
        # ...wait...
        totalFrames = 8
        for i in range(totalFrames):
            drawFrame(frameCount, txt, font, var)
            frameCount += 1
    
        # Rotate V
        totalFrames = 10
        for i in range(totalFrames):
            f = i / (totalFrames - 1)
            eased = easeCurve(f)
            varV = eased * -45
            var = dict(HROT=0, VROT=varV)
            drawFrame(frameCount, txt, font, var)
            frameCount += 1
    
        # ...wait...
        totalFrames = 8
        for i in range(totalFrames):
            drawFrame(frameCount, txt, font, var)
            frameCount += 1
    
        # Rotate H
        totalFrames = 10
        for i in range(totalFrames):
            f = i / (totalFrames - 1)
            eased = easeCurve(f)
            varH = eased * -45
            var = dict(HROT=varH, VROT=varV)
            drawFrame(frameCount, txt, font, var)
            frameCount += 1
    
        # ...wait...
        totalFrames = 3
        for i in range(totalFrames):
            drawFrame(frameCount, txt, font, var)
            frameCount += 1
    
        # Type style name
        for letter in " %s" % styleName:
            letterDelay = randint(5, 10)
            for i in range(letterDelay):
                drawFrame(frameCount, txt, font, var)
                frameCount += 1
            txt += letter
    
        # ...wait...
        totalFrames = 18
        for i in range(totalFrames):
            drawFrame(frameCount, txt, font, var)
            frameCount += 1
        
        # Backspace
        for c in txt:
            for i in range(4):
                txt = txt[:-1]
                drawFrame(frameCount, txt, font, var)
                frameCount += 1
        
    # End the animation after an even number of caret blinks
    for i in range(20):
        if frameCount % 20 == 0:
            break
        drawFrame(frameCount, txt, font, var)
        frameCount += 1
    
    break
    
saveImage("Tilt-Typesetter.gif")