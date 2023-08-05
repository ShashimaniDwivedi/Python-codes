class Person:
  name="Shashi"
  occupation="Software Developer"
  def info(self):
    print(f"{self.name} is a {self.occupation}")
    

a=Person()
b=Person()
c=Person()
D=Person()
a.name="Harry"
a.occupation="Accountant"
# print(a.name,a.occupation)
c.name="Priya"
c.occupation='Data Scientist'
a.info()
b.info()
c.info()
#D.info()
    
    