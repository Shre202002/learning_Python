#                                                   !!!!.........DECORATOR..........!!!!
# @classmethod ----------------> To to access the class attribute inited of the INSTANCE Attribute at the time of calling the class
# To overcome the INSTANCE ATTRIBUTE CLASSATRIBUTE is USED !!

class base_class:
    a = 44

    def data(self):
        print(f"Tha Value of the a In CLASS ATTRIBUTE IS; {self.a}")

b =base_class()
b.a = 100011

b.data()   #-----------> Instate ATTRIBUTE is overtaking the CLASS ATTRIBUTE..

class New_class:
    z = 30

    @classmethod  # -------------> Class method is used to access the class ATTRIBUTES OVER THE INSTANCE ATTRIBUTES 
    def show_data(cls):  #-------------> cls is used for access the class attributes inited of se lf
        print(f"Tha Value of the a In CLASS ATTRIBUTE IS {cls.z}")

z = 444
c = New_class()
c.show_data()


