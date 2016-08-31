#
#   @author      : SRvSaha
#   Filename     : cosine_similarity.py
#   Timestamp    : 01:38 01-September-2016 (Thursday)
#   Description  : Cosine similarity of 2 strings for train data || cross-lingual
#
import re, math
import sys
from collections import Counter
filename = sys.argv[1]
with open(filename) as f:
	lines=f.readlines()

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])
     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

filename = filename[:-4] + '_similarity.txt'
f_out = open(filename,'w')
for line in lines:
	cosine = 0
	splitted = line.split("\t")
	text1 = splitted[1]
	text2 = splitted[2]
	vector1 = text_to_vector(text1)
	vector2 = text_to_vector(text2)
	cosine = get_cosine(vector1, vector2)
	f_out.write(splitted[3]+"\t"+str(round(cosine,2)) + "\n")
f_out.close()
print("Operation Successful :)")









