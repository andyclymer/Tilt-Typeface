from outlineFitterPen import MathPoint
from fontTools.misc.bezierTools import splitCubicAtT
import math

g = CurrentGlyph()

cIdx = 0

c = g.contours[cIdx]

prevPoint = MathPoint(c.points[0].x, c.points[0].y)
p1 = MathPoint(c.points[1].x, c.points[1].y)
p2 = MathPoint(c.points[2].x, c.points[2].y)
p3 = MathPoint(c.points[3].x, c.points[3].y)

print(prevPoint, p1, p2, p3)

# ---

# Determine if a curve in/out of a BCP is rotating clockwise or counterclockwise
# Compare vectors of the point to the bcp and the point to the next point
vBcp0 = prevPoint - p1
vNext0 = prevPoint - p3
vBcp1 = p3 - p2
vNext1 = p3 - prevPoint
# Find which way the vector is rotating by looking at the sign of the dot product
dot0 = vBcp0[0] * vNext0[1] - vBcp0[1] * vNext0[0]
dot1 = vBcp1[0] * vNext1[1] - vBcp1[1] * vNext1[0]
# Find the angles
# ang0 = self.prevPoint.angle(p1)
# ang1 = self.pointClass(pt3).angle(p2)
# print(ang0, ang1)
dir0 = 1
dir1 = 1
if dot0 < 0:
    dir0 = -1
if dot1 < 0:
    dir1 = -1
    

print(dir0, dir1)


# ---

splits = splitCubicAtT(prevPoint, p1, p2, p3, 0.01, 0.99)
splitPt0 = MathPoint(splits[0][-1])
splitPt1 = MathPoint(splits[-1][0])
print(splitPt0, splitPt1)

# Then, find difference in angle? Was the problem before what happens when it rolls around zero?
# Subtract the angle of the BCP from the angle of the vector to the split point. Would this zero it out, and we would end up with something either above or below 0?

vBcp0 = prevPoint - p1
vNext0 = prevPoint - splitPt0
vBcp1 = p3 - p2
vNext1 = p3 - splitPt1

aBcp0 = math.atan(vBcp0[1]/vBcp0[0])
aNext0 = math.atan(vNext0[1]/vNext0[0])
#print(aBcp0, aNext0)
print(aNext0-aBcp0)

aBcp1 = math.atan(vBcp1[1]/vBcp1[0])
aNext1 = math.atan(vNext1[1]/vNext1[0])
#print(aBcp1, aNext1)
print(aNext1-aBcp1)




