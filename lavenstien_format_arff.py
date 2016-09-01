#
#   @author      : SRvSaha
#   Filename     : lavenstien_format_arff.py
#   Timestamp    : 11:47 01-September-2016 (Thursday)
#   Description  :
#

import sys

filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

f_out = open("lavenshtein_arff_format_output.txt",'w')
def lavenshtein_formatting():
    for line in lines:
        splitted = line.split("\t")
        tag = splitted[0]
        distance = splitted[1]
        f_out.write(distance[:-1]+","+tag+"\n")

if __name__ == '__main__':
    lavenshtein_formatting()
    f_out.close()
    print("Operation Successful :)")
