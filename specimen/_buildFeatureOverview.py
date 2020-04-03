margin = 72
sizeHead = (15, 17)
sizeText = (10, 12)
sizeSample = (15, 17)
sampleIndent = 72/2

colorText = (0)
colorSubTarget = (1, 0.4, 0.2)
colorSubReplacement = (0.2, 0.6, 0.2)
colorSampleDimmed = (0.7)# OpenType feature descriptions and samples

featureInfoNeon = dict(
    styleName = "Tilt Neon",
    features = [
        dict(
            featureTag = "SS01",
            featureName = "Stylistic Set 1",
            featureDescription = "Double storey “a”",
            featureSubs = [
                (("Laundrom_a_t", None), ("Laundrom_a_t", ["ss01"]))]),
        dict(
            featureTag = "SS02",
            featureName = "Stylistic Set 2",
            featureDescription = "Asymmetric “t”",
            featureSubs = [
                (("Favori_t_e", None), ("Favori_t_e", ["ss02"]))]),
        dict(
            featureTag = "SS03",
            featureName = "Stylistic Set 3",
            featureDescription = "Simplified “u”",
            featureSubs = [
                (("Disco_u_nt", None), ("Disco_u_nt", ["ss03"]))]),
        dict(
            featureTag = "DLIG",
            featureName = "Discretionary Ligatures",
            featureDescription = "Text-to-pictogram replacement",
            featureSubs = [
                (("_arrowN_", None), ("_arrowN_", ["dlig"])),
                (("_arrowE_", None), ("_arrowE_", ["dlig"])),
                (("_arrowS_", None), ("_arrowS_", ["dlig"])),
                (("_arrowW_", None), ("_arrowW_", ["dlig"])),
                (("_arrowNE_", None), ("_arrowNE_", ["dlig"])),
                (("_arrowSE_", None), ("_arrowSE_", ["dlig"])),
                (("_arrowSW_", None), ("_arrowSW_", ["dlig"])),
                (("_arrowNW_", None), ("_arrowNW_", ["dlig"])),
                (("_smile_ or _happy_", None), ("_smile_", ["dlig"])),
                (("_frown_ or _sad_", None), ("_frown_", ["dlig"])),
                (("_heart_ or _love_", None), ("_heart_", ["dlig"])),
                (("_star_ or _favorite_", None), ("_star_", ["dlig"])),
                (("_billards_ or _pool_", None), ("_billards_", ["dlig"])),
                (("_bowling_ or _bowl_", None), ("_bowling_", ["dlig"])),
                (("_key_ or _locksmith_", None), ("_key_", ["dlig"])),
                (("_scissors_, _barber_, _salon_ or _cut_", None), ("_scissors_", ["dlig"])),
                (("_shoe_ or _boot_", None), ("_shoe_", ["dlig"])),
                (("_laundry_, _laundromat_, _dryclean_ or _hanger_", None), ("_laundry_", ["dlig"])),
                (("_camera_ or _photo_", None), ("_camera_", ["dlig"])),
                (("_pizza_, _slice_ or _food_", None), ("_pizza_", ["dlig"])),
                (("_wine_, _drink_ or _bar_", None), ("_wine_", ["dlig"])),
                (("_music_, _note_, _song_ or _karaoke_", None), ("_music_", ["dlig"])),
                ]
            ),
        ]
    )
    

featureInfoWarp = dict(
    styleName = "Tilt Warp",
    features = [
        dict(
            featureTag = "SS01",
            featureName = "Stylistic Set 1",
            featureDescription = "Double storey “a”",
            featureSubs = [
                (("Laundrom_a_t", None), ("Laundrom_a_t", ["ss01"]))]),
        dict(
            featureTag = "SS02",
            featureName = "Stylistic Set 2",
            featureDescription = "Asymmetric “t”",
            featureSubs = [
                (("Favori_t_e", None), ("Favori_t_e", ["ss02"]))]),
        dict(
            featureTag = "SS03",
            featureName = "Stylistic Set 3",
            featureDescription = "Simplified “u”",
            featureSubs = [
                (("Disco_u_nt", None), ("Disco_u_nt", ["ss03"]))]),
        dict(
            featureTag = "SS04",
            featureName = "Stylistic Set 4",
            featureDescription = "Enclosed arrows",
            featureSubs = [
                (("_arrowN arrowNE arrowE arrowSE arrowS arrowSW arrowW arrowNW_", ["dlig"]), 
                    ("_arrowN arrowNE arrowE arrowSE arrowS arrowSW arrowW arrowNW_", ["dlig", "ss04"]))]),
        dict(
            featureTag = "DLIG",
            featureName = "Discretionary Ligatures",
            featureDescription = "Text-to-pictogram replacement",
            featureSubs = [
                (("_arrowN_", None), ("_arrowN_", ["dlig"])),
                (("_arrowE_", None), ("_arrowE_", ["dlig"])),
                (("_arrowS_", None), ("_arrowS_", ["dlig"])),
                (("_arrowW_", None), ("_arrowW_", ["dlig"])),
                (("_arrowNE_", None), ("_arrowNE_", ["dlig"])),
                (("_arrowSE_", None), ("_arrowSE_", ["dlig"])),
                (("_arrowSW_", None), ("_arrowSW_", ["dlig"])),
                (("_arrowNW_", None), ("_arrowNW_", ["dlig"])),
                ]
            ),
        ]
    )
    


featureInfoPrism = dict(
    styleName = "Tilt Prism",
    features = [
        dict(
            featureTag = "DLIG",
            featureName = "Discretionary Ligatures",
            featureDescription = "Text-to-pictogram replacement",
            featureSubs = [
                (("_arrowN_", None), ("_arrowN_", ["dlig"])),
                (("_arrowE_", None), ("_arrowE_", ["dlig"])),
                (("_arrowS_", None), ("_arrowS_", ["dlig"])),
                (("_arrowW_", None), ("_arrowW_", ["dlig"])),
                (("_arrowNE_", None), ("_arrowNE_", ["dlig"])),
                (("_arrowSE_", None), ("_arrowSE_", ["dlig"])),
                (("_arrowSW_", None), ("_arrowSW_", ["dlig"])),
                (("_arrowNW_", None), ("_arrowNW_", ["dlig"])),
                ]
            ),
        ]
    )
    

def drawPage(featureInfo):
        newPage("Letter")

    fs = FormattedString()

    # Page title
    fs.append(featureInfo["styleName"], font="Tilt Warp", fontSize=sizeHead[0], lineHeight=sizeHead[1])
    fs.append("\nOpenType Feature Overview", font="Tilt Neon", fontSize=sizeHead[0], lineHeight=sizeHead[1])
    fs.append("\n")

    for featureDict in featureInfo["features"]:
    
        # Feature tag and name
        fs.append(
            "\n\n%s\t%s" % (featureDict["featureTag"], featureDict["featureName"]), 
            fill=colorText,
            font="Tilt Neon",
            fontSize=sizeText[0],
            lineHeight=sizeText[1],
            tabs=[(sampleIndent, "left")])
        
        # Feature description
        fs.append(
            "\n\t%s\n" % featureDict["featureDescription"], 
            fill=colorText,
            fontSize=sizeText[0],
            lineHeight=sizeText[1],
            tabs=[(sampleIndent, "left")])
        
        # Samples
        subOn = False
        for sample in featureDict["featureSubs"]:
        
            for sampleIdx in [0, 1]:
                if sampleIdx == 0:
                    # Target
                    textHighlightColor = colorSubTarget
                    startText = "\t"
                else:
                    # Replacement
                    textHighlightColor = colorSubReplacement
                    startText = " "
        
                # Start text
                fs.append(
                    startText, 
                    font=featureInfo["styleName"],
                    fontSize=sizeSample[0],
                    lineHeight=sizeSample[1],
                    tabs=[(sampleIndent, "left")],
                    openTypeFeatures=None) # Reset features
                # Turn on features
                features = {}
                if sample[sampleIdx][1]:
                    for feaTag in sample[sampleIdx][1]:
                        features[feaTag] = True
                # Set each character
                for c in sample[sampleIdx][0]:
                    if c == "_":
                        subOn = not subOn
                    else:
                        if subOn:
                            color = textHighlightColor
                        else: color = colorSampleDimmed
                        fs.append(
                            c, 
                            fill=color,
                            tabs=[(sampleIndent, "left")],
                            openTypeFeatures=features)
            # End text
            fs.append(
                "\n", 
                fontSize=sizeSample[0],
                lineHeight=sizeSample[1],
                tabs=[(sampleIndent, "left")],
                openTypeFeatures=None) # Reset features

    textBox(fs, (margin, margin, width()-(margin*2), height()-(margin*2)))


# Build all pages
for featureInfo in [featureInfoNeon, featureInfoPrism, featureInfoWarp]:
    drawPage(featureInfo)

# Save
saveImage("OpenType Feature Overview.pdf")
