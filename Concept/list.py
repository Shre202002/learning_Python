#In Python group of data is stored in list form simlar to aray in other language 
list = ["hello", "I", "am", 11 , "year" ,  25.6 , "months" , "old"]
print(list[0])
list[0] = "Hii" #Unlike Strings List orignel values can be changes so they are MUTABLE 
print(list[0])

#Methods OF LIST 

l1= [11, 12, 5.25, 22.8]

print(len(l1))

l1.sort()  # Used For the shorting of the List by changing the origenal LIST

print(l1.sort()) # These Function Does'nt return any value after the shorting of the list 
print(l1)

l1.reverse()  #Used For the reversing the LIST AND CHANGE THO ORIGENAL LIST 
print(l1)

l1.append("sriyansh") # Add the given value at the end of the string 
print(l1)

str = "sriyansh"
l1.extend(sry) # add the given value in the list as in individual item and it could be  strintg ONLY !


num = 524 # NO INTIGER COUld be extended in the EXTEND 
# l1.extend(num) # add the given value in the list as in individual item and it could be  strintg ONLY !
print(l1)


l1.insert(5,"gupta") # Insert the Value at the middle of the List i.e at the desires INDEX of the LIST
print(l1) 

print(l1.pop(-1)) #  uesd For removing the value on the string 
l1.pop(4) # This is the function which returns the popped value of the LIST and
print(l1)

l1.remove(11) # Remove the particular Charatere / Value form the list 
print(l1)

# ---------------------------------------------------------------------------------------------
# Join Concept

l = ['cab','bba' , 'ca']
print(l)
j = '_'.join(l)
print(type(j))
print(j)


list1 = [2,10,30,40]