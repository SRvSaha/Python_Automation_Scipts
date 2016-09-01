#
#   @author      : SRvSaha
#   Filename     : final_system_format.py
#   Timestamp    : 13:52 01-September-2016 (Thursday)
#   Description  :
#

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
file4 = sys.argv[4]

with open(file1) as f:
    result1 = f.readlines()
with open(file2) as f:
    result2 = f.readlines()
with open(file3) as f:
    result3 = f.readlines()
with open(file4) as f:
    result4 = f.readlines()


f_out = open("final_output_train.txt",'w')

for i in range(len(result1)):
    f_out.write(result1[i][:-1]+"\t"+result2[i][:-1]+"\t"+result3[i][:-1]+"\t"+result4[i][:-1]+"\n")
print("Output Successful :)")
