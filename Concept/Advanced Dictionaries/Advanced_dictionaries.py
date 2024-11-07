#Advanced Dictionaries Concepts -----> For getting the advance concepts of Dictionaries i.e. Dictionary contains SOME DEFAULT VALUES 

# For Creating the default dictionary we have to import the ------->

from collections import defaultdict

# <variable_name> = defaultdict(<data_type>)
 
my_dict = defaultdict(int)

print(my_dict['age'])  #--------> By default it will retun the "0" as the result So it gir DEFAULT value 

print(my_dict)         #-------> Now it will not return the EMptY DICTIONARY as it have a key value pair of AGe and 0