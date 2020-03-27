f = CurrentFont()

"""
Andy Clymer

Scale selected anchor locations
"""


for gn in f.selection:
    scaleLoc = None
    g = f[gn]
    for a in g.anchors:
        if a.name in ["_above", "_below"]:
            scaleLoc = a.position
    
    if scaleLoc:
        g.prepareUndo()
        g.scaleBy(0.9, origin=scaleLoc)
        g.round()
        g.performUndo()