#
#   @author      : SRvSaha
#   Filename     : file_separation.py
#   Timestamp    : 23:04 31-August-2016 (Wednesday)
#   Description  : Script to Extract Sentences from Train Data into 2 different files
#

import sys

filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()
f1 = open("malayalam_train_sentence1.txt",'w')
f2 = open("malayalam_train_sentence2.txt",'w')

def file_separation():
    for line in lines:
        sent1 = line.split("\t")[1]
        sent2 = line.split("\t")[2]
        f1.write(sent1+"\n")
        f2.write(sent2+"\n")

if __name__ == '__main__':
    file_separation()
    f1.close()
    f2.close()
    print("Operation Successful :)")
