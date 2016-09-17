#
#   @author      : SRvSaha
#   Filename     : query_stopword_remove.py
#   Timestamp    : 13:31 17-September-2016 (Saturday)
#   Description  : Removing the stopwords from the EVALITA 2016 test data
#
import sys

file_query = sys.argv[1]
file_stopwords = sys.argv[2]

f_out = open("queries_without_stopword.txt",'w')
stopwords = []
with open(file_query) as f:
    queries = f.readlines()
with open(file_stopwords) as f:
    for word in f.readlines():
        stopwords.append(word[:-1])

for query in queries:
    words = (query.split("\t")[1]).split(" ")
    words[-1].strip("\n\n")
    output = query.split("\t")[0]+"\t"
    for word in words:
        if '\n' not in word:
            if word not in stopwords:
                output += word + " "
        else:
            output += word
    f_out.write(output)
f_out.close()
print("Operation Successful :)")
