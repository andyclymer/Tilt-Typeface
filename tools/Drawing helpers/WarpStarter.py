import math
import random
import copy
from fontTools.misc.bezierTools import splitCubicAtT, splitCubic
import vanilla
from fontTools.pens.basePen import BasePen





LIBKEY = "com.andyclymer.zPosition"


def getOpposite(angle, adjacent):
    # Get the opposite side of a triangle if we have the angle and the adjacent length
    if not angle == 0:
        opposite = math.tan(math.radians(angle)) * adjacent
        return opposite
    else: return 0
    
def getAngle(pt0, pt1):
    return 90 - math.degrees(math.atan2(pt0[1]-pt1[1], pt1[0]-pt0[0]))
    
def interpolate(f, x0, x1):
    return x0 + (x1 - x0) * f
    
def interpolatePoints(f, p0, p1, roundValue=False):
    x = interpolate(f, p0[0], p1[0])
    y = interpolate(f, p0[1], p1[1])
    if roundValue:
        return (int(round(x)), int(round(y)))
    else: return (x, y)

def interpLib(f, lib0, lib1, doRound=True):
    newLib = {}
    for k in lib0.keys():
        if k in lib1.keys():
            v = interpolate(f, lib0[k], lib1[k])
            if round:
                v = int(round(v))
            newLib[k] = v
    return newLib

def splitWithAngle(curve, loc, axis):
    # Split a curve at location y and return the location and angle
    r = splitCubic(*curve, loc, isHorizontal=axis)
    if len(r) == 2:
        splitLoc = r[0][-1]
        a = getAngle(r[0][-1], r[1][1]) # handle to handle
    else:
        # The location is either exatly on the end of the curve, or off the curve
        # Return the angle and location either at the top or bottom
        if loc >= curve[0][axis]:
            splitLoc = curve[0]
            a = getAngle(curve[0], curve[1])
        else:
            splitLoc = curve[-1]
            a = getAngle(curve[-2], curve[-1])
    if axis == 0:
        a = 90 - a
    return splitLoc, a
    
def makeUniqueName(length=None):
    if not length:
        length = 8
    name = ""
    for i in range(length):
        name += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return name

def absoluteBCP(anchor, bcp):
    return (anchor.x - bcp.x, anchor.y - bcp.y)

    

        
def warpGlyph(g, angle=-40, floatingDist=120, axis=1):
    # axis = axis to warp along, 1 = use "y" axis for measurement

    if len(g.contours):
        
        # Get the bounds of the glyph drawing for the warp curve
        boundMax = g.bounds[axis+2]
        boundMin = g.bounds[axis]
        """
        # Optionally increase the bounds to include the BCP locations
        for c in g.contours:
            for pt in c.points:
                ptLoc = (pt.x, pt.y)
                if ptLoc[axis] > boundMax:
                    boundMax = ptLoc[axis]
                if ptLoc[axis] < boundMin:
                    boundMin = ptLoc[axis]
        """
    
        # Find handle locations at 33.3 / 66.7 between these bounds
        p0 = [0, boundMax]
        p3 = [0, boundMin]
        p1y = interpolate(0.3333, boundMax, boundMin)
        p1x = getOpposite(angle, boundMax-p1y)
        p1 = [p1x, p1y]
        p2y = interpolate(0.6667, boundMax, boundMin)
        p2x = getOpposite(angle, p2y-boundMin)
        p2 = [p2x, p2y]
        if axis == 0:
            p0.reverse()
            p1.reverse()
            p2.reverse()
            p3.reverse()
    
        if False: # Draw the curve
            pen = g.getPen()
            pen.moveTo(p0)
            pen.curveTo(p1, p2, p3)
            pen.endPath()
            g.changed()
    
        # Shift this curve so that it's balanced at the floatingDist
        midPt = splitCubicAtT(p0, p1, p2, p3, 0.5)[0][-1][not axis]
        floatShift = int(round((-midPt*0.5) + floatingDist))
        p0[not axis] += floatShift
        p1[not axis] += floatShift
        p2[not axis] += floatShift
        p3[not axis] += floatShift
        warpCurve = [p0, p1, p2, p3]
        
        # Extrapolate the warp curve a little bit to account for any BCPs that are outside the glyph bounds
        pct = 0.2 # extrapolation percentage
        s = splitCubicAtT(*warpCurve, 1+pct) # extrap a little on one end
        warpCurve = s[0]
        s = splitCubicAtT(*warpCurve, 0-pct) # extrap a little on the other end
        warpCurve = s[1]
    
        # For each bpoint in the contour, find where it would it the curve
        # Move bPoint anchors to match the angle of that point on the curve. 
        # Keep the "y" location of all points (including handles) as they move
    
        libData = {}
    
        for c in g.contours:
        
            # Take care of the first moveTo
            pt = c.points[0]
            ptLoc = (pt.x, pt.y)
            splitLoc, angle = splitWithAngle(warpCurve, ptLoc[axis], axis)
            anchorZ = splitLoc[not axis]
            if pt.name == None:
                pt.name = makeUniqueName()
            libData[pt.name] = int(round(anchorZ))
            prevOnCurve = pt
            prevOnCurveLoc = [pt.x, pt.y]
                
            for s in c.segments:
                if len(s.points) == 3:
                    # Split at the prevOnCurve to move this bcpOut
                    bcpOut = absoluteBCP(prevOnCurve, s.points[0])
                    splitLoc, angle = splitWithAngle(warpCurve, prevOnCurveLoc[axis], axis)
                    bcpOutZ = getOpposite(angle, bcpOut[axis]) + libData[prevOnCurve.name]
                    # Split at the new on curve and move the bcpIn
                    bcpIn = absoluteBCP(s.points[-1], s.points[1])
                    endAnchorLoc = (s.points[-1].x, s.points[-1].y)
                    splitLoc, angle = splitWithAngle(warpCurve, endAnchorLoc[axis], axis)
                    anchorZ = splitLoc[not axis]
                    bcpInZ = getOpposite(angle, bcpIn[axis]) + anchorZ
                
                    # Three points now have three "z" values
                    # bcpOutZ, bcpInZ, anchorZ
                    zLocs = [bcpOutZ, bcpInZ, anchorZ]
                    for ptIdx, pt in enumerate(s.points):
                        if pt.name == None:
                            pt.name = makeUniqueName()
                        libData[pt.name] = int(round(zLocs[ptIdx]))
                else:
                    pt = s.points[0]
                    ptLoc = (pt.x, pt.y)
                    splitLoc, angle = splitWithAngle(warpCurve, ptLoc[axis], axis)
                    anchorZ = splitLoc[not axis]
                    if pt.name == None:
                        pt.name = makeUniqueName()
                    libData[pt.name] = int(round(anchorZ))
                # Hold the previous onCurve for the next segment
                prevOnCurve = s.points[-1]
                prevOnCurveLoc = (prevOnCurve.x, prevOnCurve.y)
           
        if LIBKEY in g.lib.keys():
            g.lib[LIBKEY].clear()
        g.lib[LIBKEY] = copy.deepcopy(libData)

        g.changed()



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
        bcpOutPt = interpolatePoints(0.33, self.prevPt, pt, roundValue=True)
        bcpInPt = interpolatePoints(0.67, self.prevPt, pt, roundValue=True)
        self.pen.curveTo(bcpOutPt, bcpInPt, pt)
        self.prevPt = pt

    def _curveToOne(self, pt1, pt2, pt3):
        self.pen.curveTo(pt1, pt2, pt3)
        self.prevPt = pt3

    def _closePath(self):
        pt = self.firstPt
        bcpOutPt = interpolatePoints(0.33, self.prevPt, pt, roundValue=True)
        bcpInPt = interpolatePoints(0.67, self.prevPt, pt, roundValue=True)
        self.pen.curveTo(bcpOutPt, bcpInPt, pt)
        self.pen.closePath()
        self.prevPt = None

    def _endPath(self):
        self.pen.endPath()
        self.prevPt = None
        
        

class WarpWindow:
    
    def __init__(self):
        self.w = vanilla.FloatingWindow((140, 205), "Warp Starter")
        step = 10
        self.w.decomposeButton = vanilla.SquareButton((10, step, -10, 25), "Decomp/Overlaps", sizeStyle="small", callback=self.doDecompose)
        step += 30
        self.w.curveButton = vanilla.SquareButton((10, step, -10, 25), "Curve Segments", sizeStyle="small", callback=self.doCurve)
        step += 30
        self.w.warpHButton = vanilla.SquareButton((10, step, -10, 25), "AutoWarp H", sizeStyle="small", callback=self.doWarp)
        step += 24
        self.w.warpHButton.id = "H"
        self.w.warpHVButton = vanilla.SquareButton((10, step, -10, 25), "AutoWarp H&V", sizeStyle="small", callback=self.doWarp)
        self.w.warpHVButton.id = "HV"
        step += 30
        self.w.warpAngle = vanilla.EditText((10, step, 58, 25), "-35")
        self.w.floatDist = vanilla.EditText((72, step, 58, 25), "120")
        step += 35
        self.w.selectionChoice = vanilla.RadioGroup((10, step, -10, 35), ["Current Glyph", "Selected Glyphs"], sizeStyle="small")
        self.w.selectionChoice.set(0)
        self.w.open()
        
    
    def getGlyphs(self):
        # Glyphs to process
        glyphs = []
        if self.w.selectionChoice.get() == 0:
            # Current Glyph
            g = CurrentGlyph()
            if not g == None:
                glyphs.append(g)
        else:
            # Selected Glyphs
            f = CurrentFont()
            for gn in f.selection:
                g = f[gn]
                glyphs.append(g)
        return glyphs
        
    def doCurve(self, sender):
        glyphs = self.getGlyphs()
        for g in glyphs:
            g.prepareUndo("Curve Segments")
            if not g == None:
                pen = CurvePen(g)
                g.draw(pen)
                resultGlyph = pen.glyph
                g.clearContours()
                g.appendGlyph(resultGlyph)
            g.performUndo()
        
    def doDecompose(self, sender):
        glyphs = self.getGlyphs()
        for g in glyphs:
            g.prepareUndo("Decompose, Remove Overlaps")
            if not g == None:
                for c in g.components:
                    c.decompose()
                g.removeOverlap()
            g.performUndo()
    
    def doWarp(self, sender):
        angle = self.w.warpAngle.get()
        angle = float(angle)
        floatingDist = self.w.floatDist.get()
        floatingDist = int(floatingDist)
        glyphs = self.getGlyphs()

        for g in glyphs:

            g.prepareUndo("Warp Glyph")
            
            thisGlyphAngle = angle
        
            if sender.id == "HV":
                # Use a larger angle for horizontal and vertical warping
                thisGlyphAngle = angle - 10
                # Make a copy of the glyph to warp it a second time on the vertical axis
                gVert = RGlyph()
                gVert.appendGlyph(g)
                # Warp on the vertical axis
                warpGlyph(gVert, thisGlyphAngle, floatingDist, axis=0)
            
            # Warp horizontally
            warpGlyph(g, thisGlyphAngle, floatingDist, axis=1)
        
            # Interpoalte the lib values
            if sender.id == "HV":
                newLib = {}
                if LIBKEY in g.lib.keys() and LIBKEY in gVert.lib.keys():
                    # Only 20% from H to V
                    newLib = interpLib(0.2, g.lib[LIBKEY], gVert.lib[LIBKEY])
                # Apply the new lib values to the glyph
                g.lib[LIBKEY] = copy.deepcopy(newLib)

            g.performUndo()
            g.changed()
            

WarpWindow()