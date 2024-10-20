class Number: 
    def __init__(self, n, title , author,m): #---------> Creating the Constructor for the CLASS NUMBER 
        self.n =n
        self.title =title
        self.author =author
    
    def __add__(self, num):  #--------------> It is the Dunder method which is being clled by default everytime 
        return self.n - num.n     #--------> __add__ is predefined dunder methods for the particular OPERATOR "+" 
                                                   #We can change the functionality of the OPERATOR BY OPERATOR OVERLOADING 
    def __mul__(self, num):
        return self.n * num.n

    def __sub__(self, num):
        return self.n * num.n

    def __truediv__(self, num):    #-----------> Return The Floating value 
        return self.n / num.n

    def __floordiv__(self, num):     #--------------> Return The INTIGER Value 
        return self.n // num.n
    
    def __str__(self):               #--------> The __str__() method is used to provide a readable string representation of an object, typically meant for human consumption. 
        return f"The Book {self.author} is written in {self.title}"  #--------->  It is automatically called when you use the print() function or str() on an object.

    def __len__(self): 
        return len(self.author)   #------> REturns the length of the object/ Parameter which is being recived by the class 

n = Number(10, "1900", "Orwell",20)
m = Number(20, "1984", "George", 40)
print(n)
print(f" the Length of Object is {len(n)}")
print(m+n)
print(m*n)
print(m//n)
print(m/n)
print(10+20)   #-------> Only act for the operators and operands 

