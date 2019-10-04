############################################################################

#   @author      : Ipshita2207                                             #

#   Filename     : factorial_iterative.py                                  #

#   Timestamp    : 04-Oct-2019 (Friday)                                    #

#   Description  : Implementation of Factorial Iteratively			       #

############################################################################

 

 

def factorial_iter(n):

    '''

    Utility to get the factorial of any non negative number.

 

    The input parameter is the number for which the factorial is to be found.

    If the parameter is not a valid integer then it will give proper message

    as the exception is handled.
	

 

    Usage:

 

    Enter any number:

    6

    Factorial of 6 is: 720

    '''

    output = 1;

    if n == 0:

        return output;

    while (n > 0):

        output = output * n

        n = n - 1

    return output

 

 

# Driver Method for calling the utility

 

if __name__ == '__main__':

    print("Enter any number: ")

    try:

       n = int(input())

       print("Factorial of {} is: {}".format(n, factorial_iter(n)))

    except:

        print("Please enter a valid number")

 

 

############################################################################
#   @author      : Ipshita2207                                             #
#   Filename     : factorial_recursive.py                                  #
#   Timestamp    : 04-Oct-2019 (Friday)                                    #
#   Description  : Recursive Implementation of Factorial of a number       #
############################################################################
 
 
def factorial_recursive(n):
    '''
    Utility to get the factorial of any number.
 
    The input parameter is the number for which the factorial is to be found.
    If the parameter is not a valid integer then it will given proper message
    as the exception is handled.
 
    Usage:
 
    Enter any number: 
    5
    Factorial of 5 is: 120
    '''
    if n==0:
        return 1
    return n*factorial_recursive(n-1)
 
 
# Driver Method for calling the utility 
 
if __name__ == '__main__':
    print("Enter any number: ")
    try:
       n = int(input())
       print("Factorial of {} is: {}".format(n, factorial_recursive(n)))
    except:
        print("Please enter a valid number")
