# Classes In PYTHON

# Besic class

class Employee:
    name = "SHRA" # ----------------> Class Attribute have less  preference than Object Instance
    lang = "Python" #----------> Class Attribute
    salary = 200000
    
    def getInfo(self): #------> Self is the argument for reiving the default values for function inside the class
        print(f"Employee is {self.name} \nThe language is {self.lang} and salary is {self.salary}")
        
    #@staticmethod ---> For the methods which don't need any argument for their Execution
    @staticmethod
    def wishes():
        print("Hello Guys Good Morning")
     
    # def __init__(self,name , salery , lang):         #------------> Dunder Method Which is automatically called When ever object is created 
    #     print("I am creating and object ")
    #     print(f"MY Name is {self.name}.\n My fave language is:{self.lang}\n and my salery is: {self.salary}")

         
        
    
sriyansh = Employee("Shre", 150000 , "JavaScript")
# sriyansh.name = "Sriyansh Gupta"  #-----------------> Object Instant Attribute > Class Attribute
sriyansh.getInfo()
# Employee.getInfo(sriyansh) -------> Syntatic Suger for the above 
print(sriyansh.name, sriyansh.lang)





# shre = Employee()
# shre.name ="Shre Shre" #-----------------> Object Instant Attribute > Class Attribute
# print(shre.name , shre.lang , shre.salary)





# new_Employee = Employee()
# print(new_Employee.name, new_Employee.lang)


# Self parameter 

