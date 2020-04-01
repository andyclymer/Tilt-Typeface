import os

"""
Copy glyphs from Model to Master
"""

componentMarkColor = (0.502, 0.502, 0.502, 1.0)
copiedMarkColor = (0.9294, 0.5725, 0.9529, 1.0)

fModel = None
fMaster = None

for f in AllFonts():
    if f.path:
        fileName = os.path.split(f.path)[1]
        print(fileName)
        
        if fileName == "Tilt-Neon-Model.ufo":
            fModel = f
        elif fileName == "Tilt-Neon.ufo":
            fMaster = f


for gn in fModel.keys():
    gModel = fModel[gn]
    
    # Only copy into empty glyph positions
    if not gn in fMaster:
        
        print(gn)
        
        # Make a new glyph
        gMaster = fMaster.newGlyph(gn)
        gMaster.width = gModel.width
        
        # Copy Model "foreground" to Master "model-outlined"
        gmas = gMaster.getLayer("model-outlined")
        gmod = gModel.getLayer("foreground")
        gmas.appendGlyph(gmod)
        gmas.width = gmod.width
        
        # Copy Model "model" to Master "model" 
        gmas = gMaster.getLayer("model")
        gmod = gModel.getLayer("model")
        gmas.appendGlyph(gmod)
        gmas.width = gmod.width
        
        # Copy composite glyphs to the foreground
        if gModel.markColor == componentMarkColor:
            gmas = gMaster.getLayer("foreground")
            gmod = gModel.getLayer("foreground")
            gmas.appendGlyph(gmod)
            gmas.width = gmod.width
    
        # Mark glyph
        if gModel.markColor == componentMarkColor:
            gMaster.markColor = componentMarkColor
        else: gMaster.markColor = copiedMarkColor
        
        
print("Done")