# Ibn python TUPEL stores the different data together but in unnmutable formate i.e the orignal value can't be changed using the TUPLE

# if you have to store the next value in the tupple then add comma else it would be considered as a integer

t1 = (1,2,3,4, "hello" , "Sriyansh", 2)
t3 = (1,2,4,6,9)
t2 = sorted(t3)
t4 = sum(list(t3))
print(t4)
# print(t2)



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


#submission of elements of tuple 
#Program that contain the vovvel and conconent character in tupple create the list of vovle from tupple 
vovel = ("HEllo World")
