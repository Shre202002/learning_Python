# It is  Datatype which stores the data in form of key and value pare 
#It is iN mutable i.e Original Dictinary can be updated Using its functions 
   # Key: value 
d1 = {
    "a" : 1,
    "b": 2,
    3: "c",  # It can have any data type in key value formate 
    "d" : [4,5,6,7]
}

print(d1, type(d1))

      x~
# Methods --> Nop Indexing is there In Dict
print(d1[3])

print(d1.items()) # Return all the the items present in the dict and return in the form for TUPLE

print(d1.keys())  # Return all the the keys present in the dict and return in the form for TUPLE

print(d1.values())  # Return all the the keys present in the dict and return in the form for TUPLE

d1.update({"a": 10, "z": 26, "d": [8,9,10]}) # Update the Values of particular key in the The DICT and Add neu values in The DICT
print(d1)  

print(d1.get("d")) # Retuen the value of particular key BUT IF KEY IS NOT THERE IT WILL RETURN NONE OVER THERE 
print(d1["a"]) # rETURN THE value of particular kry but IF KEY IS NOT THERE THEN IT WILL RETURN AN ERROR THERE.

d1.pop("d") # Remove particular key from dictionary 
print(d1)

print(d1.popitem()) #Remove and return the last key of the diconary 
print(d1)

d1.clear()
print(d1)

d1.setdefault("a",20) #Returns the value of the specified key. If the key does not exist, it inserts the key with the specified default value and returns that value.
print(d1["a"])




# TO Filter the values in the dictionary we use Filter Function 

# Filter_d1 = {key: value for key, value in d1.it() if value > 10}
# print(Filter_d1)

# print(d1['k'])


dict = {"name": "john", "age": 23, "country":"India"}
dict["city"] = 'kanpur'
dict["age"] = 50        # update the single key value of the dictionary
print(dict)

dict.update({"name": "Sriyansh", "Roll": 69})
print(dict)