#  Print he pattern using reclusion 
# * * * 
# * *
# *


def pattern(n):
    
    if(n== 0):
        return
    print("*" * n)
    pattern(n-1)

i = int(input("Enter the number of lines you want to print: "))
a = pattern(i)