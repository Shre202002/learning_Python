#Loops In Python 

# For Loop 
'''
SYNTEX:  For i  in range (starting , ending):

for :- keyword 
i :- Value for which we have to print the data  WHICH COUNTS THE VALUES OR JIS ME NUMBERS CHALTE HAI 
in :- Keyword 
range :- Function Which takes in put values and print the data
'''
i = [1,2,3,4,15]
for a in range (len(i)):
    print(i[a])


#While Loops 

'''
SYNTEX:  while( condition):
           statement
           incriment of condition variable

'''
a=0
while(a<len(i)):
    print(i[a])
    a+=1