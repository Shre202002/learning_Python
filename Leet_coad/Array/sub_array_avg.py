# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Given an array of integers arr and two integers k and threshold, 
# return the number of sub-arrays of size k and average greater than or equal to threshold.

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        target_sum = threshold * k  # Calculate the required sum
        current_sum = sum(arr[:k])  # Initial sum of the first 'k' elements
        count = 0  # Count of valid subarrays
        
        # Check the first window
        if current_sum >= target_sum:
            count += 1
        
        # Sliding window
        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]  # Add the new element, remove the old one
            if current_sum >= target_sum:
                count += 1
        
        return count
    
s = Solution
print(s.numOfSubarrays([2,2,2,2,5,5,5,8], 3,4))
