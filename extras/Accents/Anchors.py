g = CurrentGlyph()
f = g.font
g.appendAnchor("top", (0, f.info.xHeight))
g.appendAnchor("center", (int(g.width*0.5), f.info.xHeight))