#
#   @author      : SRvSaha
#   Filename     : css_refactoring.py
#   Timestamp    : 19:59 30-July-2016 (Saturday)
#   Description  : A program to re-factor a Cascading Style Sheet (CSS) file.
#   This script takes a CSS file as an input and change a CSS file to its correct
#   format.
#   NOTE : The name of the file must be correct (exactly as it is !).
#   Requirement  : Python3
#

output = ""
filename_ = ""
output_final = ""
filename = input("Enter the CSS filename (eg. test.css) : ")
try:
    with open(filename, 'r') as f:
        # Reading till the end of the file
        css_code = f.read(-1).strip()
    output = (((css_code.replace(';', ';\n')).replace(
        '{', '\n{\n')).replace('}', '\n}\n'))
    # Removes all the leading and trailing whitespaces
    string_ = output.strip().lstrip().rstrip()
    for string in string_.split("\n"):
        index_of_comma = []  # Keeps the index of all commas encountered
        comma_final = []  # The index of commas which are outside parantheses
        paranthesis = []  # Keep the index of opening parantheses
        # Dictionary to keep track of opening and closing index of ()
        stack = {}
        # For those lines which are already ok and doesn't contain ','
        if ',' not in string:
            output_final += string + "\n"
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
                    # When comma is outside the parenthesis
                    break
                if comma > key and comma < stack[key]:
                    # When comma is inside the parenthesis
                    comma_final.pop(comma_final.index(comma))
                    break
        # For outputing in the required format : FORMATTING
        for index in comma_final:
            if index == comma_final[0]:
                output_final += string[:index + 1] + "\n"
                prev = index
            elif index == comma_final[-1]:
                output_final += string[prev + 1:index+1] + "\n"
                output_final += string[index + 1:] + "\n"
            else:
                output_final += string[prev + 1:index+1] + "\n"
                prev = index

    # Naming the output file
    filename_ = filename[:-4] + "_" + ".css"
    # Writing the output to the file
    with open(filename_, 'w') as f:
        f.write(output_final)
    print("Operation Successful :)")
# The exception is thrown when wrong filenames are given
except FileNotFoundError:
    print("Incorrect Filename !!!")

