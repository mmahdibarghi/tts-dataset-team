from shutil import copyfile
import io

# changing file
checkerFile = io.open("voiceName.txt", mode="r", encoding="utf-8")
checkerLine = checkerFile.readlines()
for i in range(len(checkerLine)):
    src="./clips/"+checkerLine[i][:-1]
    ds="./sounds/"+checkerLine[i][:-1]
    try:
        copyfile(src,ds)
    except:
        pass

