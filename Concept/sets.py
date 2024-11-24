# FROZEN SET = ---------------> Values Can Not be Modified   ---> STRICTLY INMUTABLE...!
#Set is collection of well defined objects
#Set's are MUTABLE 
# Set is the dictonary with only values over there 
# empty set is being created by s = set() it is not created like s= {}  it will create by default DICTONARY 

s = {1,62,3,5,4,6,1,1,1,5,4,6,2,2 }
print(s) # output: {1, 2, 3, 4, 5, 6} As in set nop values are being repeated 

s.add(10) # Add element inside the set 
print(s)

s.update({11,12,3}, ['a','b','c','d'], (15,18,24))  #Updates the set by adding elements from other iterables (e.g., lists, sets, tuples).pytho
print(s)

s.remove(1) #Removes the specified element from the set. 
s.remove(10) 
# s.remove(10) #If the element is not found, it raises a KeyError

# print(s) 

s.discard(10) #Removes the specified element from the set if it is present. If the element is not found, nothing happens (no error is raised).
print(s) #NO ERROR IS THERE AS 10 IS ALREADY REMOVED FROM THERE SO THERE IS NO ERROR BECAUSE OF DISCARD 


print(s.pop()) #remove the first element from the set ---> Return the Removed Element
print(s)

s.clear()        # CLear all the elements of the SET
print(s)



s.update([1,2,3,4])
print(s)
s2= {2,4,6,8}
s3={1,3,5,7,9}
print(s2.union(s3)) # new SET is returned from the union of sets COMEN are taken Once oly 
print(f"pipe line {s2|s3}")
print(s2.intersection(s)) #Returns a new set with elements that are common to the set and all others (intersection operation).
print(f"& Symbol  {s2&s}")


r = s.difference(s2) # Pehile JO elements dusre me na ho un ko return kr ta hai set ke formate me 
print(f'Difference of set is {s-s2}')
print(r)


print(s.symmetric_difference(s2)) # Un common elements of both set's are being returned 
print(f'Syetric Difference of set is {s^s2}')

# FROZEN SET = ---------------> Values Can Not be Modified   ---> STRICTLY INMUTABLE...!
set2 = frozenset(s2)
set2.update(12)  #----> frozenset' object has no attribute 'update'