class Calculaor1:
    def add(self, a,b):
        return a+b
class Calculaor2:
    def sub(self, a,b):
        return a-b
class Derived(Calculaor1, Calculaor2):
    def Divide(self, a,b):
        return a/b

d = Derived()
print(f"the sum is: {d.add(2,3)}")

class A:
    def m(self):
        print("In A")

class B(A):
    def m(self):
        print("In B")

class C(B,A):
    def m(self):
        print("In C")

class D(C,A):  # Multiple inheritance
    pass

obj = D()
obj.m()  # Output: In B

# Check MRO
print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
