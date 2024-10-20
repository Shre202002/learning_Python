class Employee:


    def __init__(self, salry , incriment ):       #---> First argument in any of the function is always be "SELF"tf
        self.increment = incriment
        self.salary = salry
        

    @property
    def afterincrement(self):
        return ( self.salary + self.salary * (self.increment /100) )

    @property
    def changesalary(self):
        return self.afterincrement - self.salary

    

    # @afterincrement.setter
    # def afterincriment(self,salary):
    #     self.increment = ((salary/self.salary)-1)*100

salary = int(input("Enter your salary: "))
increment = int(input("Enter your increment in Percentage : "))
s = Employee(salary, increment)
print(f"The salaery after Increment is {s.afterincrement}")
print(f"The change in salary is: {s.changesalary}") 

    
 