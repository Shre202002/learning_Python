# Print table using loops 
t= int(input("Enter the Number for table"))

for a in range(1, 11):
    print(f"{t} X {a} = {a*t}")

else:
    print("Loop Ends ")
    
for a in range(0, t*11, t):
    print(a)
else:
    print("Loop Ends ")

a =0
while (a<11):
    print(f"{t} X {a} = {a*t}")
    a+=1
