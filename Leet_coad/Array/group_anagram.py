# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order


def anagram(str_list:list[str]):
 dict_duplicate = {}
 sorted_element= list 
# .Join function in PYTHOn--->    Takes an argument i.e, which is needed to be join between them and joins the string 

#  for i in str_list:
#   j = sorted(i)
#   e = ''.join(j)
#   print(f"sorted element is: {e}")
#   sorted_element.append(f'{e}')
#  print(sorted_element)

 sorted_elements = [''.join(sorted(string)) for string in str_list]
 print(sorted_elements)


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
