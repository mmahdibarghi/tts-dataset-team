import io
file1 = file1 = io.open("allpersian.txt", mode="r", encoding="utf-8")
Lines = file1.readlines()
fileEnglish = io.open("allenglish.txt", mode="r", encoding="utf-8")
englishlines = fileEnglish.readlines()
for i in range(927):
    print(englishlines[i].strip(),"\t",Lines[i].strip())
