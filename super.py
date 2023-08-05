class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()


class Employee:#parent class 
  def __init__(self, name, id):
    self.name = name
    self.id = id
  
  def showinfo(self):
    print(f"The name of the employee {self.id} is {self.name}") 
   
class Programmer(Employee):#child class 
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

e = Employee("Rohan Das", "420")
e.showinfo()
a = Programmer("Shashi", "722047", "Python")
print(a.name,a.id,a.lang)