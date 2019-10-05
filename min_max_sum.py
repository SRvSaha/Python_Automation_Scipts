############################################################################

#   @author      : Ipshita2207                                             #

#   Filename     : min_max_sum.py         		                             #

#   Timestamp    : 05-Oct-2019 (Saturday)                                  #

#   Description  : Given five positive integers, the program finds the     #
				           minimum and maximum values  	 						               #

############################################################################

 


	'''
	Given five positive integers, the program finds the  minimum and maximum 
	values that can be calculated by summing exactly four of the five integers 
		
	For example, arr=[1,3,5,7,9]. Our minimum sum is 1+3+5+7=16 and our 
	maximum sum is 3+5+7+9=24 
	
	It would print
	
	16 24
	
	'''

	arr = list(map(int, input().strip().split(' ')))
	
	add=[None]*5
	total=sum(arr)
	
	for i in range(5):
	    add[i] = total - arr[i] 
		
	mini = min(add)
	maxi = max(add)
	
	print("%s %s  " % (mini, maxi))
  
  
  
  
