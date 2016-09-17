#
#   @author      : SRvSaha
#   Filename     : evalita_id_extraction.py
#   Timestamp    : 21:04 17-September-2016 (Saturday)
#   Description  : To extract the IDs of the Training data
#
import sys

file = sys.argv[1]
f_out = open("evalita_ids.txt", 'w')
with open(file) as f:
    lines = f.readlines()
for line in lines[1:]:
    id = line.split(";")[0]
    f_out.write(id+"\n")
f_out.close()
print("Operation Successful :)")
