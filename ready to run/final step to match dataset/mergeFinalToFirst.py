import io
first = io.open("5.txt", mode="r", encoding="utf-8")
start = first.readlines()
final = io.open("resualt/5-2.txt", mode="r", encoding="utf-8")
res = final.readlines()


sendingFile = io.open("resualt/5-send.txt", mode="a", encoding="utf-8")

for i in range(len(start)):
    temp = res[i].rstrip()+"\t"+start[i].rstrip()
    # print(temp)
    sendingFile.write(temp+"\n")
sendingFile.close()



