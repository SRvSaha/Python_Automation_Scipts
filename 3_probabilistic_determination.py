#
#   @author      : SRvSaha
#   Filename     : 3_probabilistic_determination.py
#   Timestamp    : 14:50 03-September-2016 (Saturday)
#   Description  : TAG Validation of 3 possible cases : NP,P,SP using Probability
#
#
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
file4 = sys.argv[4]
file5 = sys.argv[5]

with open(file1) as f:
    lines1 = f.readlines()
with open(file2) as f:
    lines2 = f.readlines()
with open(file3) as f:
    lines3 = f.readlines()
with open(file4) as f:
    lines4 = f.readlines()
with open(file5) as f:
    lines5 = f.readlines()
f_out = open("./probabilistic_output.txt",'w')

# Change this part as per different languages
task2_hindi = {1:72.6857,2:78.2286,3:75.4571,4:78.2857,5:71.0286}

for i in range(len(lines1)):
    output_tag = ""
    list_tags = []
    combined_result = []
    P_index = []
    NP_index = []
    SP_index = []
    count_P = 0
    count_NP = 0
    count_SP = 0
    list_tags.append(lines1[i][:-1])
    list_tags.append(lines2[i][:-1])
    list_tags.append(lines3[i][:-1])
    list_tags.append(lines4[i][:-1])
    list_tags.append(lines5[i][:-1])
    for tag in list_tags:
        if tag == 'P':
            count_P += 1
        elif tag == 'NP':
            count_NP += 1
        else:
            count_SP += 1
    combined_result.append(count_P)
    combined_result.append(count_NP)
    combined_result.append(count_SP)
    combined_result.sort(reverse = True)
    if combined_result[0] != combined_result[1]:
        if combined_result[0] > combined_result[1]:
            if combined_result[0] == count_P:
                output_tag = "P\n"
            if combined_result[0] == count_SP:
                output_tag = "SP\n"
            if combined_result[0] == count_NP:
                output_tag = "NP\n"
        else:
            if combined_result[1] == count_P:
                output_tag = "P\n"
            if combined_result[1] == count_SP:
                output_tag = "SP\n"
            if combined_result[1] == count_NP:
                output_tag = "NP\n"
    else:
        #CHECKED
        if combined_result[2] == count_P:
            for k in range(len(list_tags)):
                if list_tags[k] == "NP":
                    NP_index.append(k+1)
                elif list_tags[k] == "SP":
                    SP_index.append(k+1)
            # If needed change this portion for weighted average
            sum_ = 0
            for index in NP_index:
                sum_ += (task2_hindi[index]) # make weighted avg here by multiplying weight with task2
            avg1 = (sum_ / 2) # replace 2 by sum of weights in case of weighte
            sum__ = 0
            for index in SP_index:
                sum__ += (task2_hindi[index])
            avg2 = (sum__ / 2)
            if avg1 >= avg2:
                output_tag = "NP\n"
            else:
                output_tag = "SP\n"
        if combined_result[2] == count_NP:
            for k in range(len(list_tags)):
                if list_tags[k] == "P":
                    P_index.append(k+1)
                elif list_tags[k] == "SP":
                    SP_index.append(k+1)
            # If needed change this portion for weighted average
            sum_ = 0
            for index in P_index:
                sum_ += (task2_hindi[index])
            avg1 = (sum_ / 2)
            sum__ = 0
            for index in SP_index:
                sum__ += (task2_hindi[index])
            avg2 = (sum__ / 2)
            if avg1 >= avg2:
                output_tag = "P\n"
            else:
                output_tag = "SP\n"
#CHECKED
        if combined_result[2] == count_SP:
            for k in range(len(list_tags)):
                if list_tags[k] == "P":
                    P_index.append(k+1)
                elif list_tags[k] == "NP":
                    NP_index.append(k+1)
            # If needed change this portion for weighted average
            sum_ = 0
            for index in P_index:
                sum_ += (task2_hindi[index])
            avg1 = (sum_ / 2)
            sum__ = 0
            for index in NP_index:
                sum__ += (task2_hindi[index])
            avg2 = (sum__ / 2)
            if avg1 >= avg2:
                output_tag = "P\n"
            else:
                output_tag = "NP\n"
    f_out.write(output_tag)
print("Operation Successful :)")
