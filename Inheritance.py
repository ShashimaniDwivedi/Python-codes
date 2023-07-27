class Employee:
  def __init__(self,name,id):
    self.name = name
    self.id = id
    
  def showdetails(self):
    print(f"The name of the employee {self.id} is {self.name}")  
  
  
class Programmer(Employee):
  def showLanguage(self):
    print("The Default language is Python")
    
e=Employee("Harry",420)
e.showdetails()
e1=Programmer("Raj",400)
e1.showdetails()
e1.showLanguage()        