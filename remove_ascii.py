#
#   @author      : SRvSaha
#   Filename     : remove_ascii.py
#   Timestamp    : 10:27 14-August-2016 (Sunday)
#   Description  : Remove all the ascii character encountered from Indian Languages
#   Requirement  : Python 3
#
output = ""
lines = []

with open("try.txt") as f:
    lines = f.readlines()


def remove_ascii(lines):
    global output  # Since we want to use the global output
    for line in lines:
        # Only when it's when it is in the range of Malayam Unicode and also
        # when space is there between words
        string = ''.join(i for i in line if ord(i) >= ord(
            '\u0D00') and ord(i) <= ord('\u0D7F') or ord(i) == 32)
        if len(string):
            output += string + '\n'
    with open("clean_output.txt", 'w') as f:
        f.write(output)
        print("Operation Successful :)")

if __name__ == "__main__":
    remove_ascii(lines)
