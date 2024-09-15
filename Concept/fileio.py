# To make changes over the file i.e READING IT, WRITING IT AND EDITING  we can do all these things with PYTHON 
# once the file is opend it's compelsary for the file to get close 
# to OPEN THE FILE WE USE :- <vaiavle> = open("<file name>) ----> as it always return the file data when it's being called 
import os
print(os.getcwd()) # Shows the path bat which python terminal is open !
f = open(r"D:\learning_Python\Concept\text.txt")   #r ->  For Reading the file PYTHON
data = f.read()
print(data)
f.close()



#To Writhe in the FILE In PYTHON!! --> IF we Write to Pre-Defined File then the previous data written all would be removed 


test = "Hii I am added by the code in this file"
f = open(r"D:\learning_Python\Concept\new_text.txt","w") 
f.write(test)
f.close

# To Read the Lines Of particular file in python then we have to use -> .readlines()

f = open(r"D:\learning_Python\Concept\text.txt") 
lines = f.readlines()
print(lines, type(lines))
f.close


# To Read the Particular Line from the file in python then we have to use -> .readline()

f = open(r"D:\learning_Python\Concept\text.txt") 
# line1 = f.readline()
# print(line1)
# line4 = f.readline()
# print(line4)
# line2 = f.readline()
# print(line2)
# line3 = f.readline()
# print(line3, type(line3))
# f.close

# With help of loops

line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()
f.close()



#Append and text in already written file ---> Adding at the end of the file "a"

f = open(r"D:\learning_Python\Concept\text.txt", "a")
text = "\n This is the text Appended at the bottem form coade"
f.write(text)
f.close 


#WITH in FILE IO-----|)
with open(r"D:\learning_Python\Concept\text.txt") as f:
    print(f.read())


