"""
	Goes through UFOs in a directory and checks the segment types of a specific glyph for compatibility.

	If points are in the wrong order or segment types mismatch, this will help you find which master the problem exists in.

	Originally created by @ArrowType for the Recursive project.

	USAGE EXAMPLE:

	python sources/mastering-scripts/check-segments-selected-masters.py "sources/Tilt Neon/Rotated" "Aogonek"

	TODO(?): make prettier tables by saving data to dict, then printing proper columns
"""

import sys
import os
from fontParts.world import *

try:
	if sys.argv[1]:
		print("Getting UFO paths")
		dirToCheck = sys.argv[1]
		subDirs = next(os.walk(dirToCheck))[1]
		ufosToCheck = [ path for path in subDirs if path.endswith(".ufo")]
		head = dirToCheck
	if sys.argv[2]:
		glyphsToCheck = sys.argv[2].split(" ")

		print(glyphsToCheck)

except IndexError:
	print("Please include args: <glyphName> and <directory containing UFOs>")

print(ufosToCheck)

firstColWidth = 30

print("")
print("")
key = "🥐 = curve | 📏 = line | 🚚 = move | 🥨 = qcurve"
print(f"Segment types: {key}")

print("")

for glyphName in glyphsToCheck:
	print("FONT".ljust(firstColWidth + 1), end=" ")
	print("|", end=" ")
	print(f"/{glyphName}: contours & segments")
	print("".ljust(firstColWidth + 1, "-") + " | " + "".ljust(96, "-"))
	for ufo in sorted(ufosToCheck):
		ufoPath = f"{head}/{ufo}"
		# print(ufoPath)

		f = OpenFont(ufoPath, showInterface=False)

		print(ufoPath.split("/")[-1].ljust(firstColWidth + 1), end=" ")
		print("|", end=" ")
		for i, c in enumerate(f[glyphName]):
			print(f"C{str(i).rjust(2, '0')}", end=" ")
			print(f"[segs {str(len(c.segments)).rjust(2, '0')}]", end=" ")
			for s in c:
				if s.type == "line":
					print("📏", end=" ")
				elif s.type == "curve":
					print("🥐", end=" ")
				elif s.type == "move":
					print("🚚", end=" ")
				elif s.type == "qcurve":
					print("🥨", end=" ")
			print(" |", end=" ")
		print("")
			
		f.close()
	
	print("")
	print("")

print("")
print("")
print("")