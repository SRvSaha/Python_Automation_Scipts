#
#   @author      : SRvSaha
#   Filename     : data_extract.py
#   Timestamp    : 15:57 16-September-2016 (Friday)
#   Description  : Data Extraction for EVALITA Question Answering FAQ
#
import re
import sys

filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
for line in lines[1:]:
    file = line[:3]+".txt"
    output = line[4:]
    with open(file,'w') as f:
        f.write(output)
print("Operation Successful :)")
