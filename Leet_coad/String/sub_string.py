#  Make String a Subsequence Using Cyclic Increments

# You are given two 0-indexed strings str1 and str2.
# In an operation, you select a set of indices in str1, and for each index i in the set, 
# increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.
# Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.


s = "az"   #------> Sub String Find
t = "abcd"  #------> Parent String
c=0
i=0  
j = 0
print(len(s))
print(len(t))
while i < len(t) and j < len(s):
    print(chr(ord(t[i])+1))

       
    if s[j] == t[i] or s[j] == chr(ord(t[i])+1) or t[i] == 'z' and s[j] == 'a':
        j+=1
        c+=1
    i+=1

    
if c == len(s):
    print("Yes Sub String")
else:
    print("Not Sub-String")



