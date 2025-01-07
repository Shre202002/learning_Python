class Employee:
    Name ="Sriyansh"
    Language =  "Python"
    salery = 150000
    
    def __init__(self,name,salary,lang): 
      print("I am creating and object ")
      print(f"MY Name is {name}.\nMy fave language is:{lang}\nmy salery is: {salary}")
    
    
sriyansh = Employee("Shre", 200000, "Java Script")

# Shre = Employee() ---------------> Will Give an error as Evertime an object is created I will Call Init Method and INIT metod will requir the 3- Parameters 


# in PYTION THERE is not Over loadding of the constructor
# As everime it we create 2 the constructor within the class it will call the 
# most recent and update constructor

class emp_bonus():
   def __init__(self):
      print("This is First constructor")
   def __init__(self,i):
       print("This is second constructor...!")

e = emp_bonus(1)