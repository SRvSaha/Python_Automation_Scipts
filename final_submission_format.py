#
#   @author      : SRvSaha
#   Filename     : final_submission_format.py
#   Timestamp    : 07:46 03-September-2016 (Saturday)
#   Description  : Script to make a XML type format using Python for submission
#
import sys

filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

output = "<Team NAME=\"NITMZ\" Language=Malayalam Task=Task1>\n\n"

for line in lines:
    splitted = line.split("\t")
    output += "<Paraphrase pID=\"" + splitted[0] + "\">\n"  "<Class> "+splitted[1][:-1] + " </Class>\n"+"</Paraphrase>\n\n"
output += "</Team>\n"

with open("final_submission_output.txt",'w') as f:
    f.write(output)
print("Operation Successful :)")
