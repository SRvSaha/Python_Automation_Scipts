from itertools import permutations
 
input = ['verde','numero','aqp']
 
output = sum([map(list, permutations(input, i)) for i in range(1,len(input) + 1)], [])
 
print sorted(output,key=len,reverse=True)
