import os


def setFontInfo(f, familyName, styleName, version=(0, 0), versionString=""):

    infoDict = dict(
    
        familyName = familyName,
        styleName = styleName,
        styleMapFamilyName = "%s %s" % (familyName, styleName),
        styleMapStyleName = "regular",
        
        openTypeNamePreferredFamilyName = familyName,
        openTypeNamePreferredSubfamilyName = styleName,
        openTypeNameCompatibleFullName = "%s %s" % (familyName, styleName),
        
        versionMajor = version[0],
        versionMinor = version[1],
        openTypeNameVersion = "%s.%s %s" % (version[0], version[1], versionString),
        year = 2019,
        copyright = "EARLY BETA VERSION, please don't redistribute! Thanks --Andy",
        trademark = "EARLY BETA VERSION, please don't redistribute! Thanks --Andy",
        
        unitsPerEm = 1000,
        descender = -160,
        xHeight = 517,
        capHeight = 680,
        ascender = 730,
        italicAngle = None,

        openTypeOS2TypoAscender = 990,
        openTypeOS2TypoDescender = -272,
        openTypeOS2TypoLineGap = 0,
        openTypeOS2WinAscent = 990,
        openTypeOS2WinDescent = 272,

        openTypeHheaAscender = 990,
        openTypeHheaDescender = -272,
        openTypeHheaLineGap = 0,

        openTypeNameDesigner = "Andy Clymer",
        openTypeNameDesignerURL = "http://www.andyclymer.com/",
        openTypeNameManufacturer = "Andy Clymer",
        openTypeNameManufacturerURL = "http://www.andyclymer.com/",
        openTypeNameLicense = "EARLY BETA VERSION, please don't redistribute! Thanks --Andy",
        #openTypeNameLicenseURL = "",
        #openTypeNameUniqueID = None,
        #openTypeNameDescription = None,

        openTypeOS2WidthClass = 5,
        openTypeOS2WeightClass = 400,
        #openTypeOS2VendorID = None,
        openTypeOS2Panose = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        #openTypeGaspRangeRecords = ,

        #openTypeOS2SubscriptXSize = ,
        #openTypeOS2SubscriptYSize = ,
        #openTypeOS2SubscriptXOffset = ,
        #openTypeOS2SubscriptYOffset = ,
        #openTypeOS2SuperscriptXSize = ,
        #openTypeOS2SuperscriptYSize = ,
        #openTypeOS2SuperscriptXOffset = ,
        #openTypeOS2SuperscriptYOffset = ,
        #openTypeOS2StrikeoutSize = ,
        #openTypeOS2StrikeoutPosition = ,

        postscriptFontName = "%s-%s" % (familyName.replace(" ", ""), styleName.replace(" ", "")),
        postscriptFullName = "%s %s" % (familyName, styleName),
        #postscriptSlantAngle = ,
        #postscriptUniqueID = ,
        #postscriptUnderlineThickness = ,
        #postscriptUnderlinePosition = ,
        #postscriptIsFixedPitch = ,
        postscriptWeightName = "Regular",
    )
    
    for k, v in infoDict.items():
        setattr(f.info, k, v)
    


sourceFolderPath = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Warp/Rotated Shadow"
for fileName in os.listdir(sourceFolderPath):
    if fileName.endswith(".ufo"):
        ufoPath = os.path.join(sourceFolderPath, fileName)
        
        print(fileName)
        f = OpenFont(ufoPath, showInterface=False)
        
        familyName = "Tilt Beta Warp Shadow"
        styleName = "Regular"
        version = (0, 4)
        versionString = "BETA 2019_12_12"
        
        setFontInfo(f, familyName, styleName, version=version, versionString=versionString)
        
        f.save()

print("Done")
        