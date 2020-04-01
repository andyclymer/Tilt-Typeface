
import copy
import random


markColorMagenta = (0.9294, 0.5725, 0.9529, 1.0)
markColorCyan = (0.5725, 0.9294, 0.9529, 1.0)


"""
Reset depth data for the CurrentGlyph and set to a default starting depth
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

g = CurrentGlyph()

# New dict for z value lib data
libData = {}

# Name points and give them a "z" value in the lib
for c in g.contours:
    for pt in c.points:
        pt.name = makeUniqueName()
        libData[pt.name] = DEFAULTDEPTH

# Copy to the lib
if LIBKEY in g.lib.keys():
    g.lib[LIBKEY].clear()
g.lib[LIBKEY] = copy.deepcopy(libData)

# Set the mark
g.markColor = markColorCyan
g.changed()


