# Find the word in file 


#In this Sinerio our complete file is compared to a particular word which is teacher if any word other than "teacher" would present then
# Our condition would get false 
with open(r"D:\learning_Python\pratice\File_IO\first\poem.txt") as f:
    c = f.read()
    print(c)
    if("teacher"== c): # Comparing the entire File content with the Word teacher if any word other than that would present even space or new line then there would be an error
        print("World is present")
    else:
        print("Word is not Present")

# To solve it with this method we have to 

with open(r"D:\learning_Python\pratice\File_IO\first\poem.txt") as f:
    if "teacher" in f.read():
        print("World Teacher is present there ")
    else:
        print("Word Teacher is not present there ")



#In this Sinerio our file text is compared to a particular word one by one  which is teacher if any word other than "teacher" would present then
# Our condition would get false 
f = open(r"D:\learning_Python\pratice\File_IO\first\poem.txt")
c= f.read()
if("teacher"== c):
    print("Word Teacher is Present")
else:
    print("Word Teacher is Present")
f.close()


#Check The Count Of that particular Word:-
count = 0
with open(r"D:\learning_Python\pratice\File_IO\first\poem.txt") as f:
    line = f.readline()
    while(line != ""):     # In this case We are counting each and every line only not every sting for counting of that Particular Sting 
        if "teacher" in line:
            count +=1
        line = f.readline()
print(f"The Word teacher is present {count} times in file. ")



#Check The Count Of that particular Word:-

with open(r"D:\learning_Python\pratice\File_IO\first\poem.txt") as f:
    count = f.read().count("teacher")              # Using the pre built function Count in the counting of the String appearance

print(f"The Word teacher is present {count} times in file. ")




#Other Ways By Using the---->  split() As It split's the Entire Text file in small text and after that it compar them all 
with open(r"D:\learning_Python\pratice\File_IO\first\poem.txt") as f:
    c = f.read().split()
    # print(c, type(c))
    if "sriyansh" in f.read().split():
        print(f"The Word teacher is present in file. ")
    else:
         print(f"The Word teacher is not present in file. ")