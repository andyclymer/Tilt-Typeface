f = CurrentFont()

byHeight = {}
byDepth = {}
for g in f:
    if g.bounds:
        h = g.bounds[3]
        b = g.bounds[1]
    
        if not h in byHeight:
            byHeight[h] = []
        byHeight[h].append(g.name)
    
        if not b in byDepth:
            byDepth[b] = []
        byDepth[b].append(g.name)



heights = list(byHeight.keys())
heights.sort()
heights.reverse()
depths = list(byDepth.keys())
depths.sort()

for h in heights[0:5]:
    print(h, byHeight[h])

for d in depths[0:5]:
    print(d, byDepth[d])
    
    
glyphNames = ["Aring", "Oacute", "parenleft", "Ccedilla", "ccedilla"]
    
"""

Warp
981.0 ['Aring', 'ring.cap']
951.0 ['Ograve', 'Oacute', 'Ocircumflex']
950.0 ['Odieresis']
949.0 ['Otilde']
943.0 ['Igrave', 'Aacute', 'Eacute', 'Agrave', 'circumflex.cap', 'Acircumflex', 'Iacute', 'Yacute', 'acute.cap', 'Ucircumflex', 'grave.cap', 'Uacute', 'Ecircumflex', 'Icircumflex', 'Egrave', 'Ugrave']
-266.3014695034956 ['Ccedilla']
-265.36774414431346 ['ccedilla']
-254.32710379679642 ['cedilla']
-191.0 ['parenleft']
-190 ['parenright']

Neon
982.0 ['Aring']
972.0 ['ring.cap']
958.0 ['Ocircumflex', 'Otilde']
957.6818747594463 ['Ograve', 'Oacute']
953.0 ['Acircumflex', 'Atilde', 'Ucircumflex', 'Ntilde', 'Icircumflex']
-259.84281890561874 ['ccedilla']
-257.57062214630423 ['Ccedilla']
-244.3007809097565 ['cedilla']
-185.91514531404698 ['parenleft']
-184.64687452032996 ['parenright']

Monument
981 ['Aring']
958 ['Ocircumflex']
953.0 ['Ograve', 'Oacute']
951 ['Otilde']
948 ['Acircumflex', 'Ucircumflex', 'Ecircumflex', 'Icircumflex']
-263.23632415566806 ['Ccedilla']
-251.2363241556681 ['cedilla']
-160.0 ['mu.math']
-153.0 ['parenleft']
-152 ['parenright']
!!! Add 10u on the Monument to account for the stroke
= 991 -273

"""