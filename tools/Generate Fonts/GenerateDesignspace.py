from FontInfo import setFontInfo
from variableFontGenerator import BatchDesignSpaceProcessor
import os

path = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Neon/Rotated/Tilt-Neon.designspace"

# Set font info
basePath = os.path.split(path)[0]
for fileName in os.listdir(basePath):
    if fileName.endswith(".ufo"):
        ufoPath = os.path.join(basePath, fileName)
        f = OpenFont(ufoPath, showInterface=False)
        setFontInfo(f, familyName="Tilt", styleName="Neon", version=(0, 1))
        f.save()

# Generate the variable font
#outputPath = path + ".ttf"
#desingSpace = BatchDesignSpaceProcessor(path)
#desingSpace.generateVariationFont(outputPath, autohint=False, releaseMode=True, fitToExtremes=False, report=None)

