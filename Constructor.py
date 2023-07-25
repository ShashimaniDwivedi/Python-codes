class Person:
  name="Shashi"
  occupation="Software Developer"
  def __init__(self,name,occupation): #Constructor
    self.name=name
    self.occupation=occupation
  def info(self):
    print(f"{self.name} is a {self.occupation}")
    
    
a=Person("Priya","HR")
b=Person("Shashi","Developer")
a.info()
b.info()    