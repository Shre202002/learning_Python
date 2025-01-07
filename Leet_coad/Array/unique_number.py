# 1207. Unique Number of Occurrences
# Given an array of integers arr, 
# return true if the number of occurrences of each value in the array is unique or false otherwise.

arr = [1,2,2,1,1,3]
my_dict = dict


# Example
my_list = [1, 2, 2, 3, 3, 3, 4]

# Count occurrences
element_count = {element: my_list.count(element) for element in set(my_list)}
print(element_count)  # Output: {1: 1,                   2: 2, 3: 3, 4: 1}    
