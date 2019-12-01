import os

masterFolderPaths = [
    "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Monument/Rotated 03 Combined 16 Shifted",
    "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Neon/Rotated",
    "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Warp/Rotated"]

glyphNames = ["Aring", "Oacute", "parenleft", "Ccedilla", "ccedilla"]


top = 0
topName = None
bottom = 0
bottomName = None

for folderPath in masterFolderPaths:
    for fileName in os.listdir(folderPath):
        if fileName.endswith(".ufo"):
            ufoPath = os.path.join(folderPath, fileName)
            f = OpenFont(ufoPath, showInterface=False)
            for gn in glyphNames:
                g = f[gn]
                if g.box[3] > top:
                    top = g.box[3]
                    topName = ufoPath + " " + gn
                if g.box[1] < bottom:
                    bottom = g.box[1]
                    bottomName = ufoPath + " " + gn


print(top)
print(topName)
print(bottom)
print(bottomName)

"""
1025.0
/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Monument/Rotated 03 Combined 16 Shifted/Source-HROTd_VROTd.ufo Aring
-287.7124376334655
/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Neon/Rotated/SubSource-HROTdd_VROTd.ufo ccedilla
"""