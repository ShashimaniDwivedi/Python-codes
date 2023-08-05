class Employee:
  company="Microsoft"
  noOfEmployees=0
  def __init__(self,name):
    self.name=name
    self.raise_amt=0.02 #Instance variable
    Employee.noOfEmployees+=1
    
  def showData(self):
    print(f"The name of Employee {self.noOfEmployees} is {self.name} and the amt raised by {self.company} is {self.raise_amt}") 
    
# Employee.showData(e1) same as below a 
e1=Employee("Manas")
e1.raise_amt=0.3
e1.company="Apple"
e1.showData()   # a  
e2=Employee("Honey")
e2.showData()