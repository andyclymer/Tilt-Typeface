from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, RuleDescriptor
from fontParts.world import OpenFont, NewFont
from ac.data.names import getUniqueName
from euclid import *
from outlineFitterPen import OutlineFitterPen, MathPoint
import math
import os
import copy

import outlineFitterPen
print(outlineFitterPen.__file__)


AXISINFO = {
    "HROT": dict(name="Horizontal Rotation", minimum=-45, maximum=45, default=0),
    "VROT": dict(name="Vertical Rotation", minimum=-45, maximum=45, default=0),
    "DPTH": dict(name="Depth", minimum=-100, maximum=100, default=100),
    "SLEN": dict(name="Shadow Length", minimum=0, maximum=100, default=100),
    "SANG": dict(name="Shadow Angle", minimum=-45, maximum=45, default=45)}
AXISORDER = ["HROT", "VROT", "DPTH", "SLEN", "SANG"]
SLIGHTLYOFFAXIS = 0.01


def getIdent(pt, pointData={}):
    # Get the point name, and set a name if one doesn't exist
    ident = pt.name
    if ident == None:
        ident = getUniqueName(kind="waypoint", otherNames=list(pointData.keys()))
        pt.name = ident
    return ident


ZPOSITIONLIBKEY = "com.andyclymer.zPosition"
def readGlyphPointData(glyph):
    """
    Read the pointData out of the glyph lib
    """
    # Read the zPosition data out of the glyph lib, but retain a dictionary of x,y,z in pointData for easy rotation
    pointData = {}
    # Read the lib data
    if not glyph == None:
        if ZPOSITIONLIBKEY in glyph.lib:
            libData = glyph.lib[ZPOSITIONLIBKEY]
        else: libData = {}
        # Read data out of the lib
        for c in glyph.contours:
            for pt in c.points:
                # bring in the "z" location if it was in the lib (only for points that still exist)
                ident = getIdent(pt)
                if ident in libData:
                    zLoc = libData[ident]
                else: zLoc = 0
                pointData[ident] = dict(x=pt.x, y=pt.y, z=zLoc)
    return pointData


def forceSmooth(bPt):
    """
    Force a bPoint to be smooth by moving its bcps into alignment
    """
    # Convert to mathPoints
    anchorPt = MathPoint(bPt.anchor)
    bcpIn = MathPoint(bPt.bcpIn)
    bcpInPt = anchorPt + bcpIn
    bcpOut = MathPoint(bPt.bcpOut)
    bcpOutPt = anchorPt + bcpOut
    # Get some BCP info
    distIn = anchorPt.distance(bcpInPt)
    angleIn = anchorPt.angle(bcpInPt, add=0)
    distOut = anchorPt.distance(bcpOutPt)
    angleOut = bcpOutPt.angle(anchorPt, add=0)
    # Average the angle
    if not None in [angleOut, angleIn, distOut, distIn]:
        avgAngle = ((distIn * angleIn) + (distOut * angleOut)) / (distIn + distOut)
        # Move the BCPs
        newIn = MathPoint(math.cos(avgAngle), math.sin(avgAngle)) * distIn
        newOut = MathPoint(math.cos(avgAngle), math.sin(avgAngle)) * distOut
        bPt.bcpIn = (newIn.x, newIn.y)
        bPt.bcpOut = (-newOut.x, -newOut.y) 
        


def checkCurveSegmentOverlap(pt0, pt1, pt2, pt3):
    # Check to see if this curve segment overlaps back on itself
    # (i.e. a "hook" segment)
    p0 = MathPoint(*pt0)
    p1 = MathPoint(*pt1)
    p2 = MathPoint(*pt2)
    p3 = MathPoint(*pt3)
    # Angles
    a1 = math.degrees(p0.angle(p1)) # first anchor to its bcp
    a2 = math.degrees(p3.angle(p2)) # second anchor to its bcp
    a3 = math.degrees(p0.angle(p2)) # anchor to anchor
    a4 = math.degrees(p3.angle(p1)) # anchor to anchor
    # Compare angles
    error = 0.6
    doOverlap = False
    if a1-error < a2 < a1+error: # BCPs match angle
        if a1-error < a3 < a1+error: # bcpOut to bcpIn matches angle
            doOverlap = True
        elif a1-error < a4 < a1+error: # bcpOut to next anchor matches angle
            doOverlap = True
    # If they overlap...
    if not doOverlap:
        return []
    else:
        # ...return the axis they overlap on
        if p0[0] == p1[0]:
            return ["x"]
        elif p0[1] == p1[1]:
            return ["y"]
        else: return ["x", "y"]
    
    
def checkCurveOverlap(glyph):
    # Test all segments in the glyph to see if any overlap with themselves
    # Return a list of "x" and "y" for the axis that the overlap aligns on
    prevPrevSeg = None
    prevSeg = None
    glyphResults = []
    for c in glyph.contours:
        for s in c.segments:
            # Check the points in this segment (using the last point of the prevSeg)
            toTest = []
            if prevSeg:
                if len(s.points) == 3: # Curve segments only
                    prevPoint = prevSeg.points[-1]
                    pts = [prevPoint] + list(s.points)
                    pts = [(pt.x, pt.y) for pt in pts]
                    toTest.append(pts)
                    # If the prevPrevSeg was a curve, compare this seg to that seg
                    if prevPrevSeg:
                        if len(prevPrevSeg.points) == 3:
                            pts = [prevPrevSeg.points[2], prevPrevSeg.points[0], s.points[1], s.points[2]]
                            pts = [(pt.x, pt.y) for pt in pts]
                            toTest.append(pts)
            for pts in toTest:
                if pts[0] != pts[1] and pts[2] != pts[3]: # And skip if the handles aren't extended
                    segResults = checkCurveSegmentOverlap(*pts)
                    for result in segResults:
                        if not result in glyphResults:
                            glyphResults.append(result)
                
            prevPrevSeg = prevSeg
            prevSeg = s
    glyphResults.sort()
    return glyphResults
    
    

""" Glyph Transformations """
    

def rotateGlyphPointData(g, loc, pointData, angle=45, aLoc=None):
    
    # Rotation axis
    axisVectorX = Vector3(1, 0, 0)
    axisVectorY = Vector3(0, 1, 0)
    
    # Location in the glph for the rotation to happen
    aLoc = (g.width * 0.5, 
            g.font.info.xHeight * 0.5,
            0)
            
    for c in g.contours:
        for pt in c.points:
            
            # Fetch the point data
            ident = getIdent(pt)
            
            if ident in pointData:
                # and make a vector object
                v = Vector3(pointData[ident]["x"], pointData[ident]["y"], pointData[ident]["z"])
        
                # Invert the "z" position @@@ no longer necessary
                #v.z = -v.z
                #v.z = v.z * 0.5
                # Translate
                m = Matrix4.new_translate(-aLoc[0], -aLoc[1], -aLoc[2])
                v = m.transform(v)
                # Rotate X
                m = m.new_rotate_axis(math.radians(loc["VROT"]), axisVectorX)
                v = m.transform(v)
                # Rotate Y
                m = m.new_rotate_axis(math.radians(loc["HROT"]), axisVectorY)
                v = m.transform(v)
                # Translate
                m = Matrix4.new_translate(aLoc[0], aLoc[1], aLoc[2])
                v = m.transform(v)
            
                # Move the point in the pointData
                pointData[ident]["x"] = v.x
                pointData[ident]["y"] = v.y
                pointData[ident]["z"] = v.z
                
    # Transform the margins
    # Rotate a point from (0, 0) and use the x offset for both margins
    v = Vector3(0, 0, 0)
    m = Matrix4.new_translate(-aLoc[0], -aLoc[1], -aLoc[2])
    v = m.transform(v)
    # Rotate
    m = m.new_rotate_axis(math.radians(loc["HROT"]), axisVectorY)
    v = m.transform(v)
    # Translate
    m = Matrix4.new_translate(aLoc[0], aLoc[1], aLoc[2])
    v = m.transform(v)
    # The "y" value is the LSB and RSB offset
    marginChange = int(round(v[0]))
                
    return marginChange, pointData



def flattenShadow(g, pointData, shadowDirection="right", shadowLengthFactor=1):
    """
    Apply the "z" depth to the "x" and "y" axis to flatten out a shadow
    shadowDirection = "left", "right", "center"
    shadowLengthFactor = multiplier on top of the "z" depth for the length of the shadow
    """
    # Flatten out the "Z" axis as a shadow
    for c in g.contours:
        for p in c.points:
            x = p.x
            y = p.y
            if p.name in pointData:
                z = pointData[p.name]["z"]
                if shadowDirection == "left":
                    x -= z * shadowLengthFactor
                    y -= z * shadowLengthFactor
                elif shadowDirection == "right":
                    x += z * shadowLengthFactor
                    y -= z * shadowLengthFactor
                #else: # straight down
                #    y -= (z + shadowOffset) * shadowLengthFactor
                pointData[p.name]["x"] = x
                pointData[p.name]["y"] = y
                pointData[p.name]["z"] = 0
    return pointData


def outlineGlyph(f, g, offsetAmount, contrast=0, contrastAngle=0, alwaysConnect=False, cap="Roundsimple", connection="Round"):
    """
    Outline a glyph
    """
    # Copy to background
    gl = g.getLayer("background")
    gl.appendGlyph(g)
    # Outline
    try:
        pen = OutlineFitterPen(f, offsetAmount, connection=connection, cap=cap, closeOpenPaths=True, alwaysConnect=alwaysConnect, contrast=contrast, contrastAngle=contrastAngle, preserveComponents=True) 
        g.draw(pen)
        g.clear()
        pen.drawSettings(drawOriginal=False, drawInner=True, drawOuter=True)
        pen.drawPoints(g.getPointPen())
    except:
        print("Problem outlining", g.name)








def buildDesignSpace(
        masterPath=None, 
        destPath=None, 
        glyphNames=[],
        compositionType="rotate", 
        outlineAmount=None, 
        zOffset=None, 
        shadowLengthFactor=1,
        doForceSmooth=False,
        doMakeSubSources=False,
        familyName=None,
        alwaysConnect=False,
        cap="RoundSimple",
        connection="Round",
        layerName=None,
        styleName=None):
    
    # Set up folders
    basePath, masterFileName = os.path.split(masterPath)
    if destPath == None:
        destPath = os.path.join(basePath, "Rotated")
    # Make new folders for the destPath
    if not os.path.exists(destPath):
        os.makedirs(destPath)

    # Open the master UFO
    masterFont = OpenFont(masterPath, showInterface=False)
    
    # Use all glyphs, if no names are called for
    if glyphNames == []:
        glyphNames = list(masterFont.keys())
        glyphNames.sort()
    
    """ Collect glyph data """
    # Organize the point data out of the glyph lib
    # and check to see which glyphs need to be present in a SubSource
    glyphPointData = {}
    needSubHROT = [] # Glyphs that need to be included in a SubSource when HROT is default
    needSubVROT = []
    for gName in glyphNames:
        if gName in masterFont:
            g = masterFont[gName]
            if layerName:
                # Copy point data to the layer
                if ZPOSITIONLIBKEY in g.lib.keys():
                    libdata = copy.deepcopy(g.lib[ZPOSITIONLIBKEY])
                else: libdata = {}
                g = g.getLayer(layerName)
                g.lib[ZPOSITIONLIBKEY] = libdata
            pointData = readGlyphPointData(g)
            glyphPointData[gName] = pointData
            # Test for self-overlapping contours
            if doMakeSubSources == True:
                overlapResult = checkCurveOverlap(g)
                if "x" in overlapResult:
                    needSubHROT.append(gName)
                elif "y" in overlapResult:
                    needSubVROT.append(gName)
    
    """ Organize Source combinations """
    
    # Collect source info, based on the layout type
    # Organize file names, designspace locations, glyph lists, etc.
    sourceCombinations = []
    for locHROT, tagHROT in [(-45, "HROTn"), (0, "HROTd"), (45, "HROTx")]:
        for locVROT, tagVROT in [(-45, "VROTn"), (0, "VROTd"), (45, "VROTx")]:
            if "shadow" in compositionType:
                for locSLEN, tagSLEN in [(0, "SLENn"), (100, "SLENx")]:
                    for locSANG, tagSANG in [(-45, "SANGn"), (45, "SANGx")]:
                        # Rotate and Shadow
                        fileName = "Source-%s_%s_%s_%s.ufo" % (tagHROT, tagVROT, tagSLEN, tagSANG)
                        loc = dict(HROT=locHROT, VROT=locVROT, SLEN=locSLEN, SANG=locSANG)
                        sourceInfo = dict(glyphNames=glyphNames, loc=loc, fileName=fileName, nudgeLoc=[0, 0])
                        sourceCombinations.append(sourceInfo)
            else: # Rotate only, skip the shadow axis data
                fileName = "Source-%s_%s.ufo" % (tagHROT, tagVROT)
                loc = dict(HROT=locHROT, VROT=locVROT)
                sourceInfo = dict(glyphNames=glyphNames, loc=loc, fileName=fileName, nudgeLoc=[0, 0])
                sourceCombinations.append(sourceInfo)
    
    # Process the sourceCombinations and make SubSources if necessary
    print("needSubHROT", needSubHROT)
    print("needSubVROT", needSubVROT)
    # @@@ Temporarily force all glyphs to be in all submasters
    needSubHROT = glyphNames
    needSubVROT = glyphNames
    if doMakeSubSources:
        doSubHROT = len(needSubHROT)
        doSubVROT = len(needSubVROT)
    else:
        doSubHROT = False
        doSubVROT = False
    # Loop through once to add new HROT SubSources
    newSourceCombos = []
    for sourceInfo in sourceCombinations:
        if sourceInfo["loc"]["HROT"] == 0:
            if doSubHROT:
                subSourceInfo = copy.deepcopy(sourceInfo)
                subSourceInfo["nudgeLoc"][0] = 0 # Don't nudge, move the location instead
                subSourceInfo["loc"]["HROT"] += SLIGHTLYOFFAXIS
                subSourceInfo["glyphNames"] = needSubHROT
                subSourceInfo["fileName"] = "Sub" + subSourceInfo["fileName"].replace("HROTd", "HROTdd")
                newSourceCombos.append(subSourceInfo)
                # Nudge the default source
                sourceInfo["nudgeLoc"][0] -= SLIGHTLYOFFAXIS
    sourceCombinations += newSourceCombos
    # Looping back through to add VROT SubSources and to catch all of the new HROT SubSources
    newSourceCombos = []
    for sourceInfo in sourceCombinations:
        if sourceInfo["loc"]["VROT"] == 0:
            if doSubVROT:
                subSourceInfo = copy.deepcopy(sourceInfo)
                subSourceInfo["nudgeLoc"][1] = 0 # Don't nudge, move the location instead
                subSourceInfo["loc"]["VROT"] -= SLIGHTLYOFFAXIS
                # Append the glyph list if this was the HROT=SLIGHTLYOFFAXIS
                if not subSourceInfo["loc"]["HROT"] == SLIGHTLYOFFAXIS:
                    subSourceInfo["glyphNames"] = []
                subSourceInfo["glyphNames"] += needSubVROT
                subSourceInfo["fileName"] = subSourceInfo["fileName"].replace("VROTd", "VROTdd")
                if not "Sub" in subSourceInfo["fileName"]: subSourceInfo["fileName"] = "Sub" + subSourceInfo["fileName"]
                newSourceCombos.append(subSourceInfo)
                # Nudge the default source
                sourceInfo["nudgeLoc"][1] += SLIGHTLYOFFAXIS
    sourceCombinations += newSourceCombos
    
    
    """ Make the source UFOs """
        
    for sourceInfo in sourceCombinations:
        sourceUfoPath = os.path.join(destPath, sourceInfo["fileName"])
        if not os.path.exists(sourceUfoPath):
            sourceFont = NewFont(showInterface=False)
            sourceFont.save(sourceUfoPath)
            sourceFont.info.familyName = familyName
            sourceFont.info.styleName = styleName
            sourceFont.save()
            sourceFont.close()
    

    """ Process Glyphs into Source UFOs """
    
    # Process each UFO source, one at a time
    for sourceInfo in sourceCombinations:
        
        # Combine the nudgeLoc and loc, use this value when rotating
        rotateLoc = copy.deepcopy(sourceInfo["loc"])
        rotateLoc["HROT"] += sourceInfo["nudgeLoc"][0]
        rotateLoc["VROT"] += sourceInfo["nudgeLoc"][1]
        
        sourceUfoPath = os.path.join(destPath, sourceInfo["fileName"])
        sourceFont = OpenFont(sourceUfoPath, showInterface=False)
        
        for gName in sourceInfo["glyphNames"]:
            pointData = copy.deepcopy(glyphPointData[gName])
        
            # Get the glyph started
            g = masterFont[gName]
            if layerName:
                #if ZPOSITIONLIBKEY in g.lib.keys():
                #    libdata = copy.deepcopy(g.lib[ZPOSITIONLIBKEY])
                #else: libdata = {}
                g = g.getLayer(layerName)
                #g.lib[ZPOSITIONLIBKEY] = libdata
            # Remove the glyph if it already existed and make a new one
            if gName in sourceFont:
                for layer in sourceFont.layers:
                    if gName in layer:
                        layer.removeGlyph(gName)
            sourceFont.newGlyph(gName)
            gDest = sourceFont[gName]
            gDest.appendGlyph(g)
            gDest.width = g.width
            gDest.unicode = g.unicode
            
            # Decompose
            """ # @@@ Leaving this out for now, decomposed contours lose their point IDs
            for c in gDest.components:
                baseName = c.baseGlyph
                c.decompose()
                # ...and copy over point data
                #baseGlyph = masterFont[baseName]
                basePointData = copy.deepcopy(glyphPointData[baseName])
                for ident in basePointData:
                    pointData[ident] = basePointData[ident]
            """
            
            # Shift the "z" value by an offset
            if zOffset:
                for ident in pointData:
                    pointData[ident]["z"] += zOffset
        
            # Extend the shadow
            if "SANG" in sourceInfo["loc"].keys():
                if sourceInfo["loc"]["SANG"] == -45:
                    shadowDirection = "left"
                else: shadowDirection = "right"
                finalShadowLengthFactor = (sourceInfo["loc"]["SLEN"] * 0.01) * shadowLengthFactor
                pointData = flattenShadow(gDest, pointData, shadowDirection, finalShadowLengthFactor)
        
            # Rotate the glyph
            # Merge the location and the nudgeLoc, if there is one
            marginChange, pointData = rotateGlyphPointData(gDest, rotateLoc, pointData)
            
            # Move the points
            for c in gDest.contours:
                for pt in c.points:
                    ident = getIdent(pt)
                    if ident in pointData:
                        pt.x = pointData[ident]["x"]
                        pt.y = pointData[ident]["y"]
            
            # Shift the glyph
            gDest.moveBy((-marginChange, 0))
            gDest.width -= marginChange * 2
            # hift the components back?
            for c in gDest.components:
                c.moveBy((marginChange, 0))
            
            if doForceSmooth:
                # If a bPoint was a smooth curve point in the original glyph,
                # force the related bPoint in the rotated glyph to be smooth
                for cIdx, c in enumerate(gDest.contours):
                    for bptIdx, thisBPt in enumerate(c.bPoints):
                        sourceBPt = g.contours[cIdx].bPoints[bptIdx]
                        if sourceBPt.type == "curve":
                            forceSmooth(thisBPt)
            
            # Round the point coordinates before outlining
            gDest.round()
            gDest.changed()
        
            # Outline the glyph
            if outlineAmount:
                outlineGlyph(sourceFont, gDest, outlineAmount, alwaysConnect=alwaysConnect, cap=cap, connection=connection)
                
                # Round the point coordinates again, now that it's outlined
                gDest.round()
                gDest.changed()
                
            # Update
            #gDest.changed()
            
        # Resort the font
        sourceFont.glyphOrder = masterFont.glyphOrder
        
        # Copy the kerning
        sourceFont.groups.update(copy.deepcopy(masterFont.groups))
        sourceFont.kerning.update(copy.deepcopy(masterFont.kerning))
        
        # Done, save
        sourceFont.changed()
        sourceFont.save()
        
 
    """ New DesignSpaceDocument """
        
    designSpace = DesignSpaceDocument()
    designSpaceDocFilename = os.path.splitext(masterFileName)[0] + ".designspace"
    designSpaceDocPath = os.path.join(destPath, designSpaceDocFilename)
    

    """ Axis Descriptors """
        
    for tag in sourceCombinations[0]["loc"].keys():
        a = AxisDescriptor()
        a.minimum = AXISINFO[tag]["minimum"]
        a.maximum = AXISINFO[tag]["maximum"]
        a.default = AXISINFO[tag]["default"]
        a.name = AXISINFO[tag]["name"]
        a.tag = tag
        a.labelNames[u'en'] = AXISINFO[tag]["name"]
        designSpace.addAxis(a)


    """ Source Descriptors """

    for sourceInfo in sourceCombinations:
        sourceUfoPath = os.path.join(destPath, sourceInfo["fileName"])
        # Make a source description
        s = SourceDescriptor()
        s.path = sourceUfoPath
        s.name = os.path.splitext(sourceInfo["fileName"])[0]
        #s.font = defcon.Font(s.name)
        s.copyLib = True
        s.copyInfo = True
        s.copyFeatures = True
        s.familyName = masterFont.info.familyName
        s.styleName = s.name
        # Convert the loc from tags to names
        loc = {}
        for tag, value in sourceInfo["loc"].items():
            axisName = AXISINFO[tag]["name"]
            loc[axisName] = value
        s.location = loc
        designSpace.addSource(s)
    
    

    designSpace.write(designSpaceDocPath)
    
