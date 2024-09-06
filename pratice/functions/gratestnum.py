# Program to find the greatest number Given By the user


def greatest(num):
   num.sort()
   num.reverse()
   return(num[0:3])


l = []

i = int(input("Enter the Total numbers you want to enter: "))

for n in range (0,i):
    p = int(input("Enter the  numbers : "))
    l.append(p)

# print(l)
b = greatest(l)
print(b)