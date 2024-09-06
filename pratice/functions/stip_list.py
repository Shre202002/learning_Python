# Strip the specific characters from the list and return the new list with striped characters 

def strip(n, word):
  stripped_list = []
  for item in n:
      stripped_list.append(item.strip(word) )
  return stripped_list

my_list = ["applea", "abanana ", "cherrya"]

B =strip(my_list, "a")
print(B)
