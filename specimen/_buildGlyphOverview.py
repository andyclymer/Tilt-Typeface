import drawBot as db
from ufoProcessor import DesignSpaceProcessor
from fontTools.pens.cocoaPen import CocoaPen
import os


# Font setup

angles = [-45, 0, 45]

dsPath = "../sources/Tilt Warp/Rotated/Tilt-Warp.designspace"
#dsPath = "../sources/Tilt Prism/Rotated 03 Combined/Tilt-Prism.designspace"
#dsPath = "../sources/Tilt Neon/Rotated/Tilt-Neon.designspace"

fileName = os.path.split(dsPath)[1]
baseName = fileName.split(".")[0]
pdfFileName = baseName + "-GlyphOverview.pdf"
HEADER_STYLENAME = baseName.replace("-", " ")
HEADER_URL = "https://github.com/andyclymer/Tilt-Typeface"

ds = DesignSpaceProcessor(useVarlib=True)
ds.read(dsPath)
ds.loadFonts()


# Make instances
instances = {}
for aH in angles:
    for aV in angles:
        i = ds.newInstanceDescriptor()
        i.location = {"Horizontal Rotation": aH, "Vertical Rotation": aV}
        print("Making instance", i.location)
        f = ds.makeInstance(i, doRules=False)
        locStr = "%s %s" % (aH, aV)
        instances[locStr] = f



# Drawing functions


def startNewPage(pageWidth, pageHeight, margin, header):
    db.newPage(pageWidth, pageHeight)
    # Draw the header
    with db.savedState():
        fs = db.FormattedString(
            "%s Glyph Overview\n" % HEADER_STYLENAME,
            font="Tilt Neon",
            fontSize=15)
        fs.append(
            "by Andy Clymer\n%s" % HEADER_URL,
            font="Tilt Neon",
            fontSize=8)
        db.translate(margin, db.height()-header-margin)
        db.textBox(fs, (0, 0, db.width()-(margin*2), header))
    

def drawGlyph(g):
    # Get glyph outline
    f = g.font
    pen = CocoaPen(f)
    g.draw(pen)
    bezierPath = pen.path
    # Draw
    with db.savedState():
        db.translate(-g.width * 0.5, 450) # Center the glyph
        path = db.BezierPath()
        path.setNSBezierPath(bezierPath)
        db.drawPath(path)



def drawCell(glyphName, cellWidth, cellHeight, cellLegendSize):
    
    # Cell outline
    db.fill(None)
    db.stroke(0)
    db.strokeWidth(0.25)
    db.rect(0, 0, cellWidth, cellHeight)
    
    charArea = cellWidth / 3.5
    fontSize = charArea * 0.7
    charStartingOffset = (cellWidth*0.5) - (charArea*1.5)
    
    # Glyph sample
    for iH, aH in enumerate(angles):
        for iV, aV in enumerate(reversed(angles)):
            locStr = "%s %s" % (aH, aV)
            
            f = instances[locStr]
            if glyphName in f:
                g = f[glyphName]
            
                with db.savedState():
                    db.translate(charStartingOffset, charStartingOffset) # Center the nine glyphs in the cell
                    db.translate(iH*charArea, iV*charArea) # Move to the current glyph in the cell
                    db.translate(charArea*0.5, 0) # Offset to center glyph in cell
                    db.translate(0, cellLegendSize*3) # Leave room for the legend
                    # Draw
                    db.fill(0)
                    db.stroke(None)
                    db.scale(fontSize/1000)
                    drawGlyph(g)
                
                # Legend
                db.fill(None)
                db.stroke(0)
                db.strokeWidth(0.25)
                db.lineCap("round")
                db.line((cellLegendSize, cellLegendSize*3), (cellWidth-cellLegendSize, cellLegendSize*3))
                unicodeValueStr = ""
                if g.unicode:
                    unicodeValueStr = hex(g.unicode)
                legendText = "%s\n%s" % (g.name, unicodeValueStr)
                fs = db.FormattedString(
                    legendText,
                    font="Tilt Neon",
                    fontSize=cellLegendSize,
                    tracking=1,
                    lineHeight=cellLegendSize)
                db.text(fs, (cellLegendSize, cellLegendSize*1.7))
    



# Document setup

db.newDrawing()

pageWidth = 8.5 * 72
pageHeight = 11 * 72

margin = 72 # on all sides
header = 72 # on top

cols = 6

cellLegendSize = 6

gridWidth = pageWidth - (margin * 2)
gridHeight = pageHeight - (margin * 2) - header

cellWidth = gridWidth / cols
cellLegendHeight = cellLegendSize* 3
cellHeight = cellWidth + cellLegendHeight


rows = int(round(gridHeight / cellHeight))

    
    

charset = instances["0 0"].glyphOrder

row = 0
col = 0
for i, glyphName in enumerate(charset):
    
    if row == 0 == col:
        startNewPage(pageWidth, pageHeight, margin, header)

    with db.savedState():
        db.translate(margin, margin+gridHeight-cellHeight)
        db.translate(col*cellWidth, -row*cellHeight)
    
        drawCell(glyphName, cellWidth, cellHeight, cellLegendSize)
        
    col += 1
    if col == cols:
        col = 0
        row += 1
    if row == rows:
        row = 0
        col = 0


db.saveImage(pdfFileName)

