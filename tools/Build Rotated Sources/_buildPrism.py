import os
import glob

from RotateMaster import buildDesignSpace

glyphNames = ['.notdef']

masterPath = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Prism/Masters/Tilt-Prism.ufo"
destPath = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Prism/"
destInline = os.path.join(destPath, "Rotated 01 Inline")
destOutline = os.path.join(destPath, "Rotated 02 Outline")
destCombined = os.path.join(destPath, "Rotated 03 Combined")

doInline = True
doOutline = True
doCombine = True

if doInline:
    buildDesignSpace(
        masterFont=masterPath, 
        destPath=destInline, 
        glyphNames=glyphNames,
        compositionType="rotate", 
        outlineAmount=8, 
        doForceSmooth=True,
        doMakeSubSources=False,
        alwaysConnect=True, # Temporary, force connections to have extra points for compatibility
        cap="Butt",
        connection="Round",
        familyName="Tilt Beta Prism",
        styleName="Regular",
        zOffset=60)
     
if doOutline:
    buildDesignSpace(
        masterFont=masterPath, 
        destPath=destOutline, 
        glyphNames=glyphNames,
        compositionType="rotate", 
        outlineAmount=8, 
        doForceSmooth=True,
        doMakeSubSources=False,
        alwaysConnect=False,
        cap="Roundsimple",
        connection="Round",
        layerName="outline",
        familyName="Tilt Beta Prism",
        styleName="Regular",
        zOffset=60)


if doCombine:
    if not os.path.exists(destCombined):
        os.makedirs(destCombined)
    for outlinePath in glob.glob(os.path.join(destOutline, "*.ufo")):
        fileName = os.path.split(outlinePath)[1]
        inlinePath = os.path.join(destInline, fileName)
        destPath = os.path.join(destCombined, fileName)
        fOutline = OpenFont(outlinePath, showInterface=False)
        fInline = OpenFont(inlinePath, showInterface=False)
        for gn in fOutline.keys():
            gOut = fOutline[gn]
            gIn = fInline[gn]
            for c in gOut.contours:
                gIn.appendContour(c)
        fInline.save(destPath)
        