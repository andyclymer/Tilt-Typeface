csvPath = "sortedCharset.csv"

csvFile = open(csvPath, "r", encoding="utf-8")
csvText = csvFile.read()
csvFile.close()

names = []
for line in csvText.split("\n")[1:]:
    if '","' in line: # hack
        line = line.replace('","', "")
    glyphName, uni, character, description, charset, optional, exclude = line.split(",")
    if exclude == "FALSE":
        names.append(glyphName)
    
print(" ".join(names))