#
#   @author      : SRvSaha
#   Filename     : unigram_overlap_ratio.py
#   Timestamp    : 09:16 01-September-2016 (Thursday)
#   Description  :
#
#

import sys

filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    sentences1 = [line.split("\t")[1] for line in lines]
    sentences2 = [line.split("\t")[2] for line in lines]
    labels = [line.split("\t")[3] for line in lines]

def unigram_overlap_ratio(sentence1, sentence2):
    count = 0
    sent2 = sentence2.split(" ")
    for word in sentence1.split(" "):
        if word in sent2:
            count += 1
    total = len(set(sentence1.split(" ")) | set(sentence2.split(" ")))
    ratio = count / total
    return round(ratio,4)

f_out = open("unigram_overlap_ratio_output.txt", 'w')
if __name__ == '__main__':
    index = 0
    for text1,text2 in zip(sentences1,sentences2):
        result = str(unigram_overlap_ratio(text1, text2))
        # print(result)
        f_out.write(result+"\n")
        # ARFF Format Output
        # f_out.write(result+","+labels[index]+"\n")
        index += 1
    f_out.close()
    print("Operation Successful :)")
