#Advanced Dictionaries Concepts -----> For getting the advance concepts of Dictionaries i.e. Dictionary contains SOME DEFAULT VALUES 

# For Creating the default dictionary we have to import the ------->

from collections import defaultdict

# <variable_name> = defaultdict(<data_type>)
 
my_dict = defaultdict(int)

print(my_dict['age'])  #--------> By default it will retun the "0" as the result So it gir DEFAULT value 

print(my_dict)         #-------> Now it will not return the EMptY DICTIONARY as it have a key value pair of AGe and 0

def notpresent():
    return 'The element is not present'
dt = defaultdict(notpresent)
dt['A']==123
dt['H']=234
print(dt['A'])
print(dt['H'])



# ORDERED Dictionary...

print("This is Ordered Dictionary...!")
dictionary = {}
dictionary['a'] = 1
dictionary['b'] = 2
dictionary['c'] = 3
dictionary['d'] = 4