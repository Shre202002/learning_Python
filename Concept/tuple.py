# Ibn python TUPEL stores the different data together but in unnutable formate i.e the orignal value can't be changed using the TUPLE

t1 = (1,2,3,4, "hello" , "Sriyansh", 2)

print(type(t1))
print(t1)
 
#t1[2] =  "World" there would be an error there as in tupel orignal tupel values can't be changed   


print(t1.count(2)) # Find the occurance of the the particular value of the TUPEL

print(2 in t1) # in keyword Returns the BOOLIAN if the given value is present in the tupel or not 

print(len(t1))   # retun the length of the particular TUPEL

slice = t1[1:5]   # Return The NEW TUPEL after slicing it from the particular index
print(slice)

a,b,c,d,e,g,h = t1
print(a,b,g)

print(t1)
