'''
print ther hollow star pattern 

**********
*--------*
*--------*
*--------*
**********
'''


i =  int(input("Enter the height "))
# j =  int(input("Enter the width "))

for a in range (0, i):
    if(a == 0 or a == i-1):
       print("*"*i)
    else:
        print("*"+"-"*(i-2)+ "*")
print("\n")