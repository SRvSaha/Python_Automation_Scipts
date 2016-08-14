#
#   @author      : SRvSaha
#   Filename     : corpus_clean.py
#   Timestamp    : 13:53 14-August-2016 (Sunday)
#   Description  : SCRIPT to remove all punctuations with "  " and removes all non-Malayalam stuffs
#   Requirement  : Python 3
#

import re

output = ""
lines = []
out = []

with open("TRY-1.txt") as f:
    lines = f.readlines()


def corpus_clean(lines):
    global output  # Since we want to use the global output
    for line in lines:
        string = ""
        # Only when it's when it is in the range of Malayalam Unicode and also
        # when space is there between words or the punctuations
        for i in line:
            if ord(i) >= 3328 and ord(i) <= 3455 or ord(i) >= 32 and ord(i) <= 47 or ord(i) >= 58 and ord(i) <= 63:
                if ord(i) >= 33 and ord(i) <= 47 or ord(i) >= 58 and ord(i) <= 63:
                    i = " " # Remove all punctuations with " "
                string += i
        string = re.sub('  +',' ',string) # Removing two or more spaces with single space
        if len(string) > 1: # Len = 1 when it's " "
            output += string + '\n'
    with open("clean_output.txt", 'w') as f:
        f.write(output)
        print("Operation Successful :)")

if __name__ == "__main__":
    corpus_clean(lines)
