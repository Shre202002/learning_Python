ly = ['Shre', 'Raja', 'Rama','Shibh']
# Lyst Coprision
# SYNTEX 
# newlist = [Expression for the items in the itereable list if condition is true]


newlist = []

for i in ly:
    if 'j' in i:
        newlist.append(i)

        print("Yes Present")
print(newlist)

# Lyst Coprision
newlist_2 = [i for i in ly if 'a' in i]
print(newlist_2)

n = [34, 78, 90, 23, 45, 45, 89, 90, 56, 34, 23, 45, 67, 89, 90]
# Conver the list onto set to remove the duplicates
n1 = set(n)
print(n1)
#remove the duplicates from the list
newlist_3 = []
for i in n:
    if i not in newlist_3:
        newlist_3.append(i)
print(newlist_3)

# Lyst Coprision
newlist_4 = []
[newlist_4.append(i) for i in n if i not in newlist_4]
print(newlist_4)



dict_1 = {
    'brand': 'maruti',
    'model': '800',
    'electric': False,
    'year': 1998,
    'color': 'white',
    'price': 500000,
}
print(type(dict_1))
print(len(dict_1))

# Dictionary CONSTRUCTOR
newdict = dict(name= 'Shre', age=23, city='Delhi')
print(newdict)
print(type(newdict))
print(len(newdict)) 
print(newdict['name'])
print(newdict['age'])
print(newdict.keys())
print(newdict.values())


key =['brand', 'model', 'electric', 'year', 'color', 'price']
value = ['maruti', '800', False, 1998, 'white', 500000]
# using zip() function to create a dictionary from two lists
newdict_2 = dict(zip(key, value))
print(newdict_2)
print(newdict_2.pop('model'))
print(newdict_2.popitem())
print(newdict_2.clear())
