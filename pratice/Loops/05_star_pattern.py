# Star Ptern 
'''
----*
--*****
---***
-*******
*********

'''

i = int(input("Enter The Number Of lines: "))

for a in range( 0, i+1):
    print(" " *(i-a), end="")
    print(" *" * (2*a-1), end="")
    print("\n")