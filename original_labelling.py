#
#   @author      : SRvSaha
#   Filename     : original_labelling.py
#   Timestamp    : 01:13 01-September-2016 (Thursday)
#   Description  : To label the results with Original Tags from Train Data
#

import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

labels = []
lavenshtein_ratios = []
with open(filename1) as f:
    for line in f.readlines():
        label = line.split("\t")[3]
        labels.append(label)

with open(filename2) as f:
    for ratio in f.readlines():
        lavenshtein_ratios.append(ratio)

f_out = open("lavenshtein_original_labelling.txt",'w')

def original_labelling():
    for i in range(len(lavenshtein_ratios)):
        f_out.write(labels[i]+"\t"+ lavenshtein_ratios[i])

if __name__ == '__main__':
    original_labelling()
    f_out.close()
    print("Operation Successful :)")

