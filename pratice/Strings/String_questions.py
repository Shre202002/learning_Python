name = input("Enter Your name: ")
print("good afternoon", name)
print(f"good afternoon {name}") # F string Helps to use the variable directly in the code to print the output!
 

date = input("enter date: ")
letter = '''Hay <|name|> you are Invited For Party <|date|>'''
print(letter.replace("<|name|>" , name) .replace("<|date|>" , date))
# Replacing The String from the saved String Runtime 


