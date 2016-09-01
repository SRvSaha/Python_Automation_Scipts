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

with open(file1) as f:
    result1 = f.readlines()
with open(file2) as f:
    result2 = f.readlines()
with open(file3) as f:
    result3 = f.readlines()


f_out = open("arff_output.arff",'w')

for i in range(len(result1)):
    # f_out.write(result1[i][:-1]+"\t"+result2[i][:-1]+"\t"+result3[i][:-1]+"\t"+"P"+"\n")
    # ARFF format
    f_out.write(result1[i][:-1]+","+result2[i][:-1]+","+ result3[i][:5]+","+"NP"+"\n")
print("Output Successful :)")
