# Update the data present in Which has been Entered Using the 

class Employee:
    
    def __init__(self,name,salary,project):
      
      
      with open(r"D:\learning_Python\pratice\class&Obj\Second\data.txt" ,"f+") as f:
        content = f.read()
        info = f"Emploiee name is : {name}. Salary is- {salary} working is project: {project}.\n"
        f.write(info)
        
shre = Employee("shre", 1500000, "A") 
Raj = Employee("Raj", 1200000, "B")  