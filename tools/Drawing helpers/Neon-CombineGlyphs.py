import copy

"""
Copy foreground and depth lib data from one glyph to another
2020_01_28ac
"""


sourceNames = ["arrowNW"]
destName = "arrowSW"

LIBKEY = "com.andyclymer.zPosition"

f = CurrentFont()
gDest = f[destName]

# Clear contours, but leave anchors, components, etc.
gDest.clearContours()

for sourceName in sourceNames:
    
    gSource = f[sourceName]
    
    # Copy contours
    for c in gSource.contours:
        gDest.appendContour(c)
    
    # Copy lib data
    if LIBKEY in gSource.lib.keys():
        if not LIBKEY in gDest.lib.keys():
            gDest.lib[LIBKEY] = dict()
        for ptName in gSource.lib[LIBKEY]:
            gDest.lib[LIBKEY][ptName] = gSource.lib[LIBKEY][ptName]

    gDest.changed()

print("Done")