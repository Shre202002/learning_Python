
with open(r"D:\learning_Python\pratice\File_IO\Fouth\textfile.txt" ,"r") as f:
    newContent = f.read().lower().replace("teacher", "Sriyansh", 10)
with open(r"D:\learning_Python\pratice\File_IO\Fouth\textfile.txt","w") as n:
     n.write(newContent)