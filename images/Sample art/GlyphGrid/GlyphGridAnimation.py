from fontTools.misc.bezierTools import splitCubicAtT


newDrawing()

w = 1000
h = 1000

fontSize = 350
offset = 280

angles = [-45, 0, 45]
    
    
def hexToRGB(hv):
    # from https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
    return [int(hv[i:i + 2], 16) / 255 for i in (0, 2, 4)]

def easeCurve(f):
    curve = [(0, 0), (1000, 0), (0, 1000), (1000, 1000)] # ease in-out
    #curve = [(0, 0), (0, 900), (1000, 100), (1000, 1000)] # jump jump
    #curve = [(0, 0), (1000, 0), (1000, 0), (1000, 1000)] # ease in
    split = splitCubicAtT(curve[0], curve[1], curve[2], curve[3], f)
    split = split[0][-1][1]
    return split/1000

def drawFrame(factor, txt, font, rate, fgColor, bgColor):

    newPage(w, h)
    frameDuration(rate)
    
    fgColor = hexToRGB(fgColor)
    bgColor = hexToRGB(bgColor)
    
    fill(*bgColor)
    rect(0, 0, w, h)
    
    for iH, aH in enumerate(angles):
        for iV, aV in enumerate(angles):
            
            aHf = aH * factor
            aVf = aV * factor
        
            with savedState():
            
                charOffset = (iH-1) * offset, (iV-1) * offset
            
                translate(w/2, (h/2)-(fontSize*0.3) )
                translate(*charOffset)  

                fs = FormattedString(
                    txt,
                    align="center",
                    font=font,
                    fontSize=fontSize,
                    fill=fgColor,
                    fontVariations=dict(HROT=aHf, VROT=-aVf),
                    openTypeFeatures=dict(dlig=True))

                text(fs, (0, 0))

white = "FFFFFF"
orange = "FF963B"
brick = "C43206"
beige = "FFE8AA"
lavender = "DEA3FF"
lightgreen = "01A17E"
darkgreen = "004621"
lightblue = "61D0FF"
royalblue = "1F00D0"
concrete = "C9C7B2"
elephant = "58584E"
bubblegum = "FF87BC"
grape = "823664"

scenes = [
    ("&", "Tilt Neon", white, elephant),
    ("Q", "Tilt Prism", brick, white),
    ("%", "Tilt Warp", white, lightgreen),
    ("pizza", "Tilt Neon", orange, white),
    ("ę", "Tilt Prism", white, darkgreen),
    ("Z", "Tilt Warp", grape, white),
    ("@", "Tilt Neon", white, brick),
    ("arrowE", "Tilt Prism", elephant, white),
    ("?", "Tilt Warp", white, lavender),
    ("g", "Tilt Neon", darkgreen, white),
    ("3", "Tilt Prism", white, royalblue),
    ("e", "Tilt Warp", orange, white),]

for sIdx, s in enumerate(scenes):
    
    #direction = ((sIdx%2)*2)-1
    direction = sIdx%2
    
    txt, fontName, fgColor, bgColor = s
    
    # hold at 0%
    drawFrame(direction, txt, fontName, 0.5, fgColor, bgColor)
    
    # animate
    totalFrames = 10
    for i in range(totalFrames):
        f = i / totalFrames
        if direction == 1:
            f = 1 - f
        eased = easeCurve(f)
        drawFrame(eased, txt, fontName, 1/15, fgColor, bgColor)

    # hold at 100%
    drawFrame(not direction, txt, fontName, 0.5, fgColor, bgColor)

saveImage("Tilt-GridAnimation.gif")
