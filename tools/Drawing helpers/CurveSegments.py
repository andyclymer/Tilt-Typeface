
from fontTools.pens.basePen import BasePen


"""
A pen to make all flat segments into curve segments
2019_10_22 Andy Clymer
"""

def interpolate(f, a, b, roundValue=False):
    value = a + (b - a) * f
    if roundValue:
        return int(round(value))
    else: return value

def interpolatePoint(f, a, b, roundValue=False):
    return (interpolate(f, a[0], b[0], roundValue=roundValue), interpolate(f, a[1], b[1], roundValue=roundValue))



class CurvePen(BasePen):
    
    def __init__(self, glyph):
        BasePen.__init__(self, glyph)
        
        self.glyph = RGlyph()
        self.pen = self.glyph.getPen()
        self.firstPt = None
        self.prevPt = None
        
    def _moveTo(self, pt):
        self.pen.moveTo(pt)
        self.firstPt = pt
        self.prevPt = pt

    def _lineTo(self, pt):
        bcpOutPt = interpolatePoint(0.33, self.prevPt, pt, roundValue=True)
        bcpInPt = interpolatePoint(0.67, self.prevPt, pt, roundValue=True)
        self.pen.curveTo(bcpOutPt, bcpInPt, pt)
        self.prevPt = pt

    def _curveToOne(self, pt1, pt2, pt3):
        self.pen.curveTo(pt1, pt2, pt3)
        self.prevPt = pt3

    def _closePath(self):
        pt = self.firstPt
        bcpOutPt = interpolatePoint(0.33, self.prevPt, pt, roundValue=True)
        bcpInPt = interpolatePoint(0.67, self.prevPt, pt, roundValue=True)
        self.pen.curveTo(bcpOutPt, bcpInPt, pt)
        self.pen.endPath()
        self.prevPt = None

    def _endPath(self):
        self.pen.endPath()
        self.prevPt = None


g = CurrentGlyph()

pen = CurvePen(g)
g.draw(pen)
resultGlyph = pen.glyph
g.clearContours()
g.appendGlyph(resultGlyph)
