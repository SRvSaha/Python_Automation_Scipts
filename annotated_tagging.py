#
#   @author      : SRvSaha
#   Filename     : annotated_tagging.py
#   Timestamp    : 14:59 24-September-2016 (Saturday)
#   Description  :
#
import sys

file = sys.argv[1]

with open(file) as f:
    lines = f.readlines()

output = []
for line in lines:
    splitted_line = line.split("\t")
    tag = (splitted_line[2])[6:]
    entities = ((splitted_line[3])[3:].lstrip().rstrip()).split(" ")
    if(len(entities) == 1):
        output.append(entities[0]+" B-"+tag+"\n")
    else:
        output.append(entities[0]+" B-"+tag+"\n")
        for entity in entities[1:]:
            output.append(entity+" I-"+tag+"\n")
    output.append("\n")
with open("output.txt",'w') as f:
    f.writelines(output)
print("Operation Successful :)")
