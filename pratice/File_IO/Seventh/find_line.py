#To find Out the line over which the data/Text  is present 

with open(r"D:\learning_Python\pratice\File_IO\five\data.txt") as f:
    p = f.readlines()
   #  print(p, type(p), len(p))
line_count = 1
word ="python"

for i in p:
   if (word in i):
      print(f"Yes, Word {word} is present in line number {line_count}")
      break
   line_count +=1

else:
   print(f"{word} is Not present")
    
         