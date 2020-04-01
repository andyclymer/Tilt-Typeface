from glyphNameFormatter import GlyphName
import os

# Collect info on all GF glyphs, assign names, and reformat as CSV

baseNamPath = "./GF Glyph Sets"
# Nam file combining order: Core, Plus, Pro, Expert
namFileNames = [
    "GF-latin-core_unique-glyphs.nam",
    "GF-latin-plus_unique-glyphs.nam",
    "GF-latin-plus_optional-glyphs.nam",
    "GF-latin-pro_unique-glyphs.nam",
    "GF-latin-pro_optional-glyphs.nam",
    "GF-latin-expert_unique-glyphs.nam"]

allGlyphInfo = []
allNames = []

for fileName in namFileNames:
    pathSplit = fileName.split(".")[0].split("_")
    namCategory = pathSplit[0]
    optional = "optional" in fileName
    namFilePath = os.path.join(baseNamPath, fileName)
    with open(namFilePath, "r", encoding="utf-8") as namFile:
        lines = namFile.read()
        for line in lines.split("\n"):
            if len(line):
                if line.startswith(" "):
                    unistr = None
                    character = None
                    description = None
                    name = line.replace(" ", "")
                elif line.startswith("0x"):
                    lineSplit = line.split(" ")
                    unistr = lineSplit[0]
                    uni = int(unistr, 16)
                    character = lineSplit[1]
                    description = " ".join(lineSplit[2:])
                    gn = GlyphName(uni)
                    name = gn.getName()
                # Format the entry
                if not name in allNames:
                    if not name or not name.endswith(".sc"):
                        allGlyphInfo.append([name, unistr, character, description, namCategory, optional])
                        allNames.append(name)


# My custom sorting order for GF-latin-core
sortOrder = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z zero one two three four five six seven eight nine period comma colon semicolon periodcentered ellipsis exclam exclamdown question questiondown quotesingle quotedbl quoteleft quoteright quotesinglbase quotedblleft quotedblright quotedblbase guilsinglleft guilsinglright guillemetleft guillemetright parenleft parenright bracketleft bracketright braceleft braceright slash bar brokenbar backslash fraction divisionslash bullet hyphen hyphensoft endash emdash underscore plus minus multiply divide plusminus equal less greater logicalnot mu.math asterisk asciicircum asciitilde percent degree onesuperior twosuperior threesuperior four.superior onequarter onehalf threequarters ordmasculine ordfeminine copyright registered at numbersign dollar cent sterling yen Euro currency ampersand section paragraph dieresis grave macron acute cedilla circumflex ring tilde dieresis.cap grave.cap macron.cap acute.cap cedilla.cap circumflex.cap ring.cap tilde.cap Agrave Aacute Acircumflex Atilde Adieresis Aring AE Ccedilla Egrave Eacute Ecircumflex Edieresis Igrave Iacute Icircumflex Idieresis Eth Ntilde Ograve Oacute Ocircumflex Otilde Odieresis Oslash OE Ugrave Uacute Ucircumflex Udieresis Yacute Ydieresis Thorn germandbls agrave aacute acircumflex atilde adieresis aring ae ccedilla egrave eacute ecircumflex edieresis igrave iacute icircumflex idieresis dotlessi eth ntilde ograve oacute ocircumflex otilde odieresis oslash oe ugrave uacute ucircumflex udieresis yacute thorn ydieresis space nbspace NULL CR"
sortOrder = sortOrder.split(" ")

# Apply index values temporarly, for sorting
lastIdx = len(sortOrder) + 1
for g in allGlyphInfo:
    gn = g[0]
    if gn in sortOrder:
        i = sortOrder.index(gn)
    else:
        i = lastIdx + 1
        lastIdx = i
    g.append(i)

# Then, sort by this index
allGlyphInfo.sort(key = lambda g: g[6])
# ...and then remove my temporary glyph index
allGlyphInfo = [g[:-1] for g in allGlyphInfo]


# Reformat for CSV                 
for g in allGlyphInfo:
    # Convert None type to an empty string
    g = ["" if x == None else x for x in g]
    # Convert True/False to an int 0/1
    g = [0 if x == False else x for x in g]
    g = [1 if x == True else x for x in g]
    # Convert to string
    g = [str(x) for x in g]
    # Print comma separated
    print(",".join(g))
