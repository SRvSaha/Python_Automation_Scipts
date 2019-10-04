############################################################################

#   @author      : Ipshita2207                                             #

#   Filename     : diagonal_difference.py                                  #

#   Timestamp    : 04-Oct-2019 (Friday)                                    #

#   Description  : Given a square matrix, calculate the absolute 
                   difference between the sums of its diagonals 	       #

############################################################################

 
import sys

	'''
	Input format: 
	The first line contains a single integer n, which is the number of 
	rows and columns in arr. 
	Each of the next n lines describes a row, arr[i], and consists of n space-separated
	integers arr[i][j].
	
	Output format: 
	Print the absolute difference between the sums of the matrix's two 
	diagonals as a single integer 
	
	'''
n = int(input().strip()) 
sumLeft = 0
sumRight = 0

for i in range(n):
    matrixRow = input().split()
    sumLeft = sumLeft + int(matrixRow[i])
    sumRight = sumRight + int(matrixRow[-(i + 1)])
diff = abs(sumLeft-sumRight)
print(diff)
