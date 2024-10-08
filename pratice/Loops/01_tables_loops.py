# Print table using loops 
t= int(input("Enter the Number for table"))

for a in range(1, 11):
    print(f"{t} X {a} = {a*t}")

else:                        #-------> Elese Will Execute Only when Loop condition get's FALSE If We Break the lop then ELse would Not be EXECUTED!s
    print("Loop Ends ")
    
for a in range(0, t*11, t):
    print(a)
else:
    print("Loop Ends ")

a =0
while (a<11):
    print(f"{t} X {a} = {a*t}")
    a+=1
