# Check the file Weathere the fiile is copy of not Or it is new Unique File 

with open (r"D:\learning_Python\pratice\File_IO\Sixth\File_1.txt") as f:
    content = f.read()
    
with open (r"D:\learning_Python\pratice\File_IO\Sixth\Second_2.txt") as p:
    content2 = p.read()
    
if(content == content2):
    print("Yes Boath files are same")
else:
    print("No Both Files are not same")
