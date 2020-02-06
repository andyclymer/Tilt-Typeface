import os

"""
Copy anchors from a set of source fonts to a set of destination fonts
Clears anchros before copying
Assumes that both folders have UFOs with the same names
"""

anchorSourceFonts = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Neon/Rotated (Anchors only)"
destFonts = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Neon/Rotated"


glyphNames = ['ae.alt']


for fileName in os.listdir(anchorSourceFonts):
    if fileName.endswith(".ufo"):
        
        print(fileName)
        
        fSourcePath = os.path.join(anchorSourceFonts, fileName)
        fSoruce = OpenFont(fSourcePath, showInterface=False)
        fDestPath = os.path.join(destFonts, fileName)
        fDest = OpenFont(fDestPath, showInterface=False)
        
        for gn in glyphNames:
            gSource = fSoruce[gn]
            gDest = fDest[gn]
            
            gDest.clearAnchors()
            for a in gSource.anchors:
                gDest.appendAnchor(a.name, a.position)
            
        fDest.save()
        
fSoruce.close()
fDest.close()

print("Done")
            