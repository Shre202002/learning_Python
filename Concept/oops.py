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

         
        
    
sriyansh = Employee()
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

class Student():
    
    def __init__(self,id,name,collage):
        self.id= id
        self.name = name
        self.collage = collage

    def get_id():
        print(f"The ID of Student Is{id}")
    def getOther():
        print(f"The Name of student is {Student} and collage is {collage}")

s = input("Enter Name: ")
i = int(input("Enter ID "))
c =input("Enter COllage Name ")
s = Student(s,i,c)
s.get_id
s.getOther
