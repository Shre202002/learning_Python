# Great All the persons whose name starts with Particular Character 

l = []

c = int(input("Enter Number of names You want to enter: "))

for a in range(c): 
     a = input("Enter You name: ")
     l.append(a.capitalize())  
else:
     print("Thanks For entering the names ")

for name in l:
     if(name.startswith("S")):
          print(f"Hello {name} How are You ?")   
