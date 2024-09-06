 # recursive function to print sum of first n natural number !
 
def sum(n):
     if(n==0 or n == 1):
         return 1
     return n+sum(n-1)

i = int(input("Enter The number: "))
print(f"sum for {i} natural numbers is {sum(i)}")