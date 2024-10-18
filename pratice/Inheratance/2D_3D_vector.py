class twoD_Vector:

    def __init__(self, i,j):
        self.i = i
        self.j = j
     
    def show(self):
        print(f"The 2-D Vector Data is {self.i} + {self.j}")

    def __mul__(self ,  num):
        return   ((self.i *num.i)+(self.j * num.j))
        
class threeD_Vector(twoD_Vector):

    def __init__(self, i,j,k):
        super().__init__(i,j)
        self.k = k
     
    def show(self):
        print(f"The 3-D Vector Data is {self.i} + {self.j} + {self.k}")

    def __mul__(self ,  num):
        return   ((self.i *num.i)+(self.j * num.j)+ (self.k * num.k))

twoD1 = twoD_Vector(5,6)
twoD2 = twoD_Vector(10,20)
print(f"The Dot Product Of 2D vector  is  {twoD1 * twoD2}")

threeD1 = threeD_Vector(5,6,7)
threeD2 = threeD_Vector(10,20,30)
print(f"The Dot Product Of 3D vector  is  {threeD1 * threeD2}")
