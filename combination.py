from itertools import combinations
 
input = ['verde','numero','aqp']
 
output = sum([map(list, combinations(input, i)) for i in range(1,len(input) + 1)], [])
 
output.sort(reverse = True,key=len)
print output
