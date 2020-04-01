
w = 1600
h = 600


newPage(w, h)

fill(0.2, 0.5, 0.8)
rect(0, 0, w, h)

translate(60, 80)

hrotValue = -25
vrotValue = -25


# Warp
fs = FormattedString()
fs.append("Tilt Warp ", font="Tilt Warp", fontSize=170, fill=1)
fs.append("Abc123@$&!?", font="Tilt Warp", fontSize=170, fontVariations=dict(VROT=vrotValue, HROT=hrotValue))
text(fs, (0, 0))

# Prism
translate(0, 160)
fs = FormattedString()
fs.append("Tilt Prism ", font="Tilt Prism", fontSize=170, fill=1)
fs.append("Abc123@$&!?", font="Tilt Prism", fontSize=170, fontVariations=dict(VROT=vrotValue, HROT=hrotValue))
text(fs, (0, 0))

# Neon
translate(0, 160)
fs = FormattedString()
fs.append("Tilt Neon ", font="Tilt Neon", fontSize=170, fill=1)
fs.append("Abc123@$&!?", font="Tilt Neon", fontSize=170, fontVariations=dict(VROT=vrotValue, HROT=hrotValue))

text(fs, (0, 0))


saveImage("TiltFamilyOverview.png")