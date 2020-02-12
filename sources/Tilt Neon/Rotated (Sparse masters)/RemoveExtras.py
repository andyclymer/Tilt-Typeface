for f in AllFonts():
    for g in f:
        if g.markColor == (0, 0, 0, 0.9):
            f.removeGlyph(g.name)