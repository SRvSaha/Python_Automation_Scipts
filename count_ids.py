#
#   @author      : SRvSaha
#   Filename     : evalita_id_extraction.py
#   Timestamp    : 10:11 19-September-2016 (Monday)
#   Description  : To count the number of distinct ID
#
import sys
import collections

file = sys.argv[1]

#f_out = open("original_id_final.txt",'w')
with open(file) as f:
    lines = f.readlines()
output = []

for line in lines:
    id_ = line.split("\t")[0]
    output.append(id_+"\n")
#f_out.writelines(set(output))
print(len(set(output)))
