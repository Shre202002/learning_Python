# Exception is a ab normal condition that occur ata the run time and prevent or terminate the program exections 
#The process of handling the exceptions are known as the exception handling


# ---> Der Division Error

# num = int(input("Enter a number: "))
# print(10 / num)

# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
    #   print("Try Block Is executed")-----------> At a time one exception can be handel by integrator 
# except ZeroDivisionError:
#     print("You cannot divide by zero!")
# except ValueError:
#     print("Invalid input. Please enter a number.")

# a = 'd'
# print(5 / a)   #ZeroDivisionError: division by zero

# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print("Division successful!")

    




# num = int(input("Enter a Number: "))
# if num < 0:
#     raise ValueError("Negative numbers are not allowed.")

# class NegativeNumberError(Exception):
#     pass

# try:
#     num = -5
#     if num < 0:
#         raise NegativeNumberError("Negative numbers are not allowed.")
# except NegativeNumberError as e:
#     print(e)


# Avoid this:
# try:
#     num = int("abc")
    
# except:
#     pass  # Silently ignores the error


def find_sum(value_1,value_2):
    try:
        print(value_1+value_3)
    except NameError:
        print("Function name error")
    finally:
        print("Sum finally")
try:
    find_sum(12,13)
except NameError:
    print("Invocation name error")
finally:
    print("Invocation finally")




