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
        openTypeNameLicense = "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL",
        openTypeNameLicenseURL = "http://scripts.sil.org/OFL",
        #openTypeNameUniqueID = None,
        #openTypeNameDescription = None,

        openTypeOS2WidthClass = 5,
        openTypeOS2WeightClass = 400,
        openTypeOS2VendorID = "ANDY",
        openTypeOS2Panose = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        openTypeGaspRangeRecords = [{'rangeMaxPPEM': 65535, 'rangeGaspBehavior': [1, 2]}],

        #openTypeOS2SubscriptXSize = ,
        #openTypeOS2SubscriptYSize = ,
        #openTypeOS2SubscriptXOffset = ,
        #openTypeOS2SubscriptYOffset = ,
        #openTypeOS2SuperscriptXSize = ,
        #openTypeOS2SuperscriptYSize = ,
        #openTypeOS2SuperscriptXOffset = ,
        #openTypeOS2SuperscriptYOffset = ,
        
        openTypeOS2StrikeoutSize = 100,
        openTypeOS2StrikeoutPosition = 308,
        postscriptUnderlineThickness = 100,
        postscriptUnderlinePosition = 78,

        postscriptFontName = "%s-%s" % (familyName.replace(" ", ""), styleName.replace(" ", "")),
        postscriptFullName = "%s %s" % (familyName, styleName),
        #postscriptSlantAngle = ,
        #postscriptUniqueID = ,
        #postscriptIsFixedPitch = ,
        postscriptWeightName = "Regular",
    )
    
    if "Prism" in familyName:
        infoDict["openTypeOS2StrikeoutSize"] = 16
        infoDict["openTypeOS2StrikeoutPosition"] = 318
        infoDict["postscriptUnderlineThickness"] = 16
        infoDict["postscriptUnderlinePosition"] = 60
    elif "Warp" in familyName:
        infoDict["openTypeOS2StrikeoutSize"] = 155
        infoDict["openTypeOS2StrikeoutPosition"] = 310
        infoDict["postscriptUnderlineThickness"] = 155
        infoDict["postscriptUnderlinePosition"] = 70
    
    for k, v in infoDict.items():
        setattr(f.info, k, v)
    


sourceFolderPath = "/Users/clymer/Documents/Code/Git repos/GitHub/andyclymer/Tilt-Typeface/sources/Tilt Prism/Rotated 03 Combined"
for fileName in os.listdir(sourceFolderPath):
    if fileName.endswith(".ufo"):
        ufoPath = os.path.join(sourceFolderPath, fileName)
        
        print(fileName)
        f = OpenFont(ufoPath, showInterface=False)
        
        familyName = "Tilt Beta Prism"
        styleName = "Regular"
        version = (0, 9)
        versionString = "BETA 2020_02_12"
        
        setFontInfo(f, familyName, styleName, version=version, versionString=versionString)
        
        f.save()

print("Done")
        