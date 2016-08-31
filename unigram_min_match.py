#
#   @author      : SRvSaha
#   Filename     : unigram.py
#   Timestamp    : 17:00 28-August-2016 (Sunday)
#   Description  : To find the Unigram Matches of 2 file and return the least match
#   Requirement  : Python3
#
import re
import sys

WORD = re.compile('\w+')

try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    if(len(sys.argv)<3):
        raise
except:
    print("Arguments Missing. Pass FILE1.txt FILE2.txt as parameters")
    sys.exit(1)
try:
    with open(file1) as f:
        lines_list_1 = f.readlines()
    with open(file2) as f:
        lines_list_2 = f.readlines()
except:
    print("Invalid filename !")
    sys.exit(1)

def unigram(text1, text2):
    match = 0
    text1 = WORD.findall(text1)
    text2 = WORD.findall(text2)
    for word in text1:
        if word in text2:
            match += 1
    return match

if __name__ == '__main__':
    f_out = open("./output_unigram.txt", 'w')
    for line in lines_list_1:
        min_match = []
        for _line_ in lines_list_2:
            min_match.append(unigram(line, _line_))
        index = min_match.index(min(min_match))
        # print(min_match,index)
        # print(lines_list_2[index])
        f_out.write(lines_list_2[index])
    f.close()
    print("Operation Successful :)")
