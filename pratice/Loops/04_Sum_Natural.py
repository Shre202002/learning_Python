# Sum Of N-natural Numbers 

i = int(input("Enter the Number range "))
a=0
s=0
b=0
while (a<=i):
    s = s+a
    a+=1

print(f"Sum of {i}  natural number  is {s}")


for a in range(0, i):
    b = b+a

print(f"Sum of {i}  natural number  is {s}")
