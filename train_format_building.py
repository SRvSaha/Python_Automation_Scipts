#
#   @author      : SRvSaha
#   Filename     : train_format_building.py
#   Timestamp    : 15:38 24-September-2016 (Saturday)
#   Description  :
#
import sys

file = sys.argv[1]
file = sys.argv[2]

with open(file1) as f:
    annotated = f.readlines()
with open(file2) as f:
    raw = f.readlines()

for line in raw:
    splitted_line = line.split("\t")
    tag = splitted_line[0]

