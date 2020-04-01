import os
folder = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Neon/Rotated Shadow"


for fileName in os.listdir(folder):
    if fileName.endswith(".ufo"):
        print(fileName)
        ufoPath = os.path.join(folder, fileName)
        f = OpenFont(ufoPath, showInterface=False)
        g = f["c"]
        g.clear()
        f.save()

print("Done")