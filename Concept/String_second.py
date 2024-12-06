# Slicing In Python- Slicing The character from middle in python 

a = "Hello I am sriyansh"
print(a[0:3])

# ADVANCE SLICING- gETTING THE STRING FROM THE MIDDLE OF THE STRING OR bY SKIPING AT PARTICULAR SIQUENCE !
print(a[0:7:3])

# String Functions 
# -> len 
print(len(a)), #To find the length of the string 
print(a.endswith("nsh"))
print(a.capitalize())  # Capatalise First letter of the Sentence Or String 
print(a.rstrip())  # Remove the wide space from the string 
replace_word = a.replace("Hello" , "Hii") # Change all the occurance of that particular string
print(replace_word)


#Write a python program to print the vowels Characters OF STRING !
# vowel = ['a', 'e','U','O','I','E','A','u','o','i']
# s = input("ENter a String: ")
# for i in range (len(s)):
#     if s[i] in vowel:
#         print(f"THE VOWEL IS PRESENT AT INDEX:{i+1} AND VOWEL IS {s[i]}")

# WAP to find the Friquency of Character In STRING

l={}
# for i in s:
#     if i in l:
#         l[i] = l[i]+1
#     else:
#         l[i] = 1

print(l)

#WAP to check the string is palendrom or nOT:
p = input("Enter a String For palendrome:")
n =  (p)
print(n)
if n == p:
    print(f"Haaan {p} aur {n} Hamshakal hai")
else:
     print(f"Haaan {p} aur {n} Hamshakal NAHI hai")