#Rename THe Existing File 

import os   # By Importing the OS Module we can change the old name of the file and rename it 


# old_name = r"D:\learning_Python\pratice\File_IO\Eighth\Old_FIle.txt"
# New_name = r"D:\learning_Python\pratice\File_IO\Eighth\New_file.txt"

# os.rename(old_name,New_name)

# print("File renamed successfully!")



# 2-> By Using The--->  pathlib import Path

# from pathlib import Path

# # Give Old File Name and Path 
# old_name = Path(r"D:\learning_Python\pratice\File_IO\Eighth\Old_FIle.txt")

# old_name.rename(r"D:\learning_Python\pratice\File_IO\Eighth\New_FIle.txt")

# print("File renamed successfully!")




# 3 ---> Using the Exception Handling 

old_name = r"D:\learning_Python\pratice\File_IO\Eighth\Old_FIle.txt"
New_name = r"D:\learning_Python\pratice\File_IO\Eighth\New_file.txt"

try:
 os.rename(old_name, New_name)
 print("Updated Successfully ")

except FileNotFoundError:
    print(f"Error: {old_name} does not exist.")
except PermissionError:
      print(f"Error: Permission denied to rename {old_name}.")
    