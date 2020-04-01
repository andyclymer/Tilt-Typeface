import os



"""
Compare sub-sources and see if their glyphs match the default.
Mark the glyphs green if they're needed (the glyph is different) or gray if it's not needed (they're the same)


CURRENTLY REWORKING THIS TOOL
Not fully accurate

"""



red = (0.9529, 0.5804, 0.5725, 1.0)
gray = (0, 0, 0, 0.9)#(0.3234, 0.3234, 0.3234, 1.0)
green = (0.6171, 0.9529, 0.5725, 1.0)


fonts = {}
for f in AllFonts():
    if f.path:
        fileName = os.path.split(f.path)[1]
        fonts[fileName] = f
        # Set all SubSource glyphs to gray, they'll turn green if they need to be kept
        if "SubSource" in fileName:
            for g in f:
                g.markColor = gray
                g.changed()



def roundPt(pt):
    return (int(round(pt.x)), int(round(pt.y)))

def areSame(g0, g1):
    # Return True if the points are exactly identical
    for cIdx, c0 in enumerate(g0.contours):
        c1 = g1.contours[cIdx]
        for pIdx, p0 in enumerate(c0.points):
            p1 = c1.points[pIdx]
            if not roundPt(p0) == roundPt(p1):
                return False
    return True

def compare(glyphName):
    
    g = fonts["Source-HROTd_VROTd.ufo"][glyphName]
    
    testFileNames = [("SubSource-HROTdd_VROTd.ufo", "HROTdd"), ("SubSource-HROTd_VROTdd.ufo", "VROTdd")]
    gTest = []
    for fileName, key in testFileNames:
        gTest.append((fonts[fileName][glyphName], key))
    
    # Collect related font names to these "dd" SubSources that we're testing
    gRelated = {"HROTdd": [], "VROTdd": []}
    for fileName in fonts.keys():
        if not fileName in testFileNames:
            for key in gRelated:
                if key in fileName:
                    relatedFont = fonts[fileName]
                    gRelated[key].append(relatedFont[glyphName])

    results = []
    for gt, key in gTest:
        result = areSame(g, gt)
        results.append(result)
        #if result:
        #    gt.markColor = gray # Same, don't need it
        #    gt.changed()
        if not result:
            gt.markColor = green # Keep it, they're different
            gt.changed()
            for gr in gRelated[key]:
                gr.markColor = green
                gr.changed()
        


for gn in fonts["Source-HROTd_VROTd.ufo"].keys():
    compare(gn)

#fileInfo["vSub"]["font"].save()
#fileInfo["hSub"]["font"].save()
#fileInfo["bothSub"]["font"].save()