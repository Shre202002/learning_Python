# Add Employee Data in file and check if data is already present if not add data if yes then remove data  

class Employee:
    
    def __init__(self,name,salary,project):
      
      info = f"Emploiee name is : {name}. Salary is- {salary} working is project: {project}.\n"
      
      with open(r"D:\learning_Python\pratice\class&Obj\first\data.txt" ,"r+") as f:
            
        content = f.readlines()
        print(content, type(content), len(content))      
        
        for i in content:
          
          if info in content:
            print(f"{name}'s data is already Present")
            break
        else:   
         f.write(info)
         print(f"{name}'s data is added successfully")
         
          
          
          
          
          
        
shre = Employee("shre", 1500000, "A") 
Raj = Employee("Raj", 1200000, "B")      
maya = Employee("Maya", 1200000, "C")