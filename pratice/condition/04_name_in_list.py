#Check weather the given name is present in list or not !

l = []

a = input("Enter name: ")
l.append(a)

a = input("Enter name: ")
l.append(a)

a = input("Enter name: ")
l.append(a)

a = input("Enter name: ")
l.append(a)


b = input("Enter Name to find: ")

if(b in l):
    print(b , " is present in the list")