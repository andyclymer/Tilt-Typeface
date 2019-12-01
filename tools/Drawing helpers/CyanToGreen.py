green = (0.6171, 0.9529, 0.5725, 1.0)
cyan = (0.5725, 0.9294, 0.9529, 1.0)
for f in AllFonts():
    for g in f:
        if g.markColor == cyan:
            g.markColor = green
            g.changed()