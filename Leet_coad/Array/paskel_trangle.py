# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

arr = []
n = int(input("Enter the range: "))
i=1
c=1
n = n+1
for i in range(1,n+1):
    # print(i)
    arr.append(c)
    c = int(c*(n-i)/i)
    # print(arr)
    i=+1
print(arr)



# 1   ---->0
# 1 1   --->1
# 1 2 1   --->2
# 1 3 3 1   -->3
# 1 4 6 4 1  --->4


# # c = c * (n-i)/i
# arr = []
# # n ---> input from user
# # i ----> for loop iteration
# # c ----> for printing the values in the array 

# c=1
# n = n+1
# for(i=1, i<=n, i++){
#    i<n    2<=5    3<=5   4<=5  5<=5  6<=5
#     arr.append(c)    --> i =5 , c= 1 , 4,6,4,1 arr = [1,4,6,4,1]
#     c = c * (n-i)/i ----> c = 4 * (5-2)/2 = 6  ,  6 *(5-3)/3 = 4 ,  4 * (5-4) / 4 = 1, 1 * (5-5)/5 =0
#     i++ ---> i = 3, 4 5, 6

# }

# print (arr)





# n=4
# i=1 1<5 c = 1 arr =  [1] c = 1 * (5-1)/1 = c = 4, i++--> i=2
# i=2 2<5 c = 4 arr = [1,4] 
