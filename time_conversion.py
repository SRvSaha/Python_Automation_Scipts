############################################################################

#   @author      : Ipshita2207                                             #

#   Filename     : time_conversion.py      		                             #

#   Timestamp    : 05-Oct-2019 (Friday)                                    #

#   Description  : Given a time in 12-hour AM/PM format, convert it to     #
				           military (24-hour) time.  	 						                 #

############################################################################

 


	'''
	Input format: A single string s containing a time in 12-hour clock format (i.e.:hh:mm:ssAM or 
	hh:mm:ssPM), where 01 <=hh<=12, 00<=mm and ss<=59.
	
	Sample input : 07:05:45PM
	
	Output format: Convert and print the given time in 24-hour format, where 00<=hh<=23.
	
	Sample output : 19:05:45
	
	'''

	import sys
	from time import strptime, strftime
	print(strftime("%H:%M:%S", strptime(input(), "%I:%M:%S%p")))
