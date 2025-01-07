# What is way of implementing the INCAAPULATION in PYTHON?
# We can implimnent it buy using the Class and access specifier in the class 
# -> Public
# -> Private --------> Variable can't be accessed out side the class  
#                  --> To show any variable as private we display it at double underscore --> '__'
# -> Protected ---------> Variable can be accessed out side the class
#                     --> To show any variable as protected we display it at single underscore --> '_'


class Address:
    def __init__(self,city,mobile_no):
        self.city = city  #Public
        self.__mobile_no = mobile_no #private
        self._state = "UP" #Protected 


obj = Address('kanpur', 96328281)
print(obj.city)
print(obj._state)
# print(obj.mobile_no)    # cannot be accessed



# How to access private memnber out side the class
#     there are 2 ways to access private member outside the class

#         -> Getter method  --> it get thr value of a property/data felid/ of any class

class student:
    def __init__(self,id,name):
        self.__id = id
        self.name = name
#syntex--> def det_<attribute>
    def get_id(self):            # ----> getter function return the private variable 
        return self.__id
    def set_id(self,data):
        self.__id = data

stud = student(123,"Shre")
print(f'the accessing the private variable {stud.get_id()}') #------> Accessing it using getter function
stud.set_id(963)                                          #---> Updating the value using the setter function 
print(f'the accessing the private variable by updating it {stud.get_id()}') 

#         -> Name mangling ---> WHEN we put a double underscore in front of the attribute name--> Python will internally change it's name to 
#                            -> _Classname__attribute(name mangling).
#

class product:
    def __init__(self,product_id,name,price):
        self.__product_id = product_id
        self._name = name
        self._price = price
    def get_product_id(self):
        return self.__product_id
    def display(self):
        print(f'product name: {self._name}\nproduct id: {get_product_id()}')