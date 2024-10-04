#Loops In Python 

# For Loop 
'''
SYNTEX:  For i  in range (starting , ending, steps):

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
    
    
 # WAP To Print first 15 natural Number 
a =1
while(a <= 15):
    print(a)
    a+=1

p=1
n = int(input("Enter Number to find table: "))
while (p <=10):
    print(f"{n} X {p} = {n*p}")
    p+=1

# Factorial OF Number 
x = 1
fact = 1
b = int(input("Enter Number For Factorial: "))
while(x<=b):
    fact = x * fact
    x+=1
print(f"Factorial of Number is : {fact}") 


