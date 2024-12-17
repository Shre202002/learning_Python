# c1,c2=0,0
# nums = [1,1,1]
# n =len(nums)
# for i in range(0,len(nums)):
#     if(nums[i]>= nums[i+1]):
#         print(f'this is small {nums[i]} --- {nums[i+1]} ')
#         print(i)
#         c1+=1

#         if i == n-2:
#             print('True YES MONOTONIC--1')
#             break
#         continue
#     if(nums[i]<= nums[i+1]):
#         print ('False Not Descending true') 
#         break   
# if(c1 != 0 ):
#     print('NOt Monotonic Array')
# else:
#     for i in range(0,len(nums)):
#         print(i)
#         if(nums[i]<= nums[i+1]):
#             print(f'this is greater {nums[i]} --- {nums[i+1]} ')
#             c2+=1
#             if i == n-2:
#                 print('True YES MONOTONIC--2')
#                 break
#             continue
#         if(nums[i]>= nums[i+1]):
#             print('NOT Monotonic') 
#             break

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increasing = decreasing = True  # Assume the list is both increasing and decreasing initially
        
        for i in range(len(nums) - 1):  # Loop until the second last element
            if nums[i] > nums[i + 1]:  # If the current element is greater than the next
                increasing = False     # It can't be increasing
            if nums[i] < nums[i + 1]:  # If the current element is smaller than the next
                decreasing = False     # It can't be decreasing
        
        # If it's either increasing or decreasing, it's monotonic
        return increasing or decreasing

s = Solution
nums= [1,1,1,1,1]   
print(s.isMonotonic(nums))