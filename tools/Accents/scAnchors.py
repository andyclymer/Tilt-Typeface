f = CurrentFont()



# Move anchors to SC from UC
# (Start by selecting SC glyphs)



def getRelativeBoundsLoc(g, absloc):
    # Returns the percentage (x, y) for where absloc is within (or outside) bounds
    bounds = g.bounds
    xVal = (absloc[0] - bounds[0]) / (bounds[2] - bounds[0])
    yVal = (absloc[1] - bounds[1]) / (bounds[3] - bounds[1])
    return (xVal, yVal)

def setRelativeBoundsLoc(g, relativeLoc, doRound=False):
    # Convert the relativeLoc into an absolute loc position within (or outside) bounds
    bounds = g.bounds
    xVal = ((bounds[2] - bounds[0]) * relativeLoc[0]) + bounds[0]
    yVal = ((bounds[3] - bounds[1]) * relativeLoc[1]) + bounds[1]
    if doRound:
        xVal = int(round(xVal))
        yVal = int(round(yVal))
    return (xVal, yVal)


for gn in f.selection:
    capName = gn.title() # Title case first
    if not capName in f:
        capName = capName.upper() # Then all cap
        if not capName in f:
            if capName == "KRA": capName = "K"
            if capName == "DOTLESSI": capName = "I"
            if capName == "DOTLESSJ": capName = "J"
    
    g = f[gn]
    gUC = f[capName]
    
    g.clearAnchors()
    
    # Take all anchors from the cap glyph and shift to match the new bounding box horizontally
    # Move all top anchors down the difference beetween cap and small cap height
    
    for a in gUC.anchors:
        relativeLocUC = getRelativeBoundsLoc(gUC, a.position)
        absLocLC = setRelativeBoundsLoc(g, relativeLocUC, doRound=True)
        g.appendAnchor(a.name, absLocLC)
        print("%s %s" %(gn, a.name))

print("Done")
        