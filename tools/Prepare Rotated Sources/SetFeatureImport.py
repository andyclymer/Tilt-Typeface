import os

"""
Updates UFO features to point to an imported feature file

"""

sourceFolder = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Warp/Rotated"

for fileName in os.listdir(sourceFolder):
    if fileName.endswith(".ufo"):
        print(fileName)
        
        fPath = os.path.join(sourceFolder, fileName)
        
        f = OpenFont(fPath, showInterface=False)
        
        f.features.text = "include (../Features/features.fea);"
        
        f.save()

print("Done")


