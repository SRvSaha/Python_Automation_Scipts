#
#   @author      : SRvSaha
#   Filename     : append_tab_separated.py
#   Timestamp    : 08:03 03-September-2016 (Saturday)
#   Description  : Takes two files and outputs <line_file1>\t<line_file2>
#
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as f1:
    lines1 = f1.readlines()
with open(file2) as f2:
    lines2 = f2.readlines()

f_out = open("append_tab_separated_output.txt",'w')
for line in zip(lines1,lines2):
        f_out.write(line[0][:-1]+"\t"+line[1])
    # print(line[0][:-1]+"\t"+line[1])
print("Operation Successful :)")

