# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order


def anagram(str:list[str]):
 dict_duplicate = {}
 sorted_elements = [''.join(sorted(string)) for string in str]


 print([''.join(sorted(string)) for string in str])
 for index , element in enumerate(sorted_elements):
  
  if element in dict_duplicate:
   dict_duplicate[element].append(index)
  else:
   dict_duplicate[element] = [index]

 print(dict_duplicate)


anagram(["banana", "apple", "cherry", "date",'anabna'])


# l = ['cab','bba' , 'ca']
# print(l)
# j = '_'.join(l)
# print(type(j))
# print(j)
