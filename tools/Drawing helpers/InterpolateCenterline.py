g = CurrentGlyph()

# Interpolates alternating pairs of contours at 50%

g0 = RGlyph()
g1 = RGlyph()
gi = RGlyph()

if len(g.contours) % 2 == 0:
    for i in range(0, len(g.contours), 2):
        c0 = g.contours[i]
        c1 = g.contours[i+1]
        g0.clear()
        g1.clear()
        g0.appendContour(c0)
        g1.appendContour(c1)
        gi.clear()
        gi.interpolate(0.5, g0, g1)
        g.appendGlyph(gi)