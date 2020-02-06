import os

"""
Import features into UFOs

"""

sourceFolder = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Neon/Rotated"

basePath = os.path.split(sourceFolder)[0]
print(basePath)
feaPath = os.path.join(basePath, "Features/features.fea")
print(feaPath)

feaFile = open(feaPath, "r")
feaText = feaFile.read()
feaFile.close()

for fileName in os.listdir(sourceFolder):
    if fileName.endswith(".ufo"):
        print(fileName)
        
        fPath = os.path.join(sourceFolder, fileName)
        
        f = OpenFont(fPath, showInterface=False)
        
        f.features.text = feaText
        
        f.save()

print("Done")


