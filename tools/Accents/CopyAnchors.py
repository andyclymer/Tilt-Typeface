import vanilla


"""
2020_01_27 Andy Clymer

Copy anchors between UFOs

"""

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



class AnchorCopyWindow:
    
    def __init__(self):
        
        self.fontList = AllFonts()
        self.fontNames = [str(f) for f in self.fontList]
        
        self.w = vanilla.Window((300, 220), "Copy Anchors")
        self.w.fontChoiceTitle0 = vanilla.TextBox((10, 14, -10, 25), "⬇️")
        self.w.fontChoice0 = vanilla.PopUpButton((40, 10, -10, 25), self.fontNames)
        self.w.fontChoiceTitle1 = vanilla.TextBox((10, 44, -10, 25), "➡️")
        self.w.fontChoice1 = vanilla.PopUpButton((40, 40, -10, 25), self.fontNames)
        if len(self.fontNames) > 1:
            self.w.fontChoice1.set(1)
        
        self.w.glyphTitle = vanilla.TextBox((10, 84, -10, 25), "🔠")
        self.w.glyphChoice = vanilla.PopUpButton((40, 80, -10, 25), ["Selected glyphs", "All glyphs"])
        
        self.w.measureTitle = vanilla.TextBox((10, 114, -10, 25), "↔️")
        self.w.measureChoice = vanilla.PopUpButton((40, 110, -10, 25), ["Relative to glyph bounds", "Exact copy"])
        
        self.w.clearFist = vanilla.CheckBox((40, 145, -10, 25), "Clear destination anchors first", value=True)
        
        self.w.copyButton = vanilla.SquareButton((10, 185, -10, 25), "Copy!", callback=self.copyAnchors)
        self.w.open()


    def copyAnchors(self, sender):
        
        font0 = self.fontList[self.w.fontChoice0.get()]
        font1 = self.fontList[self.w.fontChoice1.get()]
        
        if not font0 == font1:
            
            if self.w.glyphChoice.get() == 0:
                glyphList = font1.selection
            else: glyphList = font1.keys()
            
            doMeasure = not self.w.measureChoice.get()
            
            for gn in glyphList:
                if gn in font0.keys():
                    
                    g0 = font0[gn]
                    g1 = font1[gn]
                    
                    if self.w.clearFist.get():
                        g1.clearAnchors()
                    
                    for a in g0.anchors:
                        
                        if doMeasure:
                            relLoc = getRelativeBoundsLoc(g0, a.position)
                            absLoc = setRelativeBoundsLoc(g1, relLoc, doRound=True)
                            g1.appendAnchor(a.name, absLoc)
                        
                        else:
                            g1.appendAnchor(a.name, a.position)

AnchorCopyWindow()

