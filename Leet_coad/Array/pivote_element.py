# 724. Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

nums = [2,1,-1]
s = sum(nums)
n = len(nums)
print(n)
print(f"THE SUM IS {s}")
print(f'total elements are: {len(nums)}')
l=0
for i in range(n):
    r = s - l - nums[i]

    if(r == l):
        print(f'The Pivote is {i}')
        break

    l =  l + nums[i]


else:
    print('No Pivote is there...!')