'''
The script is used to find the Longest Common Sub-sequence in two sentences.

Requirements : Python 3
To Run : python4 Longest_common_subseq.py <INPUT.txt>
INPUT.txt => File containing tab separated sentences.

OUTPUT => "out.txt" consists of only the matching Sub-sequence.

'''


import sys

sentences = []

if len(sys.argv) == 2:
    def lcs(X, Y, m, n):
        L = [[0 for x in range(n + 1)] for x in range(m + 1)]

        # Following steps build L[m+1][n+1] in bottom up fashion. Note
        # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])

        # Following code is used to print LCS
        index = L[m][n]

        # Create a character array to store the lcs string
        lcs = [""] * (index + 1)
        # Since the ending should be with newline
        lcs[index] = "\n"

        # Start from the right-most-bottom-most corner and
        # one by one store characters in lcs[]
        i = m
        j = n
        while i > 0 and j > 0:

            # If current character in X[] and Y are same, then
            # current character is part of LCS
            if X[i - 1] == Y[j - 1]:
                lcs[index - 1] = X[i - 1]
                i -= 1
                j -= 1
                index -= 1

            # If not same, then find the larger of two and
            # go in the direction of larger value
            elif L[i - 1][j] > L[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return ("".join(lcs))
    with open('out.txt', 'w') as ff:
        with open(sys.argv[1]) as f:
            for sentence in f:
                sentences = sentence.split('\t')
                ff.write(lcs(sentences[0], sentences[1],
                             len(sentences[0]), len(sentences[1])))
    print("Output Successful :)")
else:
    print("Argument(s) missing. Please run the code as \n\
python3 longest_common_subseq.py <INPUT.txt>")
########################
#        TESTING       #
########################
# sentences = ['जानकारी के मुताबिक जंगलों में पन्द्रह् फरवरी से फायर सीजन  शुरूहोता है।',
#              "आमतौर पर यहां के जंगलों में 'फायर सीजन' पन्द्रह  फरवरी से शुरू होता है।"]
# print(lcs(sentences[0], sentences[1],\ len(sentences[0]), len(sentences[1])))
