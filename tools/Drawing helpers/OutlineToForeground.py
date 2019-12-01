
from outlineFitterPen import OutlineFitterPen, MathPoint

offsetAmount = 50

g = CurrentGlyph()
gm = g.getLayer("model")
gl = g.getLayer("foreground")

gl.prepareUndo("Outline")

gl.clear()
gl.appendGlyph(gm)

pen = OutlineFitterPen(None, offsetAmount, connection="Round", cap="Round", closeOpenPaths=True, alwaysConnect=False) 
gl.draw(pen)
gl.clear()
pen.drawSettings(drawOriginal=False, drawInner=True, drawOuter=True)
pen.drawPoints(gl.getPointPen())

gl.performUndo()