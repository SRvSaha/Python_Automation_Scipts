#
#   @author      : SRvSaha
#   Filename     : system_threshold.py
#   Timestamp    : 10:37 21-August-2016 (Sunday)
#   Description  : System takes in input precisions and decide P and NP using
#                   Precision, Recall and F-measure
#   Requirement  : Python3
#

import sys
import re

# The second arg passed from the command line is the filename else it'll
# raise exception
try:
    filename = sys.argv[1]
    arg = len(sys.argv)
    if(arg < 2):
        raise
# When the number of arguments passed is less that what should be passed
except:
    print(
        "Filename argument missing.\nPass the filename as second argument eg. python3 code.py <filename>")
    # Exits with status 0
    sys.exit(0)

try:
    f = open(filename)
# IOError exception is thrown when the file with the given filename
# doesn't exist
except IOError:
    print("Can't open file. Please provide correct filename")
    sys.exit(0)

input_ = f.readlines()
f.close()

# GS_P is the global variable which holds the number of P in original DataSet
GS_P = 0
# Common_P is the global variable which holds the number of P in original
# DataSet
Common_P = 0


def count_GS_P():
    """To count the number of Gold Standard P in the original train DataSet

    GS_P is the global variable which holds the number of P in original DataSet
    """
    global GS_P
    for line in input_:
        if(line.startswith('P')):
            GS_P += 1
    return GS_P


def system_precision(precision_value):
    """
    Calculates the Precision of the system.

    precision_value : Parameter that is the factor to determine P in our system. Above this precision_value, how many values will be there, are P for my system.

    Given the similarity measure between two sentences using cosine similarity,
    the system calculates the precision of the system using the formula -

    P = (GoldStandard(GS) P)intersection(MySystem's P) / Total P by MySystem

    """

    # MS_P is MySystem_P i.e, the count of P according the my system based on
    # precision value
    # Common_P is the Number of P common in MySystem and GoldStandard
    MS_P = 0
    global Common_P
    for line in input_:
        # Since the values are tab separated, we need to split them by '\t'
        values = line.split("\t")
        # Since the value is in string format so must be typecaseted to float
        temp = float(values[1].rstrip('\n'))
        if(values[0] == 'P' and temp >= precision_value):
            Common_P += 1
        if (temp >= precision_value):
            MS_P += 1
    PRECISION = float(Common_P)*100 / MS_P
    # Rounding is used to get precision upto 2 digits
    return round(PRECISION, 2)


def system_recall(precision_value):
    """[summary]

    Calculates the recall value of the system

    [description]

    Given the similarity measure between two sentences using cosine similarity,
    the system calculates the precision of the system using the formula -

    P = (GoldStandard(GS) P)intersection(MySystem's P) / Total GoldStandard P

    Arguments:

        precision_value  -- Parameter that is the factor to determine P in our system. Above this precision_value, how many values will be there, are P for my system.
    """
    RECALL = float(Common_P)*100 / count_GS_P()
    # Rounding is used to get precision upto 2 digits
    return round(RECALL, 2)


def system_f_measure(precision_value):
    """[summary]

    F-measure is approximately the average of the two when they are close, and is more generally the harmonic mean which for the case of two numbers coincides with the square of the geometric mean divided by the arithmetic mean.

    precision_value is the parameter for which we find the precision and recall and find the weighted average of them

    [description]

    F-measure is a measure of a test's accuracy. It considers both the precision p and the recall r of the test to compute the score.
    The F-score can be interpreted as a weighted average of the precision and recall.

    F-Score = 2*(P*R)/(P+R)

    """
    F_SCORE = 2 * (system_precision(precision_value) * system_recall(precision_value)) / \
        (system_precision(precision_value) + system_recall(precision_value))

    return round(F_SCORE, 4)

if __name__ == '__main__':
    precision_val = float(input("Please enter the precision value : "))
    print('Precision : ', system_precision(precision_val))
    print('Recall : ', system_recall(precision_val))
    print('F_SCORE : ', system_f_measure(precision_val))
