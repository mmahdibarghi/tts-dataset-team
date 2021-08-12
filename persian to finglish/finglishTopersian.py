from finglish import f2p
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
        "\n" : "",


    }
    ans=""
    for i in str:
        ans=ans+finglish[i]
    return ans

import io
import time
checkerFile = io.open("1englishWords.txt", mode="r", encoding="utf-8")
checkerLine = checkerFile.readlines()
# counter=0;
for sen in checkerLine:
    tmp=sen.split()
    # counter=counter+1
    # print(sen)
    for wrd in tmp:
        print(f2p(wrd))
        # if(wrd!=""):
        #     print(wrd)



        # time.sleep(0.1)








