class twoD_Vector:

    def __init__(self, i,j):
        self.i = i
        self.j = j
     
    def show(self):
        print(f"The 2-D Vector Data is {self.i} + {self.j}")

    def __mul__(self ,  num):
        return   ((self.i *num.i)+(self.j * num.j))
        
class threeD_Vector(twoD_Vector):

    def __init__(self, i,j,k):
        super().__init__(i,j)
        self.k = k
     
    def show(self):
        print(f"The 3-D Vector Data is {self.i}i + {self.j}j + {self.k}k")

    def __mul__(self ,  num):
        return   ((self.i *num.i)+(self.j * num.j)+ (self.k * num.k))



def input_data():
  threeD = []
  for i in range (3):
     n = int(input(f"Enter value {i+1} for the 3D vector: "))
     threeD.append(n)

  return threeD



# twoD1 = twoD_Vector(5,6)
# twoD2 = twoD_Vector(10,20)
# print(f"The Dot Product Of 2D vector  is  {twoD1 * twoD2}")

print("DOt product of Two #D vector ")

print("Enter which vector Product you want: ")

vectors = []
for i in range(2):
    print(f"Enter the {i+1} Vector Values")
    v = input_data()  # Get user input for the vector
    vectors.append(threeD_Vector(v[0], v[1], v[2]))  # Create threeD_Vector instance and store in list
    



print("\nVector 1:")
vectors[0].show()
print("Vector 2:")
vectors[1].show()
print(vectors)


# For N-D VECTOR WITH DOT PRODUCT 

# class nD_Vector:
#     def __init__(self, components):
#         self.components = components  # Store all components in a list

#     def show(self):
#         vector_string = " + ".join([f"{val}e{i+1}" for i, val in enumerate(self.components)])
#         print(f"The {len(self.components)}-D Vector is: {vector_string}")

#     # Dot product calculation for nD vectors
#     def __mul__(self, other):
#         if len(self.components) != len(other.components):
#             raise ValueError("Vectors must have the same dimension for dot product.")
#         return sum(x * y for x, y in zip(self.components, other.components))


# # Function to get user input for an n-dimensional vector
# def input_data(n):
#     components = []
#     for i in range(n):
#         component = int(input(f"Enter value {i+1} for the {n}-D vector: "))
#         components.append(component)
#     return components


# # Ask the user how many dimensions the vector should have
# n = int(input("Enter the dimension (n) of the vector: "))

# # List to store dynamically created nD_Vector objects
# vectors = []

# # Loop to create and store multiple instances of nD_Vector dynamically
# for i in range(2):  # Suppose we want to create 2 vectors
#     vector_values = input_data(n)  # Get user input for the n-dimensional vector
#     vectors.append(nD_Vector(vector_values))  # Create and store the object

# # Displaying both vectors
# print("\nVector 1:")
# vectors[0].show()  # Access first vector from the list
# print("Vector 2:")
# vectors[1].show()  # Access second vector from the list

# # Calculating the dot product of the two vectors
# dot_product = vectors[0] * vectors[1]
# print(f"\nDot product of the two {n}-D vectors: {dot_product}")
