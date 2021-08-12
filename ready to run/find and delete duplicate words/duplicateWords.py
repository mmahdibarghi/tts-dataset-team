import io
checkerFile = io.open("must-change-words.txt", mode="r", encoding="utf-8")
checkerLine = checkerFile.readlines()
print(dict.fromkeys(checkerLine))
