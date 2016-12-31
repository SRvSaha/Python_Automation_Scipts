'''
Script to find the longest common substring between 2 sentences.

Requirements : Python 3
To Run : python3 longest_common_substring.py <INPUT.txt>
INPUT.txt => File containing tab separated 2 sentences
OUTPUT => "out".txt containing only the longest common substring
'''

import sys

if len(sys.argv) == 2:
    def long_substr(data):
        substr = ''
        if len(data) > 1 and len(data[0]) > 0:
            for i in range(len(data[0])):
                for j in range(len(data[0]) - i + 1):
                    if j > len(substr) and is_substr(data[0][i:i + j], data):
                        substr = data[0][i:i + j]
        return substr

    def is_substr(find, data):
        if len(data) < 1 and len(find) < 1:
            return False
        for i in range(len(data)):
            if find not in data[i]:
                return False
        return True

    with open("out.txt", 'w') as f_out:
        with open(sys.argv[1]) as f_in:
            for sentence in f_in:
                sentences = sentence.split("\t")
                f_out.write(long_substr(sentences) + "\n")
    print("Output Successful :)")
else:
    print("Argument(s) missing. Please run the code as \n\
python3 longest_common_substring.py <INPUT.txt>")
##############
###Testing###
#############
# print(long_substr(["जानकारी के मुताबिक जंगलों में पन्द्रह् फरवरी से फायर सीजन शुरू होता है।", "आमतौर पर यहां के जंगलों में 'फायर सीजन' पन्द्रह  फरवरी से शुरू होता है"]))
