sum =0

for i in range (10):
    sum = sum +i
    avg = sum /10
print(f"Average of First 10 natural Number is {avg}")


#Print Even Odd

E = []
O = []

for i in range (20):
    if (i % 2 == 0):
        E.append(i)
    else:
        O.append(i)
        
print(E)
print(O)
# for i in range(len(E)):
#     print(f"Odd Numbers are {E[i]}")
# for i in range(len(O)):
#     print(f"Even Numbers are {O[i]}")