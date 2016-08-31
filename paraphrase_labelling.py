#
#   @author      : SRvSaha
#   Filename     : paraphrase_labelling.py
#   Timestamp    : 23:03 31-August-2016 (Wednesday)
#   Description  : Automatically Labelling P/NP in Test Data based on F-Measure of
#   Train Data
#

import sys

filename = sys.argv[1]
labels = []
values = []
with open(filename) as f:
    lines = f.readlines()

filename = "paraphrase_labelled_output.txt"
f_out = open(filename,'w')

def labelling():
    for line in lines:
        value = (line.split("\t")[1]).rstrip("\n")
        if(float(value) >= 0.61):
            labels.append("P")
        else:
            labels.append("NP")

def outputting():
    for line in lines:
        value = (line.split("\t")[1]).rstrip("\n")
        values.append(value)
    for i in range(len(values)):
        output = ""
        output = labels[i]+"\t"+values[i]+"\n"
        f_out.write(output)
if __name__ == '__main__':
    labelling()
    outputting()
f_out.close()
print("Operation Successful :)")
