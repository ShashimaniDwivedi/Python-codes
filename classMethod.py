class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")
    
  @classmethod
  def changecompany(cls,newcompany):
    cls.company = newcompany
      
      
e1=Employee()
e1.name="Shashi"
e1.show()
e1.changecompany("Twitter")
e1.show()
print(Employee.company)     