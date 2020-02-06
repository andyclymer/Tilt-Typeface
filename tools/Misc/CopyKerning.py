import os


"""
Copy kerning from one UFO into a folder of source UFOs
"""

ufoKpath =     "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Prism/Model/Tilt-Prism-Model.ufo"
sourceFolder = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Prism/Rotated"



fK = OpenFont(ufoKpath, showInterface=False)

for fileName in os.listdir(sourceFolder):
    if fileName.endswith(".ufo"):
        print(fileName)
        
        
        fPath = os.path.join(sourceFolder, fileName)
        
        f = OpenFont(fPath, showInterface=False)
        
        f.groups.clear()
        f.groups.update(fK.groups)
        
        f.kerning.clear()
        f.kerning.update(fK.kerning)
    
        print(len(f.kerning.keys()))
        
        f.save()

print("Done")