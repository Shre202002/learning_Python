# Slicing In Python- Slicing The character from middle in python 

a = "Hello I am sriyansh    "
print(a[0:3])

# ADVANCE SLICING- gETTING THE STRING FROM THE MIDDLE OF THE STRING OR bY SKIPING AT PARTICULAR SIQUENCE !
print(a[0:7:3])

# Sring Functions 
# -> len 
print(len(a)), #To find the length of the string 
print(a.endswith("nsh"))
print(a.capitalize())  # Capatalise First letter of the Sentence Or String 
print(a.rstrip())  # Remove the wide space from the string 
replace_word = a.replace("Hello" , "Hii") # Change all the occurance of that particular string
print(replace_word)


