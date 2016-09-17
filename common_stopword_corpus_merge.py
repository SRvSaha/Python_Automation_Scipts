#
#   @author      : SRvSaha
#   Filename     : stopword_corpus_merge.py
#   Timestamp    : 11:42 17-September-2016 (Saturday)
#   Description  : Merging the non-duplicate stop-words from Italian corpus || EVALITA 2016
#                   This script finds out the common words only.
#                   For exhaustive search it takes O(n^2) time
#
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

output = []
f_out = open("common_italian-stopwords.txt",'w')
with open(file1) as f:
    words1 = f.readlines()
with open(file2) as f:
    words2 = f.readlines()

def max(len1,len2):
    if len1 >= len2:
        max_ = len1
    else:
        max_ = len2
    return max_

if len(words1) == max(len(words1),len(words2)):
    for word in words1:
        if word in words2: # COMMON WORDS
            output.append(word)
else:
    for word in words2:
        if word in words1: # COMMON WORDS
            output.append(word)

f_out.writelines(output)
print("Operation Successful :)")
