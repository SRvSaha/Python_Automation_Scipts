#
#   @author      : SRvSaha
#   Filename     : query_combination_expansion.py
#   Timestamp    : 13:33 18-September-2016 (Sunday)
#   Description  : Combinations of all possible cases of queries for Nutch || EVALITA 2016
#
import sys
from itertools import combinations


def word_combination(words):
    output = sum([map(list, combinations(words, i))
                  for i in range(1, len(words) + 1)], [])
    output.sort(reverse=True, key=len)
    return output

file_query = sys.argv[1]

with open(file_query) as f:
    queries = []
    for query in f.readlines():
        if '\n' in query:
            query = query.strip('\n')
        queries.append(query)
output = []
for query in queries:
    file = query.split("\t")[0]
    splitted = query.split("\t")[1].split(" ")
    if len(splitted) <= 5 :
        for item in word_combination(splitted):
            output.append(file+"\t"+" ".join(item)+"\n")
    else:
        output.append(query)
with open("expanded_queries.txt",'w') as f:
    f.writelines(output)

print "Operation Successful :)"

