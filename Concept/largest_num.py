# grates Number among thee
l =[]
a = int(input("Enter A number : "))
l.append(a)
b = int(input("Enter A number : "))
l.append(b)
c = int(input("Enter A number : "))
l.append(c)

l.sort()
p = len(l)-1
print(p)
print(f" Grates Number among three is {l[p]}")

