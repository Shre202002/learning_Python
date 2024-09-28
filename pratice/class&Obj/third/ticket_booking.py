#Book Ticket and if don't get ticket alert if there is ticket give fare price and ticket Confirmation

from random import randint


train_info = []
pass_info = []
class Train:
       
       
    @staticmethod
    def use_func():
        a = Train.give_info()
        Train.add_info(a)
        
     
    def __init__(self, name, age , gender , ticket_no, train_no  ):
        self.name = name
        self.age = age
        self.gender = gender 
        self.ticket_no = ticket_no
        self.train_no = train_no
    
    @staticmethod
    def give_info():
       name = input("Enter Passenger's Name ")
       age = int(input(f"Enter {name}'s age: "))
       gender = input(f"Enter {name}'s Gender:" )
       ticket_no = randint(50000 , 99999)
       train_no =  randint(50000 , 50005)
       train_info.append(train_no)
       print((f"In Train {train_no} Passenger name is {name}, age is {age} {"his" if {gender} == "male" else "her"} ticket Number is {ticket_no} "))
    #    return( {"Train_No ": train_no, "Ticket_No: " : ticket_no,"name": name, "age": age, "Gender": gender, })
       return[ name, age,gender, train_no, ticket_no ]
   
    #    self.pass_info.append({"Train No ": train_no, "Ticket No: " : ticket_no,"name": name, "age": age, "Gender": gender, })
       
    

       
       
       
    
    
    def add_info(self):
        print(self, type(self))
        pass_info = (f"\nIn Train Number {self[3]} Passenger name is {self[0]}, age is {self[1]} {"his" if {self[2]} == "male" else "her"} ticket Number is {self[4]}")
            
               
            
        with open(rf"D:\learning_Python\pratice\class&Obj\third\{self[3]}.txt", "a+")  as f:   #--------> Creating the File as Per Train Number and adding data to them as per Train_Number  
            data = f.readlines()
            print(len(data))
            # f.seek(0)
            
            if (len(data) != 2): #------> In a train there is max 5 sates Available 
            
             for i in data:
 
                if  pass_info in data:
                    print(f"{self[0]} had already booked Ticket")
                    break
             else:
                f.write(pass_info)
                print(pass_info)
                print("Your Ticket  Booked Successfully ")
            
            else:
                print("No Seat is Available")
        
        with open(rf"D:\learning_Python\pratice\class&Obj\third\train_info_data.txt", "a")  as f:
            f.write(pass_info)
                


n = int(input("Enter The Number of Ticket You want to Book: "))
for i in range (n):
  A = Train.use_func()
    

    
            
             