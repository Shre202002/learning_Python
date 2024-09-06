# Print Weather NUMBER IS PRIME OR NOT !

i = int(input("Enter Number "))
b = 0
for a in range (2, i):
    if( i % a == 0):
       b +=1


if(b== 0):
    print(f"{i}  is prime number")
else:
    print(f"{i}  is Not prime number")
