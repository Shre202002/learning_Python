# Walrus Operators in PYTHON :=  assignment operator HOTA hai
#  --------->  it can combine assignment and evaluation in a single expression.

# SYNTEX ---------->   <Variable> := Expression 


# Without Walrus Operator
# line = input("Enter something: ")
# while line != "quit":
#     print(f"You entered: {line}")
#     line = input("Enter something: ")

# With Walrus Operator
# while (line := input("Enter something: ")) != "quit":
#     print(f"You entered: {line}")


# In List Comprehensions:  ----> (num := c*c   Assigning the value of num by wa;rus operator 
number = [num for c in range(10) if(num := c*c )< 50 and num % 2 == 0]
print (number)

def fetch_data():
    return "Hello World"

# Without Walrus Operator
data = fetch_data()  # Assume this is a function call
# if data and len(data) > 10:
#     print("Data is fetched and has more than 10 items.")

# With Walrus Operator     ------------>    data := fetch_data() Is used for assigning the value in the data variable as it returns the value rin time in conbine formate 
if (data := fetch_data()) and len(data) > 10:
    print("Data is fetched and has more than 10 items.")


# In Conditional Operators 

if (n := len("Hello World"))> 10:
    print(f"This is Hello worlds length {n}")


