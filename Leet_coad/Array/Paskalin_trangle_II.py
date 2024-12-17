# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

ans,arr = [],[]
n = int(input("Enter the range: "))
i=1
n = n+1                      
for i in range(1,n):
  c=1
  for j in range(1,i+1):
     arr.append(c)
     c = int(c*(i-j)/j)
  ans.append(arr)
  arr =[]

print(ans)