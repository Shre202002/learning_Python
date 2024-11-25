# Given an integer array nums, return true if any value appears at least twice in the array,
#  and return false if every element is distinct.
def solution(): 
 nums=[10,20,41,10]

 nums.sort()
 for i in range (len(nums)):
  if (nums[i-1] == nums[i] and i != 0):
   return True
 return False

print(solution())
# solution()