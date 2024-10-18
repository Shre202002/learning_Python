class Parent:

    def __init__(self, name , P_name): #-----> Creating the Constructor of the Parent Class Which is being called by default 
        self.name = name
        self.P_name = P_name

    def s_name(self):
        print(f"Student Name is {self.name} and his parent name is {self.P_name}")

class Studen(Parent):

    def __init__(self, salary , company , Prg, name , P_name):
        super().__init__(name , P_name )         #-----------------. Inheriting the Proprty or method to the derived class from the base class 
        self.salary = salary
        self.company = company
        self.Prg = Prg

    def data(self):

        print(f" Student name is {self.name}\n his parent name is {self.P_name} \n His salary is {self.salary} at company {self.company} on programing lang {self.Prg} ")

a = Studen( 1500000 ,"Zomato", "Python" , "Shre", "sriyansh")

a.s_name()
a.data()