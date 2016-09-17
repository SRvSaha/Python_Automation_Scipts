#
#   @author      : SRvSaha
#   Filename     : merging_stopwords.py
#   Timestamp    : 12:06 17-September-2016 (Saturday)
#   Description  : EVALITA 2016 || Script to combine only the unique stop-words from multiple stopword-files
#
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]

f_out = open("./final_stopwords_italian.txt",'w')
with open(file1) as f:
    words1 = f.readlines()
with open(file2) as f:
    words2 = f.readlines()
with open(file3) as f:
    common = f.readlines()

final = []

for word in words1:
    if word not in common:
        final.append(word)
for word in words2:
    if word not in common:
        final.append(word)
for word in common:
    final.append(word)
f_out.writelines(final)
print("Operation Successful :)")
