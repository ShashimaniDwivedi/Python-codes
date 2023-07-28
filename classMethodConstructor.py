class Employee:
  
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
    
   #Alternative constructor 
  @classmethod 
  def fromstr(cls,string):
    return cls(string.split("-")[0],int(string.split("-")[1]))
   
e1=Employee("Shashi",120000)
print(e1.name)
print(e1.salary)

string ="Shashi-120000"
e2=Employee.fromstr(string) 
   
print(e1.name)
print(e1.salary)   