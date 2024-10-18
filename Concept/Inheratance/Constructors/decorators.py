class decorator:

# @property   -----------> Use to create the NEW Instance ATTRIBUTE in The FUNCTION / METHOD 

 @property
 def name(self):
    return f"{self.fname} {self.lname}"

 @name.setter   #------------> .setter in DECORATOR used for setting the values/ Instance value which have been created 
 def name (self, value):
    self.fname = value.split( " ")[0]
    self.mname = value.split( " ")[1]
    self.lname = value.split( " ")[2]

d = decorator()
d.name ="Sriyansh Gupta hello "
print(d.fname , d.lname )