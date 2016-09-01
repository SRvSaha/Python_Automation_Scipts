#
#   @author      : SRvSaha
#   Filename     : GS_tags_extraction.py
#   Timestamp    : 14:17 01-September-2016 (Thursday)
#   Description  :
#
import sys

filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

f_out = open("tags_output.txt",'w')
for line in lines:
    tag = line.split("\t")[0]
    f_out.write(tag+"\n")
f_out.close()
print("Output Successful :)")
