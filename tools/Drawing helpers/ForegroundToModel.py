# Foreground to "model" and clear other layers"
f = CurrentFont()
for g in f:
    for gl in g.layers:
        if not gl == g:
            gl.clear()
    gl = g.getLayer("model")
    gl.appendGlyph(g)
    gl.width = g.width
    g.clear()