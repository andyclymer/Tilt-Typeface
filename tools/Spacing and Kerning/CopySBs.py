import os

rotatedPath = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Neon/Rotated"
sbsPath = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Neon/Rotated SBS ONLY"

# Fixed SBs in the master, re-rotated only for new SBs, using this script to copy metrics into the good fixed up Rotated fonts
# Fix germandbls LSB and RSB, and all other RSBs

names = ["Thorn", "germandbls", "oslash"]

for fileName in os.listdir(sbsPath):
    if fileName.endswith(".ufo"):
        rotatedUfoPath = os.path.join(rotatedPath, fileName)
        sbsUfoPath = os.path.join(sbsPath, fileName)
        
        fRotated = OpenFont(rotatedUfoPath, showInterface=False)
        fSbs = OpenFont(sbsUfoPath, showInterface=False)
        
        # germandbls LSB and RSB
        diff = int(round(fRotated["germandbls"].leftMargin - fSbs["germandbls"].leftMargin))
        fRotated["germandbls"].leftMargin -= diff
        
        # all widths
        for gn in names:
            fRotated[gn].width = fSbs[gn].width
        
        fRotated.save()
        
        
        fRotated.close()
        fSbs.close()