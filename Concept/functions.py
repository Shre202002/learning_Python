#Functions- GROUP of statement performing the specific TASK 


# Syntex->  def <name of function> (): <defibation of function 
#  calling -> <name of function>()

# l = []

# def avg(e = "Your answer is "):
#     a =int(input("Enter the value "))
#     b =int(input("Enter the value "))
#     c =int(input("Enter the value "))
#     d = (a+b+c)/3
#     print(f"{e} {d}")
#     l.append(d)

# for i in range (3):
#     avg()

# print("Your Average Values are : ", l)



#RECURSION FUNCTION -> CALLING THE FUNCTION INSIDE THE THE FUNCTION..!

f =1
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return n*fact(n-1)
    

c = int(input("Enter Number For factorial: "))
print(f"Factorial of {c} is {fact(c)}")