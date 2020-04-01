
import copy
import random


markColorMagenta = (0.9294, 0.5725, 0.9529, 1.0)
markColorCyan = (0.5725, 0.9294, 0.9529, 1.0)


"""
Get lib data started in the selected glyphs
If there's no zPosition lib data, assign names to the points and set a default depth
2020_01_28ac
"""
    
def makeUniqueName(length=None):
    if not length:
        length = 8
    name = ""
    for i in range(length):
        name += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return name


LIBKEY = "com.andyclymer.zPosition"

DEFAULTDEPTH = 120

f = CurrentFont()
for gn in f.selection:
    
    g = f[gn]
    
    # If there's no 3D lib data
    if not LIBKEY in g.lib.keys():
        
        # New dict for z value lib data
        libData = {}
    
        # Copy "model" to "foreground"
        gl = g.getLayer("model")
        g.appendGlyph(gl)
    
        # Name points and give them a "z" value in the lib
        for c in g.contours:
            for pt in c.points:
                pt.name = makeUniqueName()
                libData[pt.name] = DEFAULTDEPTH
    
        # Copy to the lib
        g.lib[LIBKEY] = copy.deepcopy(libData)
        
        # Set the mark
        g.markColor = markColorCyan
        g.changed()


