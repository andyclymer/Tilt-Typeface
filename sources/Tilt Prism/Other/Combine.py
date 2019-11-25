import os

rotInlinePath = "/Users/clymer/Documents/Code/Git repos/github/andyclymer/Tilt-Typeface/sources/Tilt Prism/Rotated 01 Inline"
rotOutlinePath = "/Users/clymer/Documents/Code/Git repos/github/andyclymer/Tilt-Typeface/sources/Tilt Prism/Rotated 02 Outline"
rotBothPath = "/Users/clymer/Documents/Code/Git repos/github/andyclymer/Tilt-Typeface/sources/Tilt Prism/Other/Rotated skeleton outline"


for fileName in os.listdir(rotInlinePath):
    if fileName.endswith(".ufo"):
        inlineUfoPath = os.path.join(rotInlinePath, fileName)
        outlineUfoPath = os.path.join(rotOutlinePath, fileName)
        savePath = os.path.join(rotBothPath, fileName)
        
        fInline = OpenFont(inlineUfoPath, showInterface=False)
        fOutline = OpenFont(outlineUfoPath, showInterface=False)
        f = NewFont(showInterface=False)
        
        for gn in fInline.keys():
            gInline = fInline[gn]
            gOutline = fOutline[gn]
            f.newGlyph(gn)
            g = f[gn]
            #for c in gInline.getLayer("background").contours:
            #    g.appendContour(c)
            for c in gOutline.getLayer("background").contours:
                g.appendContour(c)
            for c in gInline.getLayer("background").components:
                g.appendComponent(c.baseGlyph, offset=c.offset)
            g.width = gInline.width
            g.unicode = gInline.unicode
        
        
        f.save(savePath)

print("Done")