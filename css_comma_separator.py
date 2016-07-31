#
#   @author      : SRvSaha
#   Filename     : css_comma_separator.py
#   Timestamp    : 14:25 31-July-2016 (Sunday)
#   Description  : Given a CSS file, this script gives the properly formatted comma
#   separated CSS file.
#   Requirement  : Python3
#

filename = input("Enter the CSS filename (eg. test.css) : ")
output = ""
try:
    with open(filename) as f:
        string_ = f.read()
    string_ = string_.strip().lstrip().rstrip()
    for string in string_.split("\n"):
        index_of_comma = []
        comma_final = []
        paranthesis = []
        stack = {}
        if ',' not in string:
            output += string + "\n"
        else:
            for i in range(len(string)):
                if string[i] == ',':
                    index_of_comma.append(i)
                elif string[i] == '(':
                    paranthesis.append(i)
                elif string[i] == ")":
                    stack[paranthesis.pop()] = i

        # This is important to see to the () is available or not
        if len(stack) != 0:
            last = sorted(stack.values())[-1]

        for comma in index_of_comma:
            comma_final.append(comma)

        for comma in index_of_comma:
            for key in sorted(stack.keys()):
                if comma < key or comma > last:
                    break
                if comma > key and comma < stack[key]:
                    comma_final.pop(comma_final.index(comma))
                    break

        for index in comma_final:
            if index == comma_final[0]:
                output += string[:index + 1] + "\n"
                prev = index
            elif index == comma_final[-1]:
                output += string[prev + 1:index+1] + "\n"
                output += string[index + 1:] + "\n"
            else:
                output += string[prev + 1:index+1] + "\n"
                prev = index
        filename_ = filename[:-4] + "_" + ".css"
    # Writing the output to the file
    with open(filename_, 'w') as f:
        f.write(output)
    print("Operation Successful :)")
# The exception is thrown when wrong filenames are given
except FileNotFoundError:
    print("Incorrect Filename !!!")
