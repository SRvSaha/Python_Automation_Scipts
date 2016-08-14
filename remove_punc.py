#
#   @author      : SRvSaha
#   Filename     : remove_punc.py
#   Timestamp    : 13:51 14-August-2016 (Sunday)
#   Description  : To remove all the punctuations in Malyalam with "  "
#
with open("try.txt") as f:
    lines = f.readlines()
for line in lines:
    string = ""
    for i in line:
        if ord(i) >= 33 and ord(i) <= 47 or ord(i) >= 58 and ord(i) <= 63:
            i = " "
        string += i
    print(string,end = "")
