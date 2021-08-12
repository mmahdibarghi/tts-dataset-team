def f2f (str):
    finglish = {
        "ا" : "a",
        "آ" : "a",
        "أ" : "a",
        "ب" : "b",
        "پ" : "p",
        "ت" : "t",
        "ث" : "s",
        "ج" : "j",
        "چ" : "ch",
        "ح" : "h",
        "خ" : "kh",
        "د" : "d",
        "ذ" : "z",
        "ر" : "r",
        "ز" : "z",
        "ژ" : "zh",
        "س" : "s",
        "ش" : "sh",
        "ص" : "s",
        "ض" : "z",
        "ط" : "t",
        "ظ" : "z",
        "ع" : "a",
        "غ" : "gh",
        "ف" : "f",
        "ق" : "gh",
        "ک" : "k",
        "ك" : "k",
        "گ" : "g",
        "ل" : "l",
        "م" : "m",
        "ن" : "n",
        "و" : "o",
        "ؤ" : "o",
        "ه" : "h",
        "ی" : "i",
        "ى" : "i",
        " " : " ",
        "." : ".",
        "!" : "!",
        "؟" : "؟",
        "،" : "،",
        "A" : "A",
        ":" : ":",
        "%" : "%",
        "/" : "/",
        ")" : ")",
        "(" : "(",
        "»" : "»",
        "«" : "«",
        "\"" : "\"",
        "-" : "-",
        "#" : "#",
        "_" : "_",
        "1" : "1",
        "0" : "0",
        "2" : "2",
        "3" : "3",
        "4" : "4",
        "5" : "5",
        "6" : "6",
        "7" : "7",
        "8" : "8",
        "9" : "9",
        "۳": "3",
        "۱": "1",
        "۸": "8",
        "٣": "3",
        "ئ" : "a",
        "ء" : "a",
        "ً" : "a",
        "۴" : "4",
        "۹" : "9",
        "۵" : "5",
        "۷" : "7",
        "۲" : "2",
        "۰" : "0",
        "٠" : "0",
        "ـ" : "ـ",
        "," : ",",
        "ُ" : "a",
        "ِ" : "e",
        "ٔ" : "o",
        "D" : "di",
        "Q" : "Q",
        "F" : "F",
        "B" : "B",
        "I" : "I",
        "S" : "S",
        "T" : "T",
        "E" : "E",
        "M" : "M",


    }
    ans=""
    for i in str:
        ans=ans+finglish[i]
    return ans

import io
checkerFile = io.open("letsChange.txt", mode="r", encoding="utf-8")
checkerLine = checkerFile.readlines()
# farsi dataset file
persianFile = io.open("farsi-Words-DATASET.txt", mode="r", encoding="utf-8")
persianWord = persianFile.readlines()

englishFile = io.open("english-Words-DATASET.txt", mode="r", encoding="utf-8")
englishWord = englishFile.readlines()
# print(checkerLine)
for i in range(len(checkerLine)):
    # print(checkerLine[i])
    res = []
    checkertemp = checkerLine[i].split()
    # print(checkertemp)
    for checker in checkertemp:
        # print(checker)
        # print(res)
        flag = False
        couter=0
        for perWord in persianWord:
            # print(perWord.split())
            couter = couter + 1;
            if(perWord.split()==checker.split()):
              # print(perWord)
              # print(englishWord[couter-1])
              wait=englishWord[couter-1].rstrip()
              res.append(wait)
              flag=True
              break

        if (flag == False):
            print(checker)
            res.append(checker)
    # print("seeeeen")
    # print(res)
    res = ' '.join(res)
    # print(res)










     # print(f2f(Lines[i].strip()))
     # print(i)





# file1 = io.open("PersianToFinglishDataset.txt", mode="r", encoding="utf-8")
# Lines = file1.readlines()
# f = io.open("farsiDataset.txt", mode="a", encoding="utf-8")
#
# for i in range(len(Lines)):
#     temp = Lines[i].split("\t")
#     f.write(temp[1])
#     # f.write("\n")
# f.close()



