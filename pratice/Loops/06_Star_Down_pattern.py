#Print the downwerd star pattern 

'''

**********
-*******
--*****
---***
----*

'''


i = int(input("Enter a range of Number "))

for a in range (0, i):
    print("-" *(a), end="")
    print(" *" *(i-a), end="")
    print("\n")