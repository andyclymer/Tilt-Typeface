import os

folderPath = "/Users/clymer/Documents/Code/Git repos/github/andyclymer/Tilt-Typeface/sources/Tilt Prism/Other/Rotated skeleton outline"

for fileName in os.listdir(folderPath):
    if fileName.endswith(".ufo"):
        filePath = os.path.join(folderPath, fileName)
        f = OpenFont(filePath, showInterface=False)
        for g in f:
            for c in g.components:
                c.decompose()
        f.save()

print("Done")