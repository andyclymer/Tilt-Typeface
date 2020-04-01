f = CurrentFont()

lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'germandbls', 'agrave', 'aacute', 'acircumflex', 'atilde', 'adieresis', 'aring', 'ae', 'ccedilla', 'egrave', 'eacute', 'ecircumflex', 'edieresis', 'igrave', 'iacute', 'icircumflex', 'idieresis', 'dotlessi', 'eth', 'ntilde', 'ograve', 'oacute', 'ocircumflex', 'otilde', 'odieresis', 'oslash', 'oe', 'ugrave', 'uacute', 'ucircumflex', 'udieresis', 'yacute', 'thorn', 'ydieresis']

# Collect UC group names
left = "ACEHOUXY"
right = "AHOUY"
ucGroups = []
for gn in left:
    ucGroups.append("public.kern1.%s" % gn)
for gn in right:
    ucGroups.append("public.kern2.%s" % gn)




oldKerns = {}
oldKerns.update(f.kerning)
newKerns = {}

def checkLC(item):
    if item in lc:
        return True
    if "public" in item:
        end = item.split(".")[-1]
        if end.lower() == end:
            if len(end) == 1:
                return True
    return False

def checkUC(item):
    if item[0].upper() == item[0]:
        return True
    if item in ucGroups:
        return True
    return False

# 1) Remove all LC kerning pairs
# ...any kern for a group that isn't in the font
# ...any kern for a glyph that's in "lc"
for pair, value in oldKerns.items():
    isLC = [checkLC(pair[0]), checkLC(pair[1])]
    if not True in isLC:
        # neither item are LC
        newKerns[pair] = value

        
# 2) Copy UC kerns to LC
# ...all groups match now between UC and LC
moreKerns = {}
for pair, value in newKerns.items():
    leftUC = checkUC(pair[0])
    rightUC = checkUC(pair[1])
    if leftUC and not rightUC:
        # lower to other
        newPair = [pair[0].lower(), pair[1]]
        moreKerns[tuple(newPair)] = value
    elif rightUC and not leftUC:
        # other to lower
        newPair = [pair[0], pair[1].lower()]
        moreKerns[tuple(newPair)] = value
    elif leftUC and rightUC:
        # lower to lower
        newPair = [pair[0].lower(), pair[1].lower()]
        moreKerns[tuple(newPair)] = value
        # uc to lower
        newPair = [pair[0], pair[1].lower()]
        moreKerns[tuple(newPair)] = value
        # lower to uc
        newPair = [pair[0].lower(), pair[1]]
        moreKerns[tuple(newPair)] = value
# Update
newKerns.update(moreKerns)

# Done

f.kerning.clear()
f.kerning.update(newKerns)