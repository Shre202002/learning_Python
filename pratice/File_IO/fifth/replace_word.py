Words = ["teacher", "Who", "With"]


with open(r"D:\learning_Python\pratice\File_IO\fifth\poem.txt","r") as f:
    content = f.read()
    for i in Words:
        content = content.replace(i,"*"*len(i))

with open(r"D:\learning_Python\pratice\File_IO\fifth\poem.txt","w") as f:
   f.write(content)