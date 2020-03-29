

import sys

from fontTools.unicode import Unicode

string = sys.argv[1]
# string = "№ ™ ← ↑ → ↓ ↖ ↗ ↘ ↙ − ∕ ∙ ≈ ≠ ≤ ≥ ⟨ ⟩"

for char in string.split(" "):
	print(hex(ord(char)).replace("0x","U+"), end=",")
	# print(char.encode("unicode_escape"), end=",")