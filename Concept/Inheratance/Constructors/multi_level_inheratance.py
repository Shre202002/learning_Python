# Learning the concept of Inheritance

class Employess:                                            #---------> Base Class-1
    salary = 15,00,000.00
    def pay(self):
        print(f"This Employee saley is {self.salary}")


# This is the Making different Classes and copying the data from the above class insted of inherating the data from the above class        
class Programmer:                                          #---------> Base Class-2
 company = " Zomato "
 name= "Shre"
 prg = "Python"

 def data(self):
     print(f"The name is {self.name} and working at {self.company} on project with programming language is {self.prg} ")


# Making the class And INHERATING THE DATR FROM THE PARENT CLASSES 

class inheritclass(Programmer, Employess ):               #--------------> INHERATE Class, Class Which got inherate First can not  overrider the variables with same name
  
    def printdata(self):
       print(f"Employess {self.name} works in the company {self.company} and working on the project with language {self.prg} with salary at {self.salary}.")
     

a = Programmer()
a.data()
c = inheritclass()                                         #-------------> Now Inheret Class can have access to all the methods inside the programer class and Employee class 
c.printdata()
# print(c.company)