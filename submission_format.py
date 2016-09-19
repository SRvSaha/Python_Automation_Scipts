#
#   @author      : SRvSaha
#   Filename     : submission_format.py
#   Timestamp    : 16:00 18-September-2016 (Sunday)
#   Description  : FINAL submission format for EVALITA 2016
#
import sys

file = sys.argv[1]

f_out = open("RUN2-VERSION-3.txt", 'w')
with open(file) as f:
    lines = f.readlines()
output = []
for line in lines:
    splitted = line.split("\t")
    count = 1
    #print(splitted,len(splitted))
    if splitted[1] != "null\n":
        if(len(splitted)==2):
            if count <= 25:
                item = splitted[1]
                if '\n' not in item:
                    answer = splitted[0]+"\t"+item[-7:-4]+"\t"+str(count)+"\n"
                else:
                    answer = splitted[0]+"\t"+item[-8:-5]+"\t"+str(count)+"\n"
                output.append(answer)
            else:
                break
            count += 1
        else:
            for item in splitted[1:-1]:
                if count <= 25:
                    if '\n' not in item:
                        answer = splitted[0]+"\t"+item[-7:-4]+"\t"+str(count)+"\n"
                    else:
                        answer = splitted[0]+"\t"+item[-8:-5]+"\t"+str(count)+"\n"
                    output.append(answer)
                else:
                    break
                count += 1
f_out.writelines(output)
print("Operation Successful :)")
