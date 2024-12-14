# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

arr = []
n = int(input("Enter the range: "))
i=1
c=1
n = n+1
for i in range(1,n+1):
    print(i)
    arr.append(c)
    c = int(c*(n-i)/i)
    # print(arr)
    i=+1
print(arr)