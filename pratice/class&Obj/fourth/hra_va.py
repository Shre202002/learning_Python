class Employee:
    def __init__(self,id,name,designation,department,b_salary):
        self.id = id
        self.name =  name
        self.designation = designation
        self.department = department
        self.b_salary = b_salary

    def net_salary(self):
        hra = 20/100 * self.b_salary
        va = 30/100 * self.b_salary
        return self.b_salary + hra + va

    def display(self):
        print(f'The Employee name is {self.name}\nHis ID is{self.id}\nWorking in department {self.department} at designation of {self.designation}\n with besic salary of {self.b_salary}\nNet salary is {self.net_salary()}')

e1 = Employee(1,"Shre",'HOD','M.C.A',150000)
e1.display()

