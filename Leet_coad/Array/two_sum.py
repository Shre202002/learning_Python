# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# def twosum( nums: list[int], target: int):
#  for i in range(len(nums)):
#     for j in range(i,len(nums)):
#      if (nums[i] + nums[j]) == target:
#         return [i,j]
            
# print(twosum([2,7,11,15],9))

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_sort = sorted(nums)
        i = 0
        j = len(nums_sort)-1
        res = []
        while i < j:
            left = nums_sort[i]
            right = nums_sort[j]
            if left + right == target:
                res.append(left)
                res.append(right)
                break
            if left + right > target:
                j -= 1
            else:
                i += 1
        if not res:
            return []        
            
        result = []    
        for i in range(0,len(nums)):
            if nums[i] in res:
                result.append(i)
        return result

            
s = Solution()
print(s.twoSum([2,7,11,15],9))
